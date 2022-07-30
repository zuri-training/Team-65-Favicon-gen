from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from .forms import *


from PIL import Image
from zipfile import ZipFile
import os


# Create your views here.

def page(request):

    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)

        if form.is_valid():
            # save locally
            uploaded_file = request.FILES['image']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)

            
            # get locally
            filename = r'.' + fs.url(name) 
            img = Image.open(filename)

            new_name = './media/' + uploaded_file.name + '.zip'

            dimensions = [(16,16), (24,24), (32,32), (48,48), (64,64)]

            with ZipFile(new_name, 'w') as zipObj:
                for i in range(len(dimensions)):
                    img.save('logo{dimension}.ico'.format(dimension=dimensions[i]), format='ICO', sizes=[dimensions[i]])
                    zipObj.write('logo{dimension}.ico'.format(dimension=dimensions[i]))
                    os.remove('logo{dimension}.ico'.format(dimension=dimensions[i]))
                

            context = {'url': new_name, 'title': uploaded_file.name}
            os.remove(filename)

            return render(request, 'webapp/index.html', {'context': context})

    else:
        form = imageForm() 

    return render(request, 'webapp/index.html')