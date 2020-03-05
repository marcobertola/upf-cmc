
from pythonosc.udp_client import SimpleUDPClient
import random

#function to send values to the pure data controller 
def sendValues(distance):
	'''
	Parameters:
	------------
		:distance: distance between words to send to the osc server (Pure Data)
	'''

	#setting netwrok address IP and port 
	ip = "127.0.0.1"
	port = 1337

	# Create client
	try:
		client = SimpleUDPClient(ip, port)  
	except Exception as e:
		print('Client could not be created \n {}'.format(e))
		return	

	# Send array message
	client.send_message("/list", distance)   

	return

def sendTriggerValue(trigger):
	ip = "127.0.0.1"
	port = 1337

	# Create client
	try:
		client = SimpleUDPClient(ip, port) 
	except Exception as e:
		print('Client could not be created \n {}'.format(e))
		return	

	
	client.send_message("/trigger", trigger)

	return
	

