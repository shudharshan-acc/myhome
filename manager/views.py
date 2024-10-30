from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VideoForm,UpdateForm,InventoryForm
from .models import videos,inventory
# Create your views here.
@login_required(login_url="/security/login/")
def manager(request):
    return render(request,"manager/manage.html")


# Videos section
@login_required(login_url="/security/login/")
def readvideo(request):
    if request.method == 'POST':
        search = request.POST['search']
        video = videos.objects.filter(vidname__icontains=search).all()        
    else:
        video = videos.objects.filter(username=request.user).all()
   
    return render(request,"manager/videos/video.html",{'vid':video})

@login_required(login_url="/security/login/")
def edit_video(request, video_id):
    video = get_object_or_404(videos, id=video_id)  # Fetch the video object
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=video)  # Bind the form with the video instance
        if form.is_valid():
            form.save()  # Save the updated video details
            messages.success(request, 'Video updated successfully!')
            return redirect('/manager/readvideo/')  # Redirect to the page that lists videos
    else:
        form = UpdateForm(instance=video)  # Create a form instance with the existing video details

    return render(request, 'manager/videos/edit_video.html', {'form': form, 'video': video})  # Render the edit template

@login_required(login_url="/security/login/")
def add_video(request):
    if request.method == 'POST':
        
        form = VideoForm(request.POST)  # Include files in the request
        form.username = request.user
        if form.is_valid():
            form.save()  # Save the video to the database
            return redirect('/manager/readvideo/')  # Redirect to the list of videos after saving
    else:
        form = VideoForm()  # Create an empty form

    video = videos.objects.all()  # Fetch all videos for display
    return render(request, 'manager/videos/add_video.html', {'form': form, 'videos': video})

@login_required(login_url="/security/login/")
def delete_video(request,video_id,username):
    video = videos.objects.get(id=video_id)
    if video and request.user.username==username:
        video.delete()
        return redirect('/manager/readvideo')
    else:
        return redirect('/manager/readvideo')
    
# Inventory management
@login_required(login_url="/security/login/")
def readinventory(request):
    if request.method == 'POST':
        search = request.POST['search']
        inven = inventory.objects.filter(item__icontains=search).all()        
    else:
        inven = inventory.objects.filter(username=request.user).all()
   
    return render(request,"manager/inventorys/inventory.html",{'inv':inven})

@login_required(login_url="/security/login/")
def add_item(request):
    if request.method == 'POST':
        
        form = InventoryForm(request.POST)  # Include files in the request
        form.username = request.user
        if form.is_valid():
            form.save()  # Save the video to the database
            return redirect('/manager/readinventory/')  # Redirect to the list of videos after saving
    else:
        form = InventoryForm()  # Create an empty form

    inv = inventory.objects.all()  # Fetch all videos for display
    return render(request, 'manager/inventorys/add_item.html', {'form': form, 'inv': inv})

@login_required(login_url="/security/login/")
def delete_item(request,item_id,username):
    inv = inventory.objects.get(id=item_id)
    if inv and request.user.username==username:
        inv.delete()
        return redirect('/manager/readinventory')
    else:
        return redirect('/manager/readinventory')
    
@login_required(login_url="/security/login/")
def increment_item(request,item_id,username):
    inv = inventory.objects.get(id=item_id)
    if inv and request.user.username==username:
        inv.quan+=1
        inv.save()
        return redirect('/manager/readinventory')
    else:
        return redirect('/manager/readinventory')

@login_required(login_url="/security/login/")
def decrement_item(request,item_id,username):
    inv = inventory.objects.get(id=item_id)
    if inv and request.user.username==username and inv.quan>0:
        inv.quan-=1
        inv.save()
        return redirect('/manager/readinventory')
    elif inv.quan<=0:
        return delete_item(request,item_id,username)
    else:
        return redirect('/manager/readinventory')