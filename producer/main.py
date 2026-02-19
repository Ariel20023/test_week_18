import json
 

with open("border_alerts.json",encoding="utf-8") as f:
            data = json.load(f)
for d in data:
        print(d)



