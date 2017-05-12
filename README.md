# Third Eye
A solution which improves the surveillance of IP-Camera or CCTV camera placed in public domains by increasing its security features.

## Motivation For the Project
In Nugambakkam railway station at Chennai in India a women was murdered ( ***Swathi Case*** ) in broad day light using a wepon ( probably a knife or a Sickle ). The entire act was caught on a CCTV camera and later the culprit was caught using the footage, but now lets just imagine that the CCTV camera had a brain of it's own and it's able to classify that there is a dangerous object in the video and gives immediate notification to the station master with the footage in the case of railway station or any other security control unit and they are the ultimate decesion maker which decides if any action is to be taken according to the situation and also the number of CCTV camera will be increasing and it is not possible to keep track of all the cameras with man power but with this solution only those particular cameras footage can be sent to the control unit which holds a potenital weapon in the video. We will be sending the location of the crime to the cloud and also the wepon used, using this we can pin point all the regions where more frequent crimes are occuring and increase the security at those regions. 

### Pin pointing the location of the crime scene
  
  As the CCTV/IP cameras are fixed in a particular location, pinpointing the location of the crime scene is fairly simple.The crime video is being caught in the CCTV camera and the latitude and longitude of the camera is also the location of the crime scene. 
  
### Technolgy used to achieve this
  
1. OpenCV is used to capture the image.
2. CloudSight API which converts the Image to textual reprenstation.
3. Based on the keyword search for dangerous weapons we notify the station master through twillio sms api.
4. The location and the weapon used is uploaded to thingspeak database. 
5. Google map API is used to locate the crime scene. 
6. The project was built in Python.
