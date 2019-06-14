#take picture and send to server

import requests as req
from PIL import Image
from io import BytesIO

response = req.get('http://101.6.114.11:8080/?action=snapshot')
image = Image.open(BytesIO(response.content))
image.show()


