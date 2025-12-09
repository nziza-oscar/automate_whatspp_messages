import pywhatkit as kit
import datetime
import time

def send_whatsapp_message(number, message, send_hour, send_minute):
    print(f"Scheduling message to {number} at {send_hour}:{send_minute}")

    # pywhatkit requires at least 1–2 minutes ahead
    kit.sendwhatmsg(number, message, send_hour, send_minute)
    print("Message sent!")

if __name__ == "__main__":
    # Example usage
    number = "+250785697993"  # Replace with real number
    message = "Hello! This is an automated reminder 😊"

    # Schedule 1 minute from now
    now = datetime.datetime.now()
    send_hour = now.hour
    send_minute = now.minute + 1

    # Handle wrap of minutes > 59
    if send_minute >= 60:
        send_minute -= 60
        send_hour = (send_hour + 1) % 24

    send_whatsapp_message(number, message, send_hour, send_minute)
