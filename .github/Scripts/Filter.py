import json

def filtering(data):
    datas = data["results"]
    result = []
    
    for page in datas:
        instance = {}
        
        instance["Name"] = page["properties"]["이름"]["title"][0]["plain_text"]
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
    if data == None:
        return None
    return data["file"]["url"]

def checkIntroduction(data):
    if data == []:
        return None
    return data[0]["plain_text"]
        
def getItems(multi_select):
    items = []
    
    for item in multi_select:
        items.append(item["name"])
    
    return items