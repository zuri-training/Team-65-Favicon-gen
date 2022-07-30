# from PIL import Image
# from zipfile import ZipFile
# import os

# filename = r'logo.png'
# img = Image.open(filename)

# dimensions = [(16,16), (24,24), (32,32), (48,48), (64,64)]

# with ZipFile('logo.zip', 'w') as zipObj:
#     for i in range(len(dimensions)):
#         img.save('logo{dimension}.ico'.format(dimension=dimensions[i]), format='ICO', sizes=[dimensions[i]])
#         zipObj.write('logo{dimension}.ico'.format(dimension=dimensions[i]))
#         os.remove('logo{dimension}.ico'.format(dimension=dimensions[i]))
