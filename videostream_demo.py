# USAGE
# python videostream_demo.py
# python videostream_demo.py --picamera 1

# import the necessary packages
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
# cv2.
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
	"-p",
	"--picamera",
	type=int,
	default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument(
	"-c",
	"--camera",
	type=int,
	default=1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
cap = cv2.VideoCapture(args["camera"])
# initialize the video stream and allow the cammera sensor to warmup
# vs = VideoStream(usePiCamera=args["picamera"] > 0, src=args["camera"]).start()
# cap 
time.sleep(2.0)
i = 0
# loop over the frames from the video stream
img_size = [200, 360]
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	ret, frame = cap.read()
	frame = cv2.resize(frame, (img_size[1], img_size[0]))
	key = cv2.waitKey(1)
	cv2.imshow("fr", frame)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	elif key == ord("i"):
		cv2.imwrite('l2' + str(i) + '.png', frame)
		i += 1

# do a bit of cleanup
cv2.destroyAllWindows()
# vs.stop()
