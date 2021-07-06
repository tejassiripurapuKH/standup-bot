# -*- coding: utf-8 -*-

from jira import JIRA
from datetime import datetime, date, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

class JiraInstance:

    jira = None

    def __init__(self):
        self.jira = JIRA(server="https://komodohealth.atlassian.net", basic_auth=("tejas.siripurapu@komodohealth.com", os.environ["JIRA_API_TOKEN"]))

    def getStandupUpdates(self, username):
        infra_issues = self.jira.search_issues(f'project="IN" and assignee = "{username}"')
        infra_issues += self.jira.search_issues(f'project=DINF and assignee = "{username}"')
        ret = []
        for issue in infra_issues:
            last_updated = datetime.strptime(issue.fields.updated.split('T')[0], '%Y-%m-%d').date()
            today = date.today()
            if today.strftime("%A") == "Monday":
                yesterday = today - timedelta(days = 3)
            else:
                yesterday = today - timedelta(days = 1)
            status = str(issue.fields.status)
            if (status in ["In Progress", "Blocked"]) or ((status in ["Done", "Code Review"]) and (last_updated == today or last_updated == yesterday)):
                ret.append(issue.key + ': ' + status + " - " + issue.fields.summary)
        return ret

    def getOpenTickets(self, username):
        open_issues = self.jira.search_issues(f'(project="IN" or project=DINF) and (Sprint in openSprints() \
            and Sprint not in futureSprints()) and (assignee = "{username}") and (status != Done and status != Closed)')
        ret = []
        for issue in open_issues:
            ret.append(issue.key + ': ' + str(issue.fields.status) + " - " + issue.fields.summary)
        return ret
