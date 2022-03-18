# pip3 install qrcode

# import essential libraries
import qrcode

# libraries for rounded corners
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# library for logo creation
from PIL import Image

# example data of the website or application
data = input('Enter the URL you want to encode: ')  # https://github.com/supun-chamika

# open logo
logo = Image.open('logo.png')

# taking base width
base_width = 100

# adjust image size
width_percent = (base_width / float(logo.size[0]))
hSize = int((float(logo.size[1]) * float(width_percent)))
logo = logo.resize((base_width, hSize), Image.ANTIALIAS)

# instantiate QRCode object
QR = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=3)

# add data to qr code
QR.add_data(data)

# generate qr code
QR.make(fit=True)

# transfer the array into an actual image
img = QR.make_image(image_factory=StyledPilImage,
                    module_drawer=RoundedModuleDrawer(1),
                    fill_color='black',
                    back_color='white')

# set size of QR code
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)

# paste logo in QR code
img.paste(logo, pos)
# save img to a file
img.save('myQR_code.png')
print('Your QR code have been generated successfully!')
