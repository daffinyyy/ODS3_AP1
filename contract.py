import hashlib
from validate_docbr import CPF


class VotingContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.cpf = CPF()

    def validate_vote(self, candidate, voter_cpf, candidates):
        # deve existir pelo menos um candidato
        if not candidates:
            return False, "There are no registered candidates"

        # Regra 1: o candidato escolhido deve existir
        if candidate not in candidates:
            return False, "Invalid candidate"

        # Regra 2: o CPF deve ser válido
        if not self.cpf.validate(voter_cpf):
            return False, "Invalid CPF"

        # Regra 3: um eleitor só pode votar uma vez
        voter_id_hash = hashlib.sha256(
            voter_cpf.encode()
        ).hexdigest()

        if self.blockchain.has_user_voted(voter_id_hash):
            return False, "You have already voted"

        return True, voter_id_hash