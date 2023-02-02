# Generating a qrcode for my Instagram
# After running pip install qrcode and PIL Install pillow
#import the qrcode and image
import qrcode 
from PIL import Image
instagram = "https://www.instagram.com/denzelgitonga/"
# Encoding the link
instagram_url = qrcode.make(instagram)
#save
instagram_url.save("instagram.png")