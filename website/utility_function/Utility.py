from PIL import Image

def uploadImage(Image2):
    image = Image.open(Image2)
    # image.thumbnail((400, 400))
    # rgb_im =image.convert('RGB')
    image.save('media/pics/'+str(Image2).replace(" ", ""))
    imageFile ="pics/"+str(Image2).replace(" ", "")
    return imageFile