import requests
import json
authkey = open("authkey.txt", "r").read()
get = requests.get(authkey)
json_parsed = json.loads(get.content)
noOfCandidates = 1
for candidate in json_parsed:
    print(noOfCandidates)
    print (json_parsed[candidate]['name'])
    print (json_parsed[candidate]['desc'])
    noOfCandidates+=1
