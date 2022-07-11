from rest_framework import serializers
from datetime import datetime



#creating a serializer

class BlogCommentSerializers(serializers.Serializer):
    
    Comment = serializers.CharField()
    Name = serializers.CharField()
    
    













# class Comment(object):
#     def __init__(self,email,content,created= none):
#         self.email=email
#         self.content=content
#         self.created=created or datetime.now()

 
# comment = Comment(email="vikrant@gmail.com",content="hi this is vikrant")     


# serializer = CommentSerializer(comment)




