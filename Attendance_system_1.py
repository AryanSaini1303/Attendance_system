#takes images from a folder, separates name and enrollment number from the images 
#makes the excel sheet with name, enrollment number and entry time of present students only

import face_recognition
import numpy as np
import cv2
import csv
import os
from datetime import datetime
import glob
from pathlib import Path
from playsound import playsound
import re

file_name=input("Enter the lecture name, use \"_\" to separate words\n")
file_name+='_'
video_capture = cv2.VideoCapture(0)
filePath='C:/NEW FOLDER/artificial intelligence/attendance system/database'
directory=[]
images=[]
known_encoding=[]
known_names=[]
enrollment_number=[]
n=0

for filename in glob.iglob(f'{filePath}/*'):
    directory.append(filename.replace("database\\","database/"))
    images.append(face_recognition.load_image_file(directory[n]))# to load all the images 
    known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
    known_names.append(Path(directory[n]).stem)# to extract name of file from the path
    enrollment_number_separated=[float(s) for s in re.findall(r'-?\d+\.?\d*', known_names[n])]# extracting enrollment number from name digit by digit
    enrollment_number.append(' '.join([str(elem) for elem in enrollment_number_separated]))# appending all the digits of an enrollment number
    n+=1
print(directory)
students = known_names.copy()
face_locations = []
face_encodings = []
face_names = []
s=True
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")# set current date
file_name+=current_date
f = open(file_name+'.csv','w+',newline = '')# to open a csv file
lnwriter = csv.writer(f)
lnwriter.writerow(["Name","Enrollment_Number","Entry_Time"])

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_names[best_match_index]
                face_names.append(name)
            if name in known_names:
                now = datetime.now()
                font = cv2.FONT_HERSHEY_SIMPLEX
                org=(50,50)
                fontScale              = 1
                fontColor              = (0,255,0)
                thickness              = 3
                lineType               = 2# setting attributes for the text
                cv2.putText(frame,'Marked',
                    org, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)# writing text on opencv window
                playsound('C:/NEW FOLDER/artificial intelligence/attendance system/message-incoming-132126.mp3')
                if name in students:
                    # students.remove(name)
                    # print("Students left for attendance are:",students)
                    num=0
                    for x in enrollment_number:#checks for the enrollment number of the present student
                        if x in name:
                            num=x
                            break
                    finalName = ''.join([i for i in name if not i.isdigit()])#removing numbers from name
                    NAME=finalName.replace(".","")# removing dot(.) from name
                    current_time = now.strftime("%H:%M:%S")# set current time
                    print(NAME,"is marked present")
                    print("Entry time:",current_time)
                    lnwriter.writerow([NAME,num,current_time])# writes in cvs file
    cv2.imshow("Attendence system",frame)# naming the opencv window
    if cv2.waitKey(1) == ord('c'):# window closes when "c" is pressed
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()