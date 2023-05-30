import qrcode

data = 'test'
img = qrcode.make(data)

img.save('QRCODE.png')

