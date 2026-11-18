'''
we are going to use a python library like qrcode and conver url to QR
'''

import qrcode
url=input("Enter your url: ")
name=input("Enter the name you want to save as: ")

if not(name.endswith('.png')):
    name=name+'.png'

image=qrcode.make(url)
image.save(name)
