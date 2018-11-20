class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # creates a new block and adds it to the chain
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        生成新交易信息，信息将加入到下一个待挖的区块中
        params:
            - sender address of sender
            - recipient address of recipient
            - amount
        return:
            - the index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        # hashes a block
        pass
    
    @property
    def last_block(self):
        # return the last block in the chain
        pass