import secrets
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .engine import createFavicons
from .models import Image, Favicon_Zip
from accounts.models import CustomUser
from datetime import date


current_year = date.today().year
def dashBoardView(request):
    context = {'current_year': current_year}
    return render(request, 'core/dashboard.html', context)


@login_required
def imageUploadView(request):
    context = {'current_year': current_year}
    images = Image.objects.filter(user_id=request.user)
    imgs = []
    for image in images:
        favicon = Favicon_Zip.objects.get(image_id=image)
        img = {"image": image, "favicon": favicon}
        imgs.append(img)
    if request.method == 'POST':
        list(messages.get_messages(request))
        try:
            image = request.FILES['image'] or request.POST['image']
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
            return redirect('core:upload')
        except:
            messages.info(request, 'Image not provided')
            return render(request, 'core/upload.html', context)
    else:
        return render(request, 'core/upload.html', {'images': imgs, 'current_year':current_year})


@login_required
def userProfileView(request):
    images = Image.objects.filter(user_id=request.user)
    imgs = []
    for image in images:
        favicon = Favicon_Zip.objects.get(image_id=image)
        img = {"image": image, "favicon": favicon}
        imgs.append(img)
    if request.method == 'POST':
        list(messages.get_messages(request))
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        if username != request.user.username and CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('core:profile')
        elif email != request.user.email and CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Email address already exists')
            return redirect('core:profile')
        else:
            user = CustomUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            if request.FILES:
                profile_pic = request.FILES['new_image']
                user.profile_pic = profile_pic
            user.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('core:profile')
    else:
        return render(request, 'core/user_profile.html', {'images': imgs, 'current_year': current_year})


@login_required
def deleteImageView(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return redirect('core:upload')


class AboutPageView(TemplateView):
    template_name = "core/about.html"
    extra_context = {'current_year': current_year}

class ContactPageView(TemplateView):
    template_name = "core/contact.html"
    extra_context = {'current_year': current_year}


class FAQPageView(TemplateView):
    template_name = "core/faq.html"
    extra_context = {'current_year': current_year}