__author__ = 'Scott'


#RUN CAMERA

#GREAT JOB

#NEVER STOP

#GOOD
import os
import time
import picamera

from ftplib import FTP as ftp

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (2592, 1944)
    time.sleep(2)
    for filename in camera.capture_continuous('{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
	session = ftp()
	session.connect("ftp.oureportfolio.com",21)
	session.login("username","password")
	session.cwd("public_html/timelapse/")
	session.storbinary('STOR ' + filename, open(filename, 'rb'))
	print('Uploaded ' + filename)
	session.close()
	os.system('rm ' + filename)
	print('Removing ' + filename)
        time.sleep(300) # wait 5 minutes
