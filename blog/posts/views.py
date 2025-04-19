from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_create(request):

     form=PostForm(request.POST or None)

     if form.is_valid():
           instance = form.save(commit=False)
           print(form.cleaned_data.get("title"))
           instance.save()
           messages.success(request,"successfully created.")
           return redirect('posts:detail',instance.id)
     
     context = {
           "form": form,
      }
          
     return render(request,"post_form.html",context)
 

def post_detail(request,id): #retrieve

     instance=get_object_or_404(Post,id=id)

     context={
         "title":"Detail",
         "instance":instance
     }

     return render(request,'post_detail.html',context)
 

def post_list(request): #list items

     queryset=Post.objects.all()

     context={
          "object_list":queryset,
          "title":"List"
     }

     return render(request,'index.html',context)
 


def post_update(request,id):
     instance=get_object_or_404(Post,id=id)

     form=PostForm(request.POST or None,instance=instance)

     if form.is_valid():
           instance = form.save(commit=False)
           print(form.cleaned_data.get("title"))
           instance.save()
           return redirect("posts:detail", instance.id)
           messages.success(request,"successfully updated.")
     
     context = {
           "form": form,
      }
          
     return render(request,"post_form.html",context)
 


def post_delete(request,id):
     instance=get_object_or_404(Post,id=id)
     instance.delete()
     messages.success(request,"successfully deleted")
     return redirect("posts:list")

