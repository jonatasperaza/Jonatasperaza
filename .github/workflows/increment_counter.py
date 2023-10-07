python
import requests
import json

# Replace 'your_username' and 'your_repo' with your actual GitHub username and repository name
url = f'https://api.github.com/repos/your_username/your_repo/contents/README.md'

# Replace 'your_personal_access_token' with your actual GitHub personal access token
headers = {'Authorization': 'token your_personal_access_token'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')

    if '[![' in decoded_content:
        counter_start = decoded_content.find('[![' + '1')
        counter_end = counter_start + decoded_content[counter_start:].find(']') + 1
        counter_value = int(decoded_content
