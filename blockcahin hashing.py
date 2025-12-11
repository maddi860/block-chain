# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 12:16:05 2025

@author: maddi
"""

import time #timestamps
import hashlib #can use sha-256 now

class block: #used to define the block class
    def __init__(self, index, data, timestamp, prev_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()
    def compute_hash(self): #used to find the block's hash
         block_str = f'{self.index}{self.timestamp}{self.data}{self.prev_hash}'.encode()
         return hashlib.sha256(block_str).hexdigest()

#the formula for creating blockchain
def creating_blockchain(block_data):
    genesis = block(0,'genesis block',time.time(),'0')#creates the genesis block
    blockchain = [genesis]
    for i, data in enumerate(block_data, start = 1):
        prev_block = blockchain[-1]
        new_block = block(i, prev_block, data,time.time())
        blockchain.append(new_block)
    return blockchain

#actually creating the block chain
data = ['1','2','3','4','5'] #data for each block
blockchain = creating_blockchain(data)
for block in blockchain:
    print(f'index:{block.index}')
    print(f'timestamp:{block.timestamp}')
    print(f'data:{block.data}')
    print(f'block hash:{block.hash}')
    print(f'previous hash:{block.prev_hash}')
    print('---------------')