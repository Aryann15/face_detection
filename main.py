import cv2 as cv

img = cv.imread('Photos/group2.jpeg')
cv.imshow('original photo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=2)
print(f'There are {len(faces_rect)} faces')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness= 2)

cv.imshow('Detected faces',img)

cv.waitKey(0)