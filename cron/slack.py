import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from dotenv import load_dotenv
load_dotenv()

slack_token = os.environ.get('SLACK_TOKEN')
slack_client = WebClient(token=slack_token)
slack_channel = 'test'
results = {"key": "value"}  # Replace with your actual results

def post_message_to_slack(results, slack_channel):
    try:
        # Post the message to the Slack channel
        response = slack_client.chat_postMessage(
            channel=slack_channel,
            text=json.dumps(results, indent=2)
        )
        # Print the response
        print(response)
    except SlackApiError as e:
        # Print the error
        print(f"Error posting message: {e.response['error']}")
