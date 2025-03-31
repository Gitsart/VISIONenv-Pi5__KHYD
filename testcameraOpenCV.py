import cv2

# Initialize the camera (0 for default camera)
camera = cv2.VideoCapture(0)  # If you are using a USB camera, try changing 0 to 1 or higher.

if not camera.isOpened():
    print("Error: Camera not accessible")
    exit()

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Failed to grab frame")
        break

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
