import cv2
import time

video = cv2.VideoCapture(0)
# Add some sleep for the camera to initialize
time.sleep(2)
first_frame = None
while True:
    # Start reading from the camera
    check, frame = video.read()
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur the frame
    gray_frame_blur = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_blur

    # Find difference between the first frame and other frames
    delta_frame = cv2.absdiff(first_frame, gray_frame_blur)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Add rectangle on the moving objects
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 2000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("My Video", frame)

    # Request for a key press to quit video read
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
