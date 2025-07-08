from twilio.rest import Client

def send_sms(account_sid, auth_token, from_number, to_number, message):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print("SMS sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    account_sid = ""  
    auth_token = ""   
    from_number = ""      
    to_number = ""        
    message = "This is an automated SMS sent using Python."
    send_sms(account_sid, auth_token, from_number, to_number, message)