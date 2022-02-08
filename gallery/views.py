from django.shortcuts import  render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
import os
from django.shortcuts import render,redirect
from gallery.models import Category, Photo
from django.contrib import messages

# Create your views here.

def homepage(request):
	return redirect('/login')

def gallery(request):
    category = request.GET.get('category')
    myphotos = Photo.objects.filter(user= request.user)
    if category == None:
        photos = myphotos
    else:
        photos = myphotos.filter(category__name=category)
    categories = Category.objects.filter(user=request.user)
    context = {
        "categories":categories,
        "photos":photos,
    }
    return render(request, 'gallery/photos.html',context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'gallery/viewphoto.html',{'photo':photo})

def addphoto(request):
    categories = Category.objects.filter(user=request.user)
    if request.method=='POST':
        data=request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category,created  = Category.objects.get_or_create(user = request.user, name = data['new_category'])
        else:
            category=None
        photo = Photo.objects.create(user = request.user, category = category,description = data['description'],image = image )
        photo.save()
        return redirect('gallery')
    context = {
        "categories":categories,
    }
    return render(request, 'gallery/addphoto.html',context)

def deleteImage(request,pk):
    image = Photo.objects.get(id=pk)
    if len(image.image) > 0:
        os.remove(image.image.path)
    image.delete()
    messages.success(request,"Image Deleted Successfuly")
    return redirect('gallery')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/gallery")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="gallery/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/gallery")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "gallery/login.html", {"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login")