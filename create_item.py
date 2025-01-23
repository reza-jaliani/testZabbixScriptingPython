import requests
import json

url = "http://192.168.25.128/zabbix/api_jsonrpc.php"
tokenHeaders = {"Content-Type": "application/json"}
tokenPayload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "username": "Admin",
        "password": "zabbix"
    },
    "id": 1
}
tokenResponse = requests.post(url, data=json.dumps(tokenPayload), headers=tokenHeaders)
tokenOutput = tokenResponse.json()
token = tokenOutput['result']

itemPayload = {
    "jsonrpc": "2.0",
    "method": "item.create",
    "params": {
        "name": "test_item",
        "key_": "system.cpu.load[all,avg2]",
        "hostid": "10084",
        "type": 0,
        "value_type": 0,
        "interfaceid": 1,
        "delay": "60s"
    },
    "auth": token,
    "id": 2
},

itemResponse = requests.post(url, data=json.dumps(itemPayload), headers=tokenHeaders)
itemResult = itemResponse.json()
print(itemResult)
