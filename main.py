import requests
import json


class Candidate:
    def __init__(self, desc, votes, name, uid):
        self.desc = desc
        self.votes = votes
        self.name = name
        self.uid = uid


def getWinner():
    authkey = open("authkey.txt", "r").read()
    get = requests.get(authkey)
    json_parsed = json.loads(get.content)
    highest_votes = 0
    highest_votes_id = 0
    highest_votes_name = ""
    for candidate in json_parsed:
        if json_parsed[candidate]["votes"] > highest_votes:
            highest_votes = json_parsed[candidate]["votes"]
            highest_votes_id = candidate
            highest_votes_name = json_parsed[candidate]["name"]

    return  {
        "highest_votes":highest_votes,
        "highest_votes_id":highest_votes_id,
        "highest_votes_name":highest_votes_name,
    }


print("Type: \n"
      "'See winner' to see the winner of the elections\n"
      "'Delete Candidate' to delete all candidates from the list\n"
      "'Add Candidates' to add a candidate to the list \n"
      "'Reset' to reset the voting preferences of the voters in order to conduct another election\n")
choice = input("> ")
if choice.upper() == "SEE WINNER":
    print("The winner of the elections is: ", getWinner()["highest_votes_name"], "!! with ", getWinner()["highest_votes"], "votes!!")
