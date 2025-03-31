import cv2
import subprocess
import numpy as np

# Start libcamera-vid as a subprocess
command = [
    "libcamera-vid",
    "--inline",
    "-t", "0",  # Infinite run time
    "--width", "640",
    "--height", "480",
    "--framerate", "30",
    "--codec", "yuv420",
    "--output", "-",
]
process = subprocess.Popen(command, stdout=subprocess.PIPE)

# OpenCV to read frames from subprocess
while True:
    frame_size = 640 * 480 * 3 // 2  # YUV420 size
    frame = process.stdout.read(frame_size)
    if not frame:
        break

    # Convert to OpenCV BGR format
    yuv = np.frombuffer(frame, dtype=np.uint8).reshape((480 + 480 // 2, 640))
    bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

    # Display frame
    cv2.imshow("Camera Feed", bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

process.terminate()
cv2.destroyAllWindows()
