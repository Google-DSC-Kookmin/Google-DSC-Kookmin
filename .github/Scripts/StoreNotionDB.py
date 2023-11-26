import requests, json

def storeDatabase(databaseId, headers, Year):
    
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    body = getBody(Year)
    res = requests.post(readUrl, headers=headers, data=json.dumps(body))
    print(res.status_code)

    data = res.json()
    data = filtering(data)
    
    with open(f"./data/{Year}_Member.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)
        
def getBody(Year):
    body = {
                "filter": {
                    "property": "Year",
                    "multi_select": {
                        "contains": f"{Year}"
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

def filtering(data):
    datas = data["results"]
    result = []
    
    for page in datas:
        instance = {}
        instance["name"] = page["properties"]["이름"]["title"][0]["plain_text"]
        instance["email"] = page["properties"]["e-mail"]["email"]
        
        instance["roles"] = []
        for role in page["properties"]["Role"]["multi_select"]:
            instance["roles"].append(role["name"])
        
        instance["year"] = page["properties"]["Year"]["multi_select"][0]["name"]
        
        result.append(instance)
    
    return json.dumps(result, ensure_ascii=False)
        

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