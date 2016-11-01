import twitter
api = twitter.Api(consumer_key='Your consumer key here',
		  consumer_secret='Your consumer secret here',
		  access_token_key='Your token key here',
		  access_token_secret='Your token secret here')
print(api.VerifyCredentials())
import serial
import datetime
ser = serial.Serial('Your port here', 9600)
while True:
    msg = ser.readline().decode().strip()
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update = "{0}: {1}".format(dt, msg)
    print("Posting: {0}".format(update))
    api.PostUpdate(update, verify_status_length=False)
