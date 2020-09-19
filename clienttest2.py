from vidgear.gears import NetGear
import cv2

# activate Multi-Clients mode
options = {'multiclient_mode': True} 

addr = "192.168.7.89"
port = '5577'
proto = 'tcp' #tcp or ipc
pattern = 2 #0, 1, or 2

# Define NetGear Client at Server's IP address and assign a unique port address and other parameters 
client = NetGear(address = addr , port = port , protocol = proto,  pattern = pattern, receive_mode = True, logging = True, **options)  # !!! change following IP address '192.168.x.xxx' with yours !!!

# loop over
while True:
    # receive data from server
    frame = client.recv()

    # check for frame if None
    if frame is None:
        break

    # {do something with frame here}

    # Show output window
    cv2.imshow("Client 5577 Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()