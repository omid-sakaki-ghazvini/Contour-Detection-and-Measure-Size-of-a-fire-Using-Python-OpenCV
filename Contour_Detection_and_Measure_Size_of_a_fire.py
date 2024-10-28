# importing libraries
import cv2

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('test.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
    
# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # resize the image
        image = cv2.resize(frame, (350, 350))

        # convert to grayscale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # apply binary threshold
        # adjust threshold from 50 to 150 to get good results for the corresponding image
        ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)

        # detect contours on binary image
        contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # draw contours on original image
        img_copy = image.copy()
        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)

        # Loop through the contours and calculate the area of each object 
        for cnt in contours:
                area = cv2.contourArea(cnt)
                if area>=2000:
  
                    # object and display the area on the image 
                    x, y, w, h = cv2.boundingRect(cnt) 
    
                    cv2.putText(img_copy, str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 

        # display the image
        cv2.imshow('fire', img_copy)
        
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()