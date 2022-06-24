from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.timezone import now
from tinymce.models import HTMLField



# Create your models here.
class Profile(models.Model):
    class Meta:
        db_table = "user_profile"

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=1)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    paragraph = models.TextField()
    url = models.CharField(max_length=100)
    # createdOn=models.DateTimeField(auto_now=True,null=True)
    updatedOn = models.DateTimeField(auto_now_add=True, null=True)


    def icon_tag(self):
        return format_html('<img src=" /media/{}" style="width:40px;height:40px",border-radius:50%  >'.format(self.icon))

    def __str__(self):
        return self.title


class post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    prim_img = models.ImageField(upload_to="pics")
    heading = models.CharField(max_length=100)
    sec_img = models.ImageField(upload_to="pics")
    heading2 = models.CharField(max_length=100,default='SOME STRING')
    paragraph = models.CharField(max_length=100,default='SOME STRING')
    is_published=models.BooleanField(default=False)



    def __str__(self):
        return self.title


class contactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=10)
    message = models.TextField()


class authorInsight(models.Model):
    img = models.ImageField(upload_to="pics")
    title2 = models.CharField(max_length=100)
    list = models.CharField(max_length=100)
    paragraph2 = models.TextField()


# class portfolios(models.Model):
#     img2 = models.ImageField()


class post_details(models.Model):
    img3 = models.ImageField(upload_to="pics")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title3 = models.CharField(max_length=100)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    projDate = models.CharField(max_length=100)
    Blogtitle = models.CharField(max_length=100)
    Blogdes = models.CharField(max_length=100)
    BlogContent = HTMLField()
    posted_on = models.DateField(auto_now_add=True,null=True)
    primary_heading = models.CharField(max_length=100,default='')
    primary_paragraph = models.TextField(default='')

    def __str__(self):
        return self.title3


class BlogComment(models.Model):
    sno =models.AutoField(primary_key='True')
    comment = models.TextField()
    name = models.TextField()
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

class ViewCount(models.Model):
    id = models.AutoField(primary_key='True')
    post_id = models.ForeignKey(post,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_table")





