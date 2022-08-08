import secrets
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .engine import createFavicons
from .models import Image, Favicon_Zip


def dashBoardView(request):
    return render(request, 'core/dashboard.html')


@login_required
def imageUploadView(request):
    if request.method == 'POST':
        list(messages.get_messages(request))
        if request.FILES:
            image = request.FILES['image']
            imgid = f'{request.user}_image-{secrets.token_urlsafe(10)}'
            zipid = f'{request.user}_favicon-{secrets.token_urlsafe(10)}'
            url_list = createFavicons(image, imgid, zipid)
            res_img, res_zip = url_list.values()
            image = Image.objects.create(
                user_id=request.user, image_name=imgid, image_url=res_img
            )
            image.save()
            favicon = Favicon_Zip.objects.create(
                user_id=request.user, image_id=image, favicon_name=zipid, favicon_zip_url=res_zip
            )
            favicon.save()
            return redirect('core:download', pk=image.pk)
        else:
            messages.error(request, 'Image not provided')
            return render(request, 'core/upload.html')
    else:
        return render(request, 'core/upload.html')


@login_required
def imageListView(request):
    images = Image.objects.filter(user_id=request.user)
    return render(request, 'core/image_list.html', {'images': images})


@login_required
def downloadFaviconView(request, pk):
    image = Image.objects.get(id=pk)
    favicon = Favicon_Zip.objects.get(image_id=image)
    return render(request, 'core/favicon_download.html', {'favicon': favicon, 'image': image})


@login_required
def deleteImageView(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return redirect('core:image-list')