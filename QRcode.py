import qrcode


print('url:')
data = input()
img = qrcode.make(data)

img.save('QRCODE.png')

