import cv2, base64

def capture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("CaputeImage")
    while True:
        captured, frame = cam.read()
        cv2.imshow("CaputeImage", frame)
        if not captured:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            #print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            height,width,layers = frame.shape
            height = height//2
            width = width//2
            resize = cv2.resize(frame, (width, height))
            img_name = "capturedImage.png"
            cv2.imwrite(img_name, resize)
            #self.frame = " ".join(str(x) for x in frame) # save to db...  self.frame
            #print("{} written!".format(img_name))

            file = open(img_name, 'rb')
            file_content = file.read()    
            base64_code = base64.b64encode(file_content)
            cam.release()
            cv2.destroyAllWindows()
            return base64_code
        
