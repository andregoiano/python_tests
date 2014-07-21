from mixpanel import Mixpanel
from twilio.rest import TwilioRestClient
import mixpanel
# import datetime

mp = Mixpanel(ae91c3869706778b25a08e6f504ab1bd)

# create or update a profile with First Name, Last Name,
# E-Mail Address, Phone Number, and Favorite Color
mp.people_set('johndoe', {
    '$first_name'    : 'John',
    '$last_name'     : 'Doe',
    '$email'         : 'john.doe@mylorealestate.com',
    '$phone'         : '5555555555',
    'Company'        : 'Mylo Real Estate',
    'RERA'           : '49231',
    'Subscription Plan' : 'Free'
})

mp.people_append('johndoe', {
    'Last Logged in' : 'Today'
})

# You can also include properties to describe
# the circumstances of the event
mp.track(johndoe, 'Subscription Plan', {
    'Old Plan': 'Free',
    'New Plan': 'Enterprise'
})

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACa92624250d881722233fe9bbd4e53d86"
auth_token  = "80e8a7bdd20cbc681fc7438006372565"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Welcome to Mecenato!",
    to="+971567448969",    # Replace with your phone number
    from_="+353768886969") # Replace with your Twilio number
print message.sid