from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
# Create your views here.
from . import Assignment_Writer
from PIL import Image
import base64
from io import BytesIO
import numpy as np
page = Image.open("files/newoptimal.jpg")
page = np.asarray(page)
def index(request):
    return render(request,"index.html",{})

def write(request):
    def get(value):
        return request.GET.get(value)

    string = get('string')
    fontwidth = get('fontwidth')
    fontheight = get('fontheight')
    tableft = get('tableft')
    tabright = get('tabright')
    fontsize = get('fontsize')
    fontcolor = get('fontcolor')[1:]
    fontcolor = (int(fontcolor[:2],16),int(fontcolor[2:4],16),int(fontcolor[4:6],16))
    AW = Assignment_Writer.Assignment_Writer(page=page.copy(), string=string, FONT_SIZE=tuple(map(int,fontsize.split())), FONT_COLOR=fontcolor,
                           FONT_SIZE_HEIGHT=int(fontheight), FONT_SIZE_WIDTH=int(fontwidth), tab_left=int(tableft),
                           tab_right=int(tabright))
    output = AW.generate()
    buffered = BytesIO()
    output.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return HttpResponse(img_str,content_type="image/jpeg")





# try:
#     with open(valid_image, "rb") as f:
#         return HttpResponse(f.read(), content_type="image/jpeg")
# except IOError:
#     red = Image.new('RGBA', (1, 1), (255,0,0,0))
#     response = HttpResponse(content_type="image/jpeg")
#     red.save(response, "JPEG")
#     return response