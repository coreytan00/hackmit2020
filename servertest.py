from vidgear.gears import NetGear
from vidgear.gears import VideoGear
from vidgear.gears import CamGear
import socket
import cv2

# Open suitable video stream (webcam on first index in our case) 
stream = VideoGear(source=0).start() 
#stream = CamGear(source='https://www.youtube.com/watch?v=orXAg5dIMa8&ab_channel=TaylorSwiftVEVO', y_tube=True, logging=True).start() 

# activate multiclient_mode mode
options = {'multiclient_mode': True} 

addr = "192.168.7.89"
port = [5567,5577]
proto = 'tcp' # tcp or ipc
pattern = 2 #0, 1, or 2

# Define NetGear Client at given IP address and assign list/tuple of all unique Server((5577,5578) in our case) and other parameters 
server = NetGear(address = addr, port = port, protocol = proto,  pattern = pattern, logging = True, **options) # !!! change following IP address '192.168.x.xxx' with yours !!!

# Define received data dictionary
data_dict = {}

# loop over until KeyBoard Interrupted
while True:

  try: 

    # read frames from stream
    frame = stream.read()

    # check for frame if not None-type
    if frame is None:
      print('no frame')
      break
    #print("frame read")

    # {do something with the frame here}


    # send frame and also receive data from Client(s)
    server.send(frame)

    """
    # check if valid data recieved
    if not(recv_data is None):
      # extract unique port address and its respective data
      unique_address, data = recv_data
      # update the extracted data in the data dictionary
      data_dict[unique_address] = data

    
    if data_dict:
      #print data just received from Client(s)
      for key, value in data_dict.items():
          print("Client at port {} said: {}".format(key,value))
    """

  except KeyboardInterrupt:
    break

# safely close video stream
stream.stop()
# safely close server
server.close()