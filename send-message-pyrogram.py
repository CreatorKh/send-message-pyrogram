# A script to use pyrogram module to send messages to telegram users periodically using pyrogram
# The PyPi schedule module can be used to achieve this or the inbuilt time module
import schedule
import time
from pyrogram import Client
# For environment variables
from os import environ
from dotenv import load_dotenv
load_dotenv()

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_STRING"]

app = Client(session_string, api_id, api_hash)


with app:
    n = 0
    while n < 1000:
        app.send_message(958190331,"sori eto bila proverka")
        app.send_message(613720723, "sori eto bila proverka")
        print("balyyya")
        time.sleep(0)
        n += 1
