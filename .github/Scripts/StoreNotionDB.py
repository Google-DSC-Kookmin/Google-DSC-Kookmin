import requests, json
from Filter import filtering

def storeDatabase(databaseId, headers, Year):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    body = getBody(Year)
    res = requests.post(readUrl, headers=headers, data=json.dumps(body))
    print(res.status_code)

    if res.status_code == 200:
        data = filtering(res.json())
        
        data = json.loads(data)
        data = [ item for item in data if Year in item["Year"] ]

        with open(f"./data/{Year}_Member.json", "w", encoding="utf8") as f:
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
    with open('./.secrets.json') as f:
        secrets = json.loads(f.read())
        
    token = secrets['Notion_Token']

    databaseId = secrets['Notion_Database_ID']

    headers = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2022-06-28"
    }

    Years = ["22-23", "23-24"]
    
    for year in Years:
        storeDatabase(databaseId, headers, year)