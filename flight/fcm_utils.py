import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def send_notification(token, message):
    """
    Send a notification to the given device token with the provided message.
    """
    message = messaging.Message(
        notification=messaging.Notification(
            title='Flight Status Update',
            body=message,
        ),
        token=token,
    )
    response = messaging.send(message)
    return response
