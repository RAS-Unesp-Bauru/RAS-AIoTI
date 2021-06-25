import numpy as np
import datetime
import cv2
import paho.mqtt.client as mqtt

#MQTT Connection to Broker
clientMQTT = mqtt.Client()
clientMQTT.connect("177.94.189.10", 9095)

# Video Capture 
capture = cv2.VideoCapture(0)

# History, Threshold, DetectShadows 
# fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, True)
fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)

# Keeps track of what frame we're on
frameCount = 0
s = "The impression has started!"
clientMQTT.publish("RAS/AIoTI/3d_printer/status", "Started")


#time variables
i=0 #indicates the time counting started
n=0 #indicates the time now
flag = 0 #flag that indicates the begining of the time verification

T = "Not over" #Variable T indicates the stage of the impression

print(s)

while(1):
	# Return Value and the current frame
    ret, frame = capture.read()

	#  Check if a current frame actually exist
    if not ret:
        break

    # frameCount += 1
	# Resize the frame
    resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

	# Get the foreground mask
    fgmask = fgbg.apply(resizedFrame)

	# Count all the non zero pixels within the mask
    count = np.count_nonzero(fgmask)


	# Determine how many pixels do you want to detect to be considered "movement"
	# if (frameCount > 1 and count > 500):
    if count <= 500: #The T variable looks for a time of no movement to detect if the impression is over
        
        if flag == 0:
            
            time = datetime.datetime.now()
        
            i = int(time.second) + int(time.minute) * 60
            
            flag = 1
        
        time = datetime.datetime.now()
        
        n = int(time.second) + int(time.minute) * 60
        
        if (n - i) >= 10:
            
            if (n - i) >= 20:
                s = "Over"
                clientMQTT.publish("RAS/AIoTI/3d_printer/status", "Over")
                print(s)
                break
            
            elif s != "Stopped":
                s = "Stopped"
                clientMQTT.publish("RAS/AIoTI/3d_printer/status", "Stopped")
                print(s)
        
    else:
    
        flag = 0   
        
        if s != "Moving":
            clientMQTT.publish("RAS/AIoTI/3d_printer/status", "Moving")
            s = "Moving"
            print(s)
            
    cv2.imshow('Frame', resizedFrame)
    cv2.imshow('Mask', fgmask)
    
    k = cv2.waitKey(1) & 0xff
    
    if k == 27:
        break

clientMQTT.publish("RAS/AIoTI/3d_printer/status", "Over")

capture.release()
cv2.destroyAllWindows()