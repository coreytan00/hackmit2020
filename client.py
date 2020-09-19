from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears.helper import reducer
import cv2

options = {'bidirectional_mode': True}

#define netgear client w/ default settings
stream = VideoGear(source='yuh.mp4').start() #Open any video stream
client = NetGear(receive_mode = True, pattern = 1, logging = True, **options)

# infinite loop
while True:
    frame = stream.read()
    print("frame read")

    # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break

    frame = reducer(frame, percentage = 40)
    # do something with frame here

    data = client.recv(return_data = frame)
    if data is None:
        break

    server_data, frame = data
    if frame is None:
        break

    if server_data:
        print(server_data)
    # Show output window
    cv2.imshow("Client Window", frame) 
    #show output for client too

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break


# close output window
#cv2.destroyAllWindows()
# safely close video stream
stream.stop()
# safely close client
client.close()


#NOTES
#right now client is receiving video data from server. i want other way around.
#however i want server to play music. also support multiple clients.


#url submit - to server - update all clients
#ready check (wait till everyone ready) (also unready) - 3 2 1 server play send to all clients
#check latency for each client?
#send all data back to server
#total encapsulating recordding for all input streams - the live virtual recording
#videos all sidebyside up and down.

#clienet server - have message types and perform actions accordingly, structure it like
# my 53 final project.