import sys
import os
from twython import Twython

# go here and create a new app: https://apps.twitter.com
# then click "key and access tokens" to generate them
# put them inside the quotes below

CONSUMER_KEY = 'your consumer key here'
CONSUMER_SECRET = 'your consumer secret here'
ACCESS_KEY = 'your access key here'
ACCESS_SECRET = 'your access secret here'


# this runs the following script from the command line that takes the photo and saves it
# it will only work for USB webcams,
# you'll have to do something different if you're using a pi-cam
# if you find your webcam can't handle light levels use -S xx to specify skip frames before photo capture
# capture a second timestamped photo plant-%Y-%m-%d.jpg to start gathering images for your inevitable timelapse
os.system ("fswebcam -d/dev/video0 -r1280x960 -S 45 --no-banner plantpic.jpg plant-%Y-%m-%d--%H-%M-%S.jpg")

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
photo = open('plantpic.jpg','rb')
image_ids = api.upload_media(media=photo)
api.update_status(status='', media_ids=image_ids['media_id'])
