from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACa92624250d881722233fe9bbd4e53d86"
auth_token  = "80e8a7bdd20cbc681fc7438006372565"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Welcome to Mecenato!",
    to="+971567448969",    # Replace with your phone number
    from_="+353768886969") # Replace with your Twilio number
print message.sid