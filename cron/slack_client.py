import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from dotenv import load_dotenv
load_dotenv()

slack_token = os.environ.get('SLACK_TOKEN')
if not slack_token:
    from aws_secrets import get_secret
    slack_token = get_secret("SLACK_TOKEN")
slack_client = WebClient(token=slack_token)
slack_channel = 'test'

def post_message_to_slack(results, slack_channel):
    try:
        response = slack_client.chat_postMessage(
            channel=slack_channel,
            text=json.dumps(results, indent=2)
        )
        print(response)
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
