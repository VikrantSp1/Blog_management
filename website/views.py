from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Categories, post_details,post,BlogComment
from .models import authorInsight, Profile, contactInfo ,ViewCount
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Q
from .serializers.serializers import BlogCommentSerializers
from datetime import datetime
# Create your views here.
from django.shortcuts import redirect


def home(request):
    if request.method == "GET":
        try:
            # a2 =Profile.objects.filter(country='Pakistan').values('user__username','state','city','user__email')
            # a2 = Profile.objects.filter(country='India', isactive=1).values('user__username', 'state', 'city',
            #                                                                 'user__email')
            # print('1')
            # print(a2)
            username=""
            if request.user.is_authenticated:
                print('55')   
                print(request.user) 
                username= request.user.username
                firstname=request.user.first_name
                print(firstname)
                print('66')
            print('1')
            dests = Categories.objects.filter().values('id','icon', 'title', 'paragraph')
            print('2')
            # sa= authorInsight.objects.filter().values('img','title2','paragraph2','list')[0]
            sa = authorInsight.objects.filter().values('img', 'title2', 'paragraph2', 'list')
            print('3')
            portfolioImg = post_details.objects.filter(post__is_published=1).values('id','post_id','img3','post__is_published')
            print('4')

            query1= post.objects.filter(heading= 'v heading').values('title','category__id')
            
            query2 =post.objects.filter(heading2='v heading 2').values('title','category__id')

            y =query1|query2

            a= post.objects.filter( Q(heading='v heading')  |  Q(heading2='v heading 2')| Q(id__gt=1)).values('prim_img','title','category__id')
            print('aaa',a)
            for x in a:
                print('yyy',x)
                print("====+======+====")



            b= User.objects.filter(Q(first_name="viki") & Q(id=4)).values('first_name','id')
            print('4444b444',b)    
         
            return render(request, 'home.html', {'dest': dests, 'saa': sa, 'port': portfolioImg ,'username':username})
        except Exception as E:
            print("----------")
            print(E)
            return HttpResponse(str(E))
    else:
        print("actual post portfolio")

        return render(request,'blogpage.html')



# gives a list of posts by taking a category id as paramerter
@login_required(login_url='/login')
def list_posts(request,category_id):
    info=post.objects.filter(category_id=category_id,is_published=True).values('id','prim_img', 'heading','sec_img','heading2','paragraph')
    return render(request, 'post.html',{'x':info})



@login_required(login_url='/login')
def postdetails(request,post_id):
    print("under post_details")
    try:

        a=99
        b=343243535
        print("=-=-=-=-")
        post_obj=post.objects.get(id=post_id)
        if not ViewCount.objects.filter(post_id=post_id,user_id=request.user):
            b=ViewCount(post_id=post_obj,user_id=request.user)
            b.save()

            post_count = ViewCount.objects.filter(post_id=post_id).count()
            post_details.objects.filter(post_id=post_id).update(views=post_count)

            
        
        


        print('###')
        print('####@@@@###',request.user)

        commentData=BlogComment.objects.filter(post_id=post_id).values('name','comment','timestamp__date')
        print(commentData)

        post_obj = post.objects.filter(id=post_id).values('category_id')[0]
        category_id = post_obj['category_id']
        Latest_info = post.objects.filter(category_id=category_id).exclude(id=post_id).values('id', 'prim_img', 'heading','heading2')
        print()
        data = post_details.objects.filter(post_id=post_id).values('id','img3','title3','client','projDate','Blogtitle','posted_on','BlogContent','primary_heading','primary_paragraph','views')

        return render(request,'post-details.html',{'post_details':data , 'Latest_info':Latest_info,'post_id':post_id,'commentData':commentData})

    except Exception as e:
        print(e,"==================")

        return HttpResponse(str(e))


def postComment(request,post_id):
    print("under postcomment","sdjklhasdjkhasdhd")
    try: 

        if request.method == "POST":
            #print("post")
            #print(request.POST)
            #print(request.POST.get('Comment'),request.POST.get('Name'))
            
            #print(request.POST)
            data = request.POST
            form=BlogCommentSerializers(data=data)            
            if form.is_valid():
                print("11111",form)
               
                comment2 = BlogComment(post_id=post_id,comment=data["Comment"], name=data["Name"])
                
                comment2.save()
            else:
                print('123')
                print(form.errors)
                return HttpResponse(form.errors)
                
            # messages.success(request, "Your comment has been posted successfully")

            return redirect("/post_details/"+ str(post_id))
    
    except Exception as e:
        print(e,"==================")

        return HttpResponse(str(e))


def Contact(request):
    print("entered in contact function")
    if request.method == "POST":
        print("data is savedddd")
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = contactInfo(name=name, email=email, subject=subject, message=message)
        data.save()
        print('data is saved')

        return redirect('/?message=Information successfully saved')
    else:
        print("not savedddd")
        return render(request, 'home.html')


def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session["user_id"]=user.id
            User_data = request.session.get("user_id")
            print("1111333",User_data)
            return redirect('/')
            
        else:
            messages.info(request, 'invalid credential')
            return redirect('/login')

    else:
        return render(request, 'login.html')

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # number = request.POST.get('number')
        email = request.POST.get("email")
        # address = request.POST.get("address")
        # pincode = request.POST.get("pincode")
        password = request.POST.get("password")
        Cpassword = request.POST.get("password1")

        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save()
                request.session["user_id"]=user.id
                print('user created')
                User_data = request.session.get("user_id")
                print("333333",User_data)
                return redirect('login')
        else:
            messages.info(request, "password not matching...")
            return redirect('/register')
        return redirect('/')
    else:
        return render(request, 'register.html')

        return HttpResponse(" Welcome ")

# from django.db import connection
# cursor = connection.cursor()
# def stored_procedure(request):
#     try:
#         cursor.execute('call Product1')
#         result = cursor.fetchall()
#         return render(request,'storedprod.html',{'result':result})
#     finally:
#         cursor.close()



cursor = connection.cursor()
def stored_procedure(request):
    try:
        cursor.execute('call Getcontactinfos (%s)',[1])
        result = cursor.fetchall()
        return render(request,'para.html',{'result':result})
    except Exception as e:
        print(e)
        cursor.close()

        return render(request,'para.html',{'result': str(e)})


