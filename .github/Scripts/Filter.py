import json

def filtering(data):
    datas = data["results"]
    result = []
    
    for page in datas:
        instance = {}
        
        instance["Name"] = checkIntroduction(page["properties"]["이름"]["title"])
        instance["Email"] = page["properties"]["E-mail"]["email"]
        instance["Position"] = getItems(page["properties"]["Role"]["multi_select"])
        instance["Responsibility"] = getItems(page["properties"]["Session"]["multi_select"])
        instance["Introduction"] = checkIntroduction(page["properties"]["Introduction"]["rich_text"])
        instance["GithubLink"] = page["properties"]["Github"]["url"]
        instance["Image"] = checkCover(page["cover"])
        instance["Year"] = getItems(page["properties"]["Year"]["multi_select"])
        
        result.append(instance)
    
    return json.dumps(result, ensure_ascii=False)


def checkCover(data):
    if data:
        if data.get("type") == "file" and data.get("file"):
            return data["file"]["url"]
        elif data.get("type") == "external" and data.get("external"):
            return data["external"]["url"]
    
    return None

def checkIntroduction(data):
    if data:
        return data[0]["plain_text"]
    return None
        
def getItems(multi_select):
    items = []
    
    for item in multi_select:
        items.append(item["name"])
    
    return items