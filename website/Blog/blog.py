from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from website.models import post_details
from website.models import Categories
from website.models import post
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.views import View
from website.utility_function.Utility import uploadImage
from PIL import Image
import os

class addPost(View):
    def get(self,request):
        cat=Categories.objects.filter().values('id','title')
        print('---------',cat)
        return render(request,'AddBlog.html',{'category':cat})



    def post(self,request):
        data = request.POST
        img1 = request.FILES['prim_img']
        img2 = request.FILES['sec_img']
        img1_path = uploadImage(img1)
        img2_path = uploadImage(img2)
        User_data = request.session.get("user_id")
        print('###wow###',User_data)
        ############################ cat=category.objects.get(id=data['category_id']) ####################################
        
        new_post=post.objects.create(title=data['title'],category_id=data['category_id'], prim_img=img1_path,
                                                heading=data['heading'], sec_img=img2_path,heading2=data['heading2'],paragraph=data['paragraph'],is_published=0)
                                      
        print('==================',new_post,post.id)  
        print(request.POST)                                      
  



        c=post_details.objects.create(user_id=User_data,img3=img1_path,title3=data["title"],post=new_post,client=data["Client"],projDate=data["ProjDate"],Blogtitle=data["Blog_title"],Blogdes=data["Blog_des"],BlogContent=data["BlogContent"],primary_heading=data["Primary_heading"],primary_paragraph=data["Primary_paragraph"])
        print(c)
        return redirect('/post')
    
class myBlog(View):
    
    def get(self,request):
        
        id = request.session.get("user_id")
        print("###oops###",id)
        list = post.objects.filter(post_data__user__id=id).values('id','title','prim_img','heading','sec_img','heading2','paragraph')
    

        return render(request,'myBlog.html',locals())

