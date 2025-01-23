import requests
import json

URL = "http://192.168.25.128/zabbix/api_jsonrpc.php"
tokenheaders = {"Content-Type": "application/json"}

tokendata = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "username": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

tokenresponse = requests.post(URL, data=json.dumps(tokendata), headers=tokenheaders)
tokenoutputs = tokenresponse.json()

hostdata = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid", "host"]
    },
    "id": 2,
    "auth": tokenoutputs['result']
}

hostresponse = requests.get(URL,data=json.dumps(hostdata), headers=tokenheaders)
hostoutputs = hostresponse.json()
hosts = hostoutputs['result']
for host in hosts:
    print(f"Host ID: {host['hostid']}-------Host Name: {host['host']}")
