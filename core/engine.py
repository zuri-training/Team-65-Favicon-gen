import cloudinary.api
import cloudinary.uploader
import cloudinary
from PIL import Image
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
import dotenv
from pathlib import Path

# getting the file to read the .env folder for cloudinary info
root = Path(__file__).resolve().parent.parent
dotenv.read_dotenv(root / '.env')

# setting cloudinary configuration globally
cloudinary.config(
    cloud_name=str(os.getenv('CLOUD_NAME')),
    api_key=str(os.getenv('CLOUD_KEY')),
    api_secret=str(os.getenv('CLOUD_SECRET')),
    secure=True
)


def createFavicons(img, imgid, zipid):
    # create temporary storage
    image_path = 'tempstorage'
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
    with ZipFile('tempstorage/favicon.zip', 'w', ZIP_DEFLATED) as zip:
        os.chdir(image_path)
        for x in os.listdir():
            if x != 'favicon_image.png':
                zip.write(x)
        os.chdir('../core')
        zip.write('site.webmanifest')
        zip.close()
    # upload image and zipped file to cloudinary and retrieve url
    os.chdir('../')
    responseImage = cloudinary.uploader.upload(
        './tempstorage/favicon_image.png', public_id=imgid)
    responseZip = cloudinary.uploader.upload(
        './tempstorage/favicon.zip', public_id=zipid, resource_type='auto')
    res_img = responseImage['secure_url']
    res_zip = responseZip['secure_url']
    # delete tempstorage
    shutil.rmtree(image_path)
    return {'res_img': res_img, 'res_zip': res_zip}