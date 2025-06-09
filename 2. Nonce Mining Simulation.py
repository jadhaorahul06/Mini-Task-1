import time

def mine_block(block, difficulty):
    start = time.time()
    target = "0" * difficulty
    while block.hash[:difficulty] != target:
        block.nonce += 1
        block.hash = block.calculate_hash()
    print(f"Mined in {time.time()-start:.2f}s. Nonce: {block.nonce}, Hash: {block.hash}")

mine_block(Block(0, "Mining Test", "0"), 4)  # Finds hash starting with "0000"