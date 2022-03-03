import cv2 
import numpy as np 
from elements.yolo import OBJ_DETECTION 
from networktables import NetworkTables
import time

video1=cv2.VideoCapture(0)
video1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

video2=cv2.VideoCapture(1)
video2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

Object_classes = [ 'blue', 'red' ] 
Object_colors = list([[255,0,0],[0,0,255]]) 
Object_detector = OBJ_DETECTION('weights/best_2_25_v5v5.pt', Object_classes) 

"""
cap1 = cv2.VideoCapture(0)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#cap1.set(cv2.CAP_PROP_FPS, 30)

cap2 = cv2.VideoCapture(1)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#cap2.set(cv2.CAP_PROP_FPS, 30)
"""

NetworkTables.initialize(server="roborio-5057-frc.local")
sd = NetworkTables.getTable('SmartDashboard')
print("Is connected: " + str(NetworkTables.isConnected()))

while True:
    t1 = time.time()
    _, frame1 = video1.read() 
    _, frame2 = video2.read()

    frame = np.hstack((frame1,frame2))

    # detection process 
    objs = Object_detector.detect(frame) 

    """
    # plotting 
    for obj in objs: 
        # print(obj) 
        label = obj['label'] 
        score = obj['score'] 
        [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
        color = Object_colors[Object_classes.index(label)] 
        frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), color, 2) 
        frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA)
    """
    print(f"fps: {1/(time.time()-t1)}")
    
    keyCode = cv2.waitKey(10) & 0xFF
    if keyCode == 27 or keyCode == ord('q'):
        break

video1.release()
video2.release()
