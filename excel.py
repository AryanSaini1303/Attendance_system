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
sql=mysql.connector.connect(host="localhost",user="aryan",password="root")
cursor=sql.cursor()
query="use attendance_database"
cursor.execute(query)
query="select enrollment,name from students where section='C' "
cursor.execute(query)
result=cursor.fetchall
for i in result:
   