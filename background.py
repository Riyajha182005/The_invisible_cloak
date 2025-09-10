import cv2 ## oprncv  for image processing 
## creating a videocapture object
cap=cv2.VideoCapture(0) ## this my webcam 

## Getting the background image 
while cap.isOpened():
   ret,background=cap.read() ## simply reading from the webcam
   if ret:
      cv2.imshow("image",background)
      if cv2.waitKey(5)==ord('q'):
         ## save the background image 
         cv2.imwrite("image.jpeg",background)
         break
      
cap.realese()
cv2.destroyAllWindows()