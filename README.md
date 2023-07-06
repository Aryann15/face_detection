# face_detection
performed using classifiers (an algorithm that decides whether a given algorithm is positive, or negative whether a face is present or not). here I am using open cv's already trained classifiers (HAAR CASCADES). I have their frontalface XML file. this is the result i get, <img width="956" alt="image" src="https://github.com/Aryann15/face_detection/assets/82017158/d82e571f-a694-4043-973c-c14c6bf2b9bf">

there are some errors in detecting the faces as haar cascades are really sensitive to noise in an image. we can try to minimize the noise sensitivity by modifying the scale factor in minimum neighbours
