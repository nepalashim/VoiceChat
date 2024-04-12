from videostream import AudioSender
from vidstream import AudioReceiver

import threading 
import socket

# ip = socket.gethostbyname(socket.gethostname())


receiver = AudioReceiver('100.69.102.186',9999)# we can still use the  ->>ip parameter instead of 100.69...  if to make more dyanmic 
receive_thread = threading.Thread(target= receiver.start_server)


sender= AudioSender('192.168.0.172',5555) # put the ipv4 adress of next communicator

sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()









