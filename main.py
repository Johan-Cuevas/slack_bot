import os
import datetime
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


myloaded_env = load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

@app.message("Tell me the tiem")
def message_time(message, say):
    say(f"The date is f{datetime.date.today()} ")


# Sends a message at scheduled time
def scheduled_message():
    # Unix Epoch time
    client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
    list_of_time_to_post = [1609360668, 1609360678]
    for time in list_of_time_to_post:
        try:
            time_to_post = time
            channel_id = os.environ.get("CHANNEL_ID")
            client.chat_scheduleMessage(
                channel=channel_id,
                post_at=time_to_post,
                text="Hello this is a scheduled message"
            )
        except SlackApiError:
            print("Some error occured")

# Start your app
if __name__ == "__main__":
    scheduled_message()
    app.start(port=int(os.environ.get("PORT", 3000)))