from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears.helper import reducer
import numpy as np
import cv2

options = {'bidirectional_mode': True}

#Define netgear server w/ receive
stream = VideoGear(source='yuh.mp4').start()
server = NetGear(pattern=1, logging=True, **options) 

# infinite loop until [Ctrl+C] is pressed
while True:
    try: 
        # receive frames from network
        frame = stream.read()
       	
        if frame is None:
            break
        print("frame read")
        
        frame = reducer(frame, percentage = 40)
        # do something with frame here
        target_data = "hi this is server"

        recv_data = server.send(frame, message = target_data)

        if not(recv_data is None) and isinstance(recv_data, np.ndarray):
        	cv2.imshow("Server Window", recv_data)
        	key = cv2.waitkey(1) & 0xFF
        else:
        	print('uhoh')

    except KeyboardInterrupt:
        break

stream.stop()

# safely close server
server.close()


def server_init():
	"""
       	package = []
        audio_data = "here"
        other_data = "here2"
        package.append(audio_data)
        package.append(other_data)
	"""
	pass
	 