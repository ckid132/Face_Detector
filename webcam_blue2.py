import cv2
import Serial
import numpy as np
sp = serial.Serial
sp = serial.Serial('COM3', 9600, timeout = 1)
webcam = cv2.VideoCapture(0)

pos_x = pos_y = 90
_pos_x = _pos_y = 90

margin_x = 20
margin_y = 20


if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    if not status:
        break

    frame_flipped = cv2.flip(frame, 1)  # 좌우 반전

    hsv = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 100, 120])
    upper_blue = np.array([150, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame_flipped, frame_flipped, mask=mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = None
    largest_area = 0

    COLOR = (0, 255, 0)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > largest_area:
            largest_area = area
            largest_contour = cnt

    if largest_contour is not None:
        if largest_area > 500:
            x, y, width, height = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame_flipped, (x, y), (x + width, y + height), COLOR, 2)
            center_x = x + width // 2
            center_y = y + height // 2
            print("center : %s, %s)" %(center_x, center_y)
            
            if center_x < 320 - margin_x:
                print("pan left")
                if pos_x - 1 >=0
                    pos_x = pos_x - 1
                else:
                    pos_x = 0
                else:
                    pos_x =0
            elif center_x > 320 + margin_x:
                print("pan right")
                if pos_x + 1 <= 180:
                    pos_x = pos_x + 1
                else:
                    pos_x = 180
                    _pos_x = pos_x
            
            else:
                print("pan stop")
                
            if center_y < 240 - margin_y :
                print("tilt up")
            elif center_y < 240 + margin_y :
                print("tilt down")
            else :
                print("tilt stop")
            
            #-------------------------------------------------------------------------------------
            if center_x < 300:
                if center_y > 260:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan left and tilt down")
                elif center_y < 220:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan left and tilt up")
                else:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan left")
                    
            if center_x > 340:
                if center_y > 260:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan right and tilt down")
                elif center_y < 220:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan right and tilt up")
                else:
                    print("center: ( %s, %s )"%(center_x, center_y), "  pan right")
                    
            if center_x > 300 and center_x < 340:
                if center_y > 260:
                    print("center: ( %s, %s )"%(center_x, center_y), "  up")
                elif center_y < 220:
                    print("center: ( %s, %s )"%(center_x, center_y), "  tile down")
                else: 
                    print("center: ( %s, %s )"%(center_x, center_y), "  Stop")
            #---------------------------------------------------------------------------------------
        

    cv2.imshow("VideoFrame", frame_flipped)

    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

webcam.release()
cv2.destroyAllWindows()