import requests
import json
import time
import paho.mqtt.publish as publish
##settings part
ready = True
delay = 60 	  #60 seconds by default
streamer = "" #paste here your streamer's name
ID = ""		  #how to generate this id: https://docs.aws.amazon.com/lumberyard/latest/userguide/chatplay-generate-twitch-client-id.html

while ready:
	r = requests.get("https://api.twitch.tv/kraken/streams?client_id=" + ID + "&channel=" + streamer)
	data = r.json()
	streaming = data['_total']
	if data['_total'] == 1:
		print("broadcasting")
	else:
		print("not broadcasting")
	#uncomment and edit following line to mqtt publish
	#publish.single("topic/topic", payload="Streaming", hostname="adress", port=1883, auth={'username':"login",'password':"pass"})
	
	time.sleep(delay);

