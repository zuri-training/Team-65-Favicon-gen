import cloudinary
from PIL import Image
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path

# getting the file to read the .env folder for cloudinary info
root = Path(__file__).resolve().parent.parent


def createFavicons(img, imgid, zipid):
    # create temporary storage
    image_path = root/'tempstorage'
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    #os.mkdir(os.path.join(root, 'tempstorage' ))
    os.mkdir(image_path)
    # loop through sizes, convert image into different sizes and formats, save converted files to tempstorage
    sizes = [(16, 16), (32, 32), (180, 180), (192, 192), (512, 512)]
    current_Image = Image.open(img)
    current_Image.save(f'{image_path}/favicon_image.png')
    for size in sizes:
        new_image = current_Image.resize(size)
        new_image.save(f'{image_path}/favicon{size[0]}x{size[1]}.png')
    new_image = current_Image.resize((48, 48))
    new_image.save(f'{image_path}/favicon.ico')
    # zip all files in tempstorage including site manifest in the core
    with ZipFile(root/'tempstorage/favicon.zip', 'w', ZIP_DEFLATED) as zip:
        os.chdir(image_path)
        for x in os.listdir():
            if x != 'favicon_image.png':
                zip.write(x)
        os.chdir(root/'core')
        zip.write('site.webmanifest')
        zip.close()
    # upload image and zipped file to cloudinary and retrieve url
    os.chdir(root)
    responseImage = cloudinary.uploader.upload(
        root/'tempstorage/favicon_image.png', public_id=imgid)
    responseZip = cloudinary.uploader.upload(
        root/'tempstorage/favicon.zip', public_id=zipid, resource_type='auto')
    res_img = responseImage['secure_url']
    res_zip = responseZip['secure_url']
    # delete tempstorage
    shutil.rmtree(image_path)
    return {'res_img': res_img, 'res_zip': res_zip}
