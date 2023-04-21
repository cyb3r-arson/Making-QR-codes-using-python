Making QR codes using Python.
import qrcode


text = "Hello, world!"


qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(text)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")
