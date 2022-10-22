# Generating qrcode
# Import the module
import qrcode
#import the image
from PIL import Image
# Assign the content to be encoded
linkedin = "https://www.linkedin.com/in/denzel-gitonga-67622b208/"
#Encode it
linkedin_qrcode = qrcode.make(linkedin)
#Save the image
linkedin_qrcode.save('my_linkedin_url.png')