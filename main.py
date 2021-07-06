import os, requests

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from modules.jira import JiraInstance

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
jira = JiraInstance()

# @app.command("/demo")
# def hello_command(ack, say, body):
#     ack(f"Hey team!")

@app.command("/standup")
def standup_updates(ack, say, client, body):
    ack()
    user_name = body["user_name"]
    user_id = body["user_id"]
    if body["text"]:
        user_name = body["text"]
    tickets = jira.getStandupUpdates(user_name)
    update_msg = "Updates:\n"
    for ticket in tickets:
        update_msg += "\t• " + ticket + "\n"
    channel_id = body["channel_id"]
    user_profile = client.users_profile_get(user=user_id)
    prof_pic_url = user_profile["profile"]["image_512"]
    client.chat_postMessage(
        channel=channel_id,
        username=user_name,
        icon_url=prof_pic_url,
        text = update_msg
    )

@app.command("/retro")
def open_tickets(ack, say, client, body):
    ack()
    user_name = body["user_name"]
    user_id = body["user_id"]
    if body["text"]:
        user_name = body["text"]
    tickets = jira.getOpenTickets(user_name)
    update_msg = "Updates:\n"
    for ticket in tickets:
        update_msg += "\t• " + ticket + "\n"
    channel_id = body["channel_id"]
    user_profile = client.users_profile_get(user=user_id)
    prof_pic_url = user_profile["profile"]["image_512"]
    client.chat_postMessage(
        channel=channel_id,
        username=user_name,
        icon_url=prof_pic_url,
        text = update_msg
    )

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
