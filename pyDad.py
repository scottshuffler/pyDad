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
	try:
		session = ftp()
		session.connect("192.168.1.2",21)
		session.login("username","password")
		session.cwd("admin/timelapse/")
		session.storbinary('STOR ' + filename, open(filename, 'rb'))
		print('Uploaded to NAS' + filename)
		session.close()
	except Exception as ex:
		print('Error: ' + str(ex))
	try:
                session = ftp()
                session.connect("ftp.oureportfolio.com",21)
                session.login("username","password")
                session.cwd("public_html/timelapse/")
                session.storbinary('STOR ' + filename, open(filename, 'rb'))
                print('Uploaded to webserver' + filename)
                session.close()
        except Exception as ex:
                print('Error: ' + str(ex))
	finally:
		os.system('rm ' + filename)
		print('Removing ' + filename)
        time.sleep(600) # wait 5 minutes
