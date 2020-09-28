from twilio.rest import Client
account_sid = 'AC5ec5e6dd974f0da1b700de7425e23d66'
auth_token = '2c68c1f2a5f10ad9c4afe8688bc15814'
client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body='Brian tragasable',
	         from_='+13345641977',
	         to='+17862866129'
	     )


	

