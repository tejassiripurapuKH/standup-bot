# Standup/Infrabot

Slack bot for posting standup and retro updates to channel. Currently

## Usage

- `/standup [Full name as it appears in Jira]`: Posts standup updates which includes tickets that are In Progress or Blocked, and tickets which were moved to Code Review or Done in the past day.
- `/retro [Full name as it appears in Jira]`: Posts retro updates which includes tickets that are not Done and in the current sprint.

## Development

Create new commands by adding on to `main.py` refer to other commands for syntax/structure. You will also need to add the Slash Command in the [Slack API](https://api.slack.com/apps/A0244KM6WG7) as well. Use `test-workspace` for testing/development, ask Tejas for access.

Need to set following environment variables:
- `JIRA_API_TOKEN`: Jira API token, find in Jira developer settings
- `SLACK_BOT_TOKEN`: Slack Bot or User token for your Slack App
- `SLACK_APP_TOKEN`: (only required if using Socket Mode) Slack App token generated when Socket Mode is enabled

## Deployment

`bash build_and_push.sh {tag}`: automated deployment script which creates docker image, tags with `latest` and `{tag}`, pushes to DockerHub, then restarts k8s deployment to pick up latest image. Deployed in namespace `tejas` on `dev-eks1`.
