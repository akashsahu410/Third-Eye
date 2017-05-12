import cv2
import cloudsight
from json import load
from urllib2 import urlopen
import serial
import urllib2
import cookielib
from getpass import getpass
import os
import sys
import httplib, urllib
import gmplot
from twilio.rest import TwilioRestClient

gmap = gmplot.GoogleMapPlotter(12.8404, 80.1525,15)

lat = [12.8404]
log = [80.1525]

for i in range (500):
    lat.append(12.8404)
    log.append(80.1525)

for i in range(0, 500):
    lat.append(12.8404-float(i/100))
    log.append(80.1525-float(i/100))

for i in range(0, 500):
    lat.append(12.8404-float(i/100))
    log.append(80.1525-float(i/100))

for i in range(0, 500):
    lat.append(12.8404-float(i/100))
    log.append(80.1525+float(i/100))

for i in range(0, 500):
    lat.append(12.8404-float(i/100))
    log.append(80.1525-float(i/100))

for i in range(0, 500):
    lat.append(12.8404-float(i/100))
    log.append(80.1525-float(i/100))

gmap.heatmap(lat, log) 

#gmap.plot(lat, log, 'cornflowerblue', edge_width = 8)
gmap.draw("map.html")
#os.system('firefox map.html')

key = 'PKHDQGM4BTGH9PK1'       #thingspeak key
def sms(msg4):
    accountSid = 'ACb4685d583d4b2918859fcda3d1c1e4a6'
    authToken = 'c6dbfe5e027080256a0c9bc4e0af68f6'
    twilioClient = TwilioRestClient(accountSid, authToken)
    myTwilioNumber = '+12513330106'
    destCellPhone = '+917358297069'
    myMessage = twilioClient.messages.create(body = msg4, from_=myTwilioNumber, to=destCellPhone)

        


def thingspeak(temp):
    #temp = 1
    params = urllib.urlencode({'field1': temp, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print temp
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"

cam = cv2.VideoCapture(3)                    #main program
cv2.namedWindow("test")
img_counter = 0

while True:                                  #capturing image
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

auth = cloudsight.OAuth('6qj8DDj8TmCfYkl6Ysx5cg','U2RLYEjRHUZpmrrvtiKMww')              #cloudsight
api = cloudsight.API(auth)  

with open('opencv_frame_0.png', 'rb') as f:
    response = api.image_request(f, 'opencv_frame_0.png', {
        'image_request[locale]': 'en-US',
    })

status = api.wait(response['token'], timeout=30)
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    #    print status
    pass

statusStr = str(status)  # Converts the status to string 
char = 'name'        
colan = "',"         
indexOfName =  statusStr.find(char)   # Search for the string:[name] in the string
tempStr = statusStr[indexOfName+9:]   # Extracts the entire string after the [name] string
indexOfColan = tempStr.find(colan)    # From the extracted string get the index of colan
#print tempStr[:indexOfColan]         # Prints only the required string 

desc = tempStr[:indexOfColan]          # contains descriptor
print desc

flagmap = 0 
if "orange screwdriver" in desc:
        msg = "LETHAL WEAPON DETECTED AT CAMERA \nDescription :" + desc
        sms(msg)
        thingspeak(1)
        flagmap = 1
elif "knife" in desc:
        msg = "LETHAL WEAPON DETECTED AT CAMERA \nDescription :" + desc
        sms(msg)
        thingspeak(0.5)
        flagmap = 1

elif "gun" in desc:
        msg = "LETHAL WEAPON DETECTED AT CAMERA \nDescription :" + desc
        sms(msg)
        thingspeak(1.5)
        flagmap = 1



if flagmap==1:
    os.system('firefox map.html')


cam.release()
cv2.destroyAllWindows()
