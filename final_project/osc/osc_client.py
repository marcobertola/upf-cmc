
from pythonosc.udp_client import SimpleUDPClient
import random

#function to send values to the pure data controller 
def sendValues():

	max_value = 10

	#setting netwrok address IP and port 
	ip = "127.0.0.1"
	port = 1337

	# Create client
	try:
		client = SimpleUDPClient(ip, port)  
	except Exception as e:
		print('Client could not be created \n {}'.format(e))
		return	

	# array initialization	
	values = []

	#filling array with random values
	for i in range(max_value):
		values.append(random.randrange(127))
	print('Values that will be sent: {}\n'.format(values))

	# Send array message
	client.send_message("/values", values)   
	

	return