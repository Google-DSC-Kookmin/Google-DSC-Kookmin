import os
import requests
import json
from Filter import filtering

script_dir = os.path.dirname(os.path.abspath(__file__))

def load_secrets():
    secrets_path = "./.secrets.json"

    if os.path.isfile(secrets_path):
        with open(secrets_path) as f:
            secrets = json.loads(f.read())
        return secrets
    else:
        return {
            "Notion_Token": os.environ.get('NOTION_TOKEN'),
            "Notion_Database_ID": os.environ.get('NOTION_DATABASE_ID')
        }

def storeDatabase(databaseId, headers, Year):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    body = getBody(Year)
    res = requests.post(readUrl, headers=headers, data=json.dumps(body))
    print(res.status_code)

    if res.status_code == 200:
        data = filtering(res.json())
        
        data = json.loads(data)
        data = [item for item in data if Year in item["Year"]]

        file_path = os.path.join(script_dir, "..", "..", "data", f"{Year}_Member.json")
        print(f"Script directory: {script_dir}")
        print(f"Target file path: {file_path}")

        with open(file_path, "w", encoding="utf8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def getBody(Year):
    body = {
        "filter": {
            "property": "Year",
            "multi_select": {
                "contains": {
                    "name": Year
                }
            }
        },
        "sorts": [
            {
                "property": "이름", 
                "direction": "ascending"
            }
        ]
    }
    
    return body        

if __name__ == "__main__":
    secrets = load_secrets()

    token = secrets['Notion_Token']
    databaseId = secrets['Notion_Database_ID']

    headers = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2022-06-28"
    }

    Years = ["22-23", "23-24"]
    
    for year in Years:
        storeDatabase(databaseId, headers, year)
