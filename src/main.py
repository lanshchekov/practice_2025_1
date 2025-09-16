import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        # Create encoded string as a hash body
        hash_body = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
        sha.update(hash_body)
        return sha.hexdigest()


import datetime as date


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
  index = last_block.index + 1
  timestamp = date.datetime.now()
  data = "Hey! I'm block " + str(index)
  return Block(index, timestamp, data, last_block.hash)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
last_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 5

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(last_block)
  blockchain.append(block_to_add)
  last_block = block_to_add

  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Hash: {}\n".format(block_to_add.hash))