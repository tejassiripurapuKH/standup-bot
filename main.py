import os, requests

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from modules.jira import JiraInstance

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
jira = JiraInstance()

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.command("/standup")
def standup_updates(ack, say, body):
    ack()
    if body["text"]:
        tickets = jira.getStandupUpdates(body["text"])
    else:
        tickets = jira.getStandupUpdates(body["user_name"])
    update_msg = "Updates:\n"
    for ticket in tickets:
        update_msg += "\t• " + ticket + "\n"
    say(update_msg)

@app.command("/retro")
def open_tickets(ack, say, body):
    ack()
    if body["text"]:
        tickets = jira.getOpenTickets(body["text"])
    else:
        tickets = jira.getOpenTickets(body["user_name"])
    update_msg = "Open tickets:\n"
    for ticket in tickets:
        update_msg += "\t• " + ticket + "\n"
    say(update_msg)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
