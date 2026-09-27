import hashlib
from validate_docbr import CPF
from fastapi import FastAPI
from pydantic import BaseModel
import json

from block import Block
from blockchain import Blockchain
from contract import VotingContract

cpf = CPF()

class VoteRequest(BaseModel):
    choice: str
    voter_cpf: str

DIFFICULTY = 3

app = FastAPI()
blockchain = Blockchain(DIFFICULTY)
categories = list(blockchain.get_categories())
voting_contract = VotingContract(blockchain)

@app.get("/chain")
def get_chain():
    return blockchain.get_chain()

@app.get("/result")
def get_sorted_votes():
    votes = blockchain.get_votes()
    return sorted(votes.items(), key=lambda x: x[1], reverse=True)

@app.get("/categories")
def get_categories():
    return categories

@app.get("/download")
def export_blockchain():
    chain = blockchain.get_chain()
    return json.dumps(chain, indent=4)

@app.get("/stats")
def get_votes_dataframe():
    votes = blockchain.get_votes()
    return votes

@app.post("/candidate")
def add_candidate(new_category: str):
    global categories

    if new_category and new_category not in categories:
        categories.append(new_category)
        categories.sort()

        return True, f"The category {new_category} has been created."
    else:
        return False, "Invalid or already existent category"

@app.post("/vote")
def validate_and_vote(vote: VoteRequest):
    choice = vote.choice
    voter_cpf = vote.voter_cpf

    valid, result = voting_contract.validate_vote(
        choice,
        voter_cpf,
        categories
    )

    if not valid:
        return {"success": False, "message": result}

    voter_id_hash = result
    blockchain.add_block({"voto": choice}, voter_id_hash)

    return {"success": True, "message": "Vote successfully registered"}
