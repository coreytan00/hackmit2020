from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import cv2

stream = VideoGear(source=0).start()

#input audio stream path
input_audio = "input-audio.aac" 

#ready your parameters
output_params = { '-i': input_audio, '-acodec': 'copy'}


while True:
	frame = stream.read()
	# read frames

	# check if frame is None
	if frame is None:
		#if True break the infinite loop
		break
	
	# do something with frame here

	# write frame to writer
	writer.write(frame) 
	   
	# Show output window
	cv2.imshow("Output Frame", frame)

	key = cv2.waitKey(1) & 0xFF
	# check for 'q' key-press
	if key == ord("q"):
		#if 'q' key-pressed break out
		break

cv2.destroyAllWindows()
# close output window

stream.stop()
# safely close video stream
writer.close()
# safely close writer