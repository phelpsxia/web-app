#take picture and send to server

import requests as req
from PIL import Image
from io import BytesIO

response = req.get('http://101.6.114.11:8080/?action=snapshot')
#image = Image.open(BytesIO(response.content))

url = 'http://[2001:da8:270:2018:f816:3eff:fe98:4550]:8888/streaming'
res = req.request("POST",url, data=response.content)



