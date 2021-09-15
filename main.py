import requests
import json




class Candidate():
    def __init__(self, id, votes, name):
        self.id = id
        self.votes = votes
        self.name = name

authkey = open("VoteApp-Priv/authkey.txt", "r").read()
get = requests.get(authkey)
json_parsed = json.loads(get.content)
noOfCandidates = 1

candidates = []
highest_votes = 0
highest_votes_id = 0
highest_votes_name = ""

def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

for candidate in json_parsed:
    candidate_obj = Candidate(json_parsed[candidate]["id"], json_parsed[candidate]["votes"], json_parsed[candidate]["name"])
    if json_parsed[candidate]["votes"] > highest_votes:
        highest_votes = json_parsed[candidate]["votes"]
        highest_votes_id = json_parsed[candidate]["id"]
        highest_votes_name = json_parsed[candidate]["name"]

help = input("Type 'help' if you want to see more options\n"
             ">")

if help.upper() == "HELP":
    print("Type: \n"
          "'See winner' to see the winner of the elections\n"
          "'Delete Candidate' to delete all candidates from the list\n"
          "'Add Candidates' to add a candidate to the list \n"
          "'Reset' to reset the voting preferences of the voters in order to conduct another election\n")
    choice = input("> ")
    if choice.upper() == "SEE WINNER":
        print("The winner of the elections is: ", highest_votes_name, "!! with ", highest_votes, "votes!!")
