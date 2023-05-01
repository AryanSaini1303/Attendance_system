#Imports images from specific folders compares the face and makes new excel sheet everyday of all the students

#Importing related libraries
import face_recognition
import numpy as np
import cv2
import csv
import os
from datetime import datetime
import glob
from pathlib import Path
from playsound import playsound
import mysql.connector

directory=[]
images=[]
known_encoding=[]
all_enrollment_numbers=[]
n=0
    
#Establising database connection
sql=mysql.connector.connect(host="localhost",user="aryan",password="root")
cursor=sql.cursor()
query="use attendance_database"
cursor.execute(query)

#Taking input of the lecture
section=""
category=""
subject=input("Enter the lecture name, use \"_\" to separate words\n")
section=input("Enter the section: A, C, BOTH\n").upper()
session_type=input("Enter the class type: lab or theory\n").upper()
if session_type=="LAB":
    if section=="A":
        category=input("Enter the group: T1, T2\n").upper()
    elif section=="C":
        category=input("Enter the group: T3, T4\n").upper()
elif session_type=="THEORY":
    if section=="A":
        category=""
        category="T1,T2"
    elif section=="C":
        category=""
        category="T3,T4"  
else:
    print("Wrong input.")
    exit(0)
    
# Providing file path of the images
filePathAT1='C:/NEW FOLDER/artificial intelligence/attendance system/new_database/Student_Images/Section A/T 1'
filePathAT2='C:/NEW FOLDER/artificial intelligence/attendance system/new_database/Student_Images/Section A/T 2'
filePathCT3='C:/NEW FOLDER/artificial intelligence/attendance system/new_database/Student_Images/Section C/T 3'
filePathCT4='C:/NEW FOLDER/artificial intelligence/attendance system/new_database/Student_Images/Section C/T 4'

if session_type=="LAB":
    if section=="A":
        if category=="T1":
            for filename in glob.iglob(f'{filePathAT1}/*'):
                directory.append(filename.replace("T 1\\","T 1/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))
                known_encoding.append(face_recognition.face_encodings(images[n])[0])
                n+=1
        elif category=="T2":
            for filename in glob.iglob(f'{filePathAT2}/*'):
                directory.append(filename.replace("T 2\\","T 2/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))
                known_encoding.append(face_recognition.face_encodings(images[n])[0])
                n+=1
    elif section=="C":
        if category=="T3":
            for filename in glob.iglob(f'{filePathCT3}/*'):
                directory.append(filename.replace("T 3\\","T 3/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))
                known_encoding.append(face_recognition.face_encodings(images[n])[0])
                n+=1
        elif category=="T4":
            for filename in glob.iglob(f'{filePathCT4}/*'):
                directory.append(filename.replace("T 4\\","T 4/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))
                known_encoding.append(face_recognition.face_encodings(images[n])[0])
                n+=1
elif session_type=="THEORY":
    if section=="A":
        for filename in glob.iglob(f'{filePathAT1}/*'):
            directory.append(filename.replace("T 1\\","T 1/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1  
        for filename in glob.iglob(f'{filePathAT2}/*'):
            directory.append(filename.replace("T 2\\","T 2/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1      
    elif section=="C":
        for filename in glob.iglob(f'{filePathCT3}/*'):
            directory.append(filename.replace("T 3\\","T 3/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1
        for filename in glob.iglob(f'{filePathCT4}/*'):
            directory.append(filename.replace("T 4\\","T 4/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1
    elif section=="BOTH":
        for filename in glob.iglob(f'{filePathAT1}/*'):
            directory.append(filename.replace("T 1\\","T 1/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1
        for filename in glob.iglob(f'{filePathAT2}/*'):
            directory.append(filename.replace("T 2\\","T 2/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1
        for filename in glob.iglob(f'{filePathCT3}/*'):
            directory.append(filename.replace("T 3\\","T 3/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1
        for filename in glob.iglob(f'{filePathCT4}/*'):
            directory.append(filename.replace("T 4\\","T 4/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))
            known_encoding.append(face_recognition.face_encodings(images[n])[0])
            n+=1

# Creating csv file     
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")
file_name=subject+'_'+section+'_'+category+"_"+current_date+'.csv'
f = open(file_name,'a',newline = '')
lnwriter = csv.writer(f)
lnwriter.writerow(["Enrollment_Number","Name","Entry Time"])

# Creating variables for face recognition
face_locations = []
face_encodings = []
s=True
marked=[]

# Initialising face recognition
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encoding,face_encoding)
            enrol_num=""
            face_distance = face_recognition.face_distance(known_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                enrol_num = all_enrollment_numbers[best_match_index]
            if enrol_num in all_enrollment_numbers:
                if enrol_num in marked:
                    continue
                else:
                    now = datetime.now()
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    org=(50,50)
                    fontScale= 1# setting attributes for the text
                    fontColor= (0,255,0)
                    thickness= 3
                    lineType = 2
                    cv2.putText(frame,'Marked',
                        org, 
                        font, 
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)# writing text on opencv window
                    playsound('C://NEW FOLDER//artificial intelligence//attendance system//message-incoming-132126.mp3')
                    current_time = now.strftime("%H:%M:%S")# set current time
                    print(enrol_num,"is marked present")
                    print("Entry time:",current_time)
                    query= "update students set entry_time="+"'"+current_time+"'"+" where enrollment="+"'"+enrol_num+"'"
                    cursor.execute(query)
                    sql.commit()
                marked.append(enrol_num)
                            
    # Naming the openCV window                             
    cv2.imshow("Attendence system",frame)
    if cv2.waitKey(1) == ord('c'):# window closes when "c" is pressed
        break
    
#Fetching student data
if session_type=="LAB":
    query="Select enrollment, name, entry_time from students where category='"+category+"'"
elif session_type=="THEORY":
    if section=="BOTH":
        query="select enrollment, name, entry_time from students"
    elif section=="A" or section=="C":
        query="Select enrollment, name, entry_time from students where section='"+section+"'"
cursor.execute(query)
result=cursor.fetchall()
for i in result:
    lnwriter.writerow([i[0],i[1],i[2]])
query= "update students set entry_time='none' where section='C' OR section='A'"
cursor.execute(query)
sql.commit()
cap.release()
cv2.destroyAllWindows()
f.close()