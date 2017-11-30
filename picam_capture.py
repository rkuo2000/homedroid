from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
print('capturing image...')
sleep(3)
camera.capture('image.jpg')
camera.stop_preview()
