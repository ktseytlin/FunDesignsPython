from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd98dd76dc1047dfbda25e279b92b7004"
auth_token  = "1499fa6ccdd87ed7a199b97d8b1bae49"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I am about to leave the house. Sent you text via Python!",
    to="+12406034653",    # Replace with your phone number
    from_="+12402527851") # Replace with your Twilio number
print message.sid
