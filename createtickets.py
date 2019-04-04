import os

import yaml
import requests
from dotenv import load_dotenv

load_dotenv()

stram = open("config.yml", "r")
config = yaml.load(stram)
headers = {'Private-Token': os.environ.get('ACCESS_TOKEN')}
api_url = os.path.join(config.get('gitlab'), 'api/v4/')
source_poject = config.get('source-project')
query_params = {
    'per_page': '100',
}
source_issues_url = os.path.join(api_url, 'projects/', str(source_poject), 'issues/')
tickets = requests.get(
    url=source_issues_url,
    params=query_params,
    headers=headers,
)
for project in config.get('projects'):
    print(f'Start creating issues for project: {project}')
    create_issue_url = os.path.join(api_url, 'projects/', str(project), 'issues/')
    for ticket in tickets.json():
        print(f'Create ticket: {ticket.get("title")}')
        requests.post(
            url=create_issue_url,
            headers=headers,
            data={
                'title': ticket.get('title'),
                'description': ticket.get('description'),
                'labels': ticket.get('labels'),
                # 'assignee_ids': data.get('assignees').map(lambda a: a.get('id')),
            }
        )
