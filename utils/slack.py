def sendSlackMessage(updates):
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        update_msg = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Updates:"
                }
            }
        ]
        for update in updates:
            update_msg.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*•* " + update
                }
            })

        response = client.chat_postMessage(
            channel="U024RHH9QLC",
            blocks = update_msg
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]
