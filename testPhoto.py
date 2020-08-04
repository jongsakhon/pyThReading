from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution = (64, 64)
camera.start_preview()
sleep(3)
camera.capture('testPho2.jpg')
camera.stop_preview()