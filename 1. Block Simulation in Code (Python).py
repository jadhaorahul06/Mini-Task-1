import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        return hashlib.sha256(
            f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        ).hexdigest()

# Create blockchain
blockchain = [Block(0, "Genesis Block", "0")]
for i in range(1, 3):
    blockchain.append(Block(i, f"Block {i} Data", blockchain[-1].hash))

# Tamper test
blockchain[1].data = "Tampered Data"
print(f"Block 2's previous hash now invalid: {blockchain[2].previous_hash != blockchain[1].hash}")