import qrcode as qr


qr = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/themanuca')

img = qr.make_image(fill_color="black", back_color="white")

img.save('qr_git.jpg')