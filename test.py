from dataTypes import *
import socket
import client
from noiseEncryption import *


my_client = client.Client("127.0.0.1")
my_client.SetupConnection()

"""client =  Noise()

client.connectToNoise("localhost",6222)

client.sendNoiseFrame(b"test")

data=client.receiveNoiseFrame()

print(data)"""

#print(BOOL(True))

"""print(U8(22))

print(STR0_255("thiaago"))


host = socket.gethostname()
print(host)

client = Client("127.0.0.1")

client.SetupMiningConnection()"""




