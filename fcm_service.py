import firebase_admin
from firebase_admin import credentials, messaging
import os

if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "firebase_service_account.json"))
    firebase_admin.initialize_app(cred)


def send_data_to_topic(topic: str, data: dict):
    message = messaging.Message(
        topic=topic,
        data={str(k): "" if v is None else str(v) for k, v in data.items()},
        android=messaging.AndroidConfig(
            priority="high"
        )
    )

    response = messaging.send(message)
    print(f"✅ FCM sent successfully: {response}")
    return response