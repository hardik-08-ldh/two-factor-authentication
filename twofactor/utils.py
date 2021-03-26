import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
1
2
client = Client(account_sid, auth_token)

def sendSMS(user_code, phone_number):
    message = client.messages \
                    .create(
                        3
                    )

    print(message.sid)