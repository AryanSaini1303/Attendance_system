# takes input via tkinter frame(form)

# importing related libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import face_recognition
import numpy as np
import cv2
import csv
import os
from datetime import datetime
import glob
import time
from pathlib import Path
from playsound import playsound
import mysql.connector
import pandas as pd

data_1=[]
def submit_data(data_1):
    messagebox.showinfo('Status','Data saved')
    category=''
    session_type=''
    section=''
    subject=sub_entry.get()
    if session_entry.get()==1:
        session_type='LAB'
    elif session_entry.get()==2:
        session_type='THEORY'
    if section_entry.get()==1:
        section='A'
    elif section_entry.get()==2:
        section='C'
    elif section_entry.get()==3:
        section='BOTH'
    if category1.get()==1:
        category+='T1'
    if category2.get()==1:
        category+='T2'
    if category3.get()==1:
        category+='T3'
    if category4.get()==1:
        category+='T4'
    data=[]
    data.append(subject)
    data.append(session_type)
    data.append(section)
    data.append(category)
    for x in data:
       data_1.append(x)
window = Tk()
window.title('Lecture Information')
frame=Frame(window)
frame.pack()
main_frame=LabelFrame(frame,text='')
main_frame.grid(row=0,column=0,sticky='news',padx=20,pady=30)

#Subject Input
sub_lb=Label(main_frame,text='SUBJECT',font=('Cambria',17,'bold'))
sub_lb.grid(row=0,column=0,padx=20,pady=20)
sub_options=['CHE1003(Bio-sciences_Nanotechnology)',
             'CSE2022(Artificial Intelligence Techinques and Methods)',
             'CSE2101(Artificial Neural Network)',
             'CSE2102(Computer Network)',
             'CSE2103(Software Engineering and Project Management)',
             'CSE2718(Computer Architecture)']
sub_entry=ttk.Combobox(main_frame,values=sub_options,width=50,height=25)
sub_entry.grid(row=0,column=1,sticky='w',padx=20,pady=20)

#Session type input
session_lb=Label(main_frame,text='SESSION',font=('Cambria',17,'bold'))
session_lb.grid(row=1,column=0,padx=20,pady=20)
session_entry=IntVar()
session_op1=Radiobutton(main_frame,text='LAB',variable=session_entry,value=1,font=('Courier',15))
session_op2=Radiobutton(main_frame,text='THEORY',variable=session_entry,value=2,font=('Courier',15))
session_op1.grid(row=1,column=1,sticky='w',padx=10)
session_op2.grid(row=1,column=1,padx=10)

#Section Input
section_lb=Label(main_frame,text='SECTION',font=('Cambria',17,'bold'))
section_lb.grid(row=2,column=0,padx=20,pady=20)
section_entry=IntVar()
section_op1=Radiobutton(main_frame,text='A',variable=section_entry,value=1,font=('Courier',15))
section_op2=Radiobutton(main_frame,text='C',variable=section_entry,value=2,font=('Courier',15))
section_op3=Radiobutton(main_frame,text='BOTH',variable=section_entry,value=3,font=('Courier',15))
section_op1.grid(row=2,column=1,sticky='w',padx=10)
section_op2.grid(row=2,column=1,padx=10)
section_op3.grid(row=2,column=1,sticky='e',padx=10)

#Category Input
category_lb=Label(main_frame,text='CATEGORY',font=('Cambria',17,'bold'))
category_lb.grid(row=3,column=0,padx=20,pady=20)
category1 = IntVar()  
category2 = IntVar()  
category3 = IntVar()
category4 = IntVar()
c1 = Checkbutton(main_frame, text = "T1", 
                      variable = category1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
c2 = Checkbutton(main_frame, text = "T2",
                      variable = category2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
c3 = Checkbutton(main_frame, text = "T3",
                      variable = category3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
c4 = Checkbutton(main_frame, text = "T4",
                      variable = category4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
c1.grid(row=3,column=1,padx=10,sticky='w')
c2.grid(row=3,column=1,padx=10)
c3.grid(row=4,column=1,padx=10,sticky='w')
c4.grid(row=4,column=1,padx=10)

#Submit button
data_1=[]
main_frame2=LabelFrame(frame,text='')
main_frame2.grid(row=5,column=0,padx=20,pady=5)
submit=Button(main_frame2,text='Submit',width=15,height=2,bg='blue',activebackground='green',command=lambda:submit_data(data_1))
submit.grid(row=5,column=0)
window.mainloop()

    
# Establising database connection
sql=mysql.connector.connect(host="localhost",user="aryan",password="root")
cursor=sql.cursor()
query="use attendance_database"
cursor.execute(query)

subject=data_1[0]    
session_type=data_1[1]
section=data_1[2]
category=data_1[3]
subject_code,subject_name=subject.split("(")

# Providing file path of the images
filePathAT1='C:/NEW FOLDER/Projects/Attendance_system/new_database/Student_Images/Section A/T 1'
filePathAT2='C:/NEW FOLDER/Projects/Attendance_system/new_database/Student_Images/Section A/T 2'
filePathCT3='C:/NEW FOLDER/Projects/Attendance_system/new_database/Student_Images/Section C/T 3'
filePathCT4='C:/NEW FOLDER/Projects/Attendance_system/new_database/Student_Images/Section C/T 4'

# Creating variables for importing and encoding the required images
directory=[]
images=[]
known_encoding=[]
all_enrollment_numbers=[]
n=0

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

# Current_date = now.strftime("%d-%m-%Y")
current_date="28-03-2023"
if session_type=="THEORY":
    record_path="C:/NEW FOLDER/Projects/Attendance_system/new_database/attendance_record/"+subject_code+"/"+session_type+"/"+section+".csv"
elif session_type=="LAB":
    record_path="C:/NEW FOLDER/Projects/Attendance_system/new_database/attendance_record/"+subject_code+"/"+session_type+"/"+category+".csv"
df=pd.read_csv(record_path)
total_columns=len(df.axes[1])
df = pd.read_csv(record_path)
df[current_date]="A"
df.to_csv(record_path,index=False)
df = pd.read_csv(record_path)

# Creating variables for face recognition
face_locations = []
face_encodings = []
s=True
marked=[]
start_time=time.time()

# Initialising face recognition
cap = cv2.VideoCapture(0)
while True:
    if (time.time()-start_time)>1200:
        print("Times up!, no attendance will be marked now")
        exit(0)# Closes the program after 20 minutes
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
                    fontScale= 1# Setting attributes for the text
                    fontColor= (0,255,0)
                    thickness= 3
                    lineType = 2
                    cv2.putText(frame,'Marked',
                        org, 
                        font, 
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)# Writing text on opencv window
                    playsound('C://NEW FOLDER//Projects//Attendance_system//message-incoming-132126.mp3')
                    current_time = now.strftime("%H:%M:%S")# Set current time
                    print(enrol_num,"is marked present")
                    print("Entry time:",current_time)
                    if session_type=="LAB":
                        query="Select enrollment, name, entry_time from students where category='"+category+"'"
                    elif session_type=="THEORY":
                        if section=="BOTH":
                            query="select enrollment, name, entry_time from students"
                        elif section=="A" or section=="C":
                            query="Select enrollment, name, entry_time from students where section='"+section+"'"
                    cursor.execute(query)
                    result=cursor.fetchall()
                    a=0
                    for i in result:
                        if i[0]==enrol_num: 
                            df.loc[a, current_date] = "P"
                            df.to_csv(record_path, index=False)
                        a+=1
                marked.append(enrol_num)                           
    # Naming the OpenCV window                             
    cv2.imshow("Attendence system",frame)
    if cv2.waitKey(1) == ord('c'):# Window closes when "c" is pressed
        break
cap.release()
cv2.destroyAllWindows()