import datetime
import hashlib
import json
import os

class Blockchain:
    def __init__(self):
        self.chain = list()

    def createBlock(self, proof, data):
        block = { 'index': self.getLastIndex(),
                    'timestamp': str(datetime.datetime.now()),
                    'proof': self.proofOfWork(proof),
                    'data': data,
                    'currentHash': self.newHash(data),
                    'previousHash': self.getLastHash() }
        self.chain.append(block)
        self.writeToFile()
        #return block

    def proofOfWork(self, previousProof):
        newProof = 1
        checkProof = False
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof**2 - previousProof**2).encode()).hexdigest()
            if hashOperation[:3] == '000':
                checkProof = True
            else:
                newProof += 1
        return newProof

    def newHash(self, data):
        encodedBlock = (str(self.getLastHash()) + str(data)).encode()
        return hashlib.sha256(encodedBlock).hexdigest()

    def validateChain(self, chain):
        previousBlock = chain[0]
        blockIndex = 1
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if blockIndex['previousHash'] != self.newash(previousHash):
                return False
            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.sha256(str(proof**2 - previousProof**2).encode()).hexdigest()
            if hashOperation[:3] != '000':
                return False
            previousBlock = block
            blockIndex += 1
        return True

    def writeToFile(self):
        filename="doc.json"
        openType = "a"
        with open(filename, openType) as f:
            x = json.dumps(self.chain[-1], indent=4)
            f.write(x)
            f.write("\n")
        f.close()

    def getLastIndex(self):
        filename = "doc.json"
        file = open(filename, "r")
        f = str(file.readlines())
        start = f.rindex("index") + 8
        end = start+1
        while (f[end] != ","):
            end = end + 1
        return int(f[start:end])+1

    def getLastProof(self):
        filename = "doc.json"
        file = open(filename, "r")
        f = str(file.readlines())
        start = f.rindex("proof") + 8
        end = start+1
        while (f[end] != ","):
            end = end + 1
        return int(f[start:end])

    def getLastHash(self):
        filename = "doc.json"
        file = open(filename, "r")
        f = str(file.readlines())
        start = f.rindex("currentHash") + 15
        end = start+1
        while (f[end] != ","):
            end = end + 1
        #print(f[start:end-1])
        return f[start:end-1]

    def execute(data = ""):
        blockchain = Blockchain()
        #while(True):
            #data = str(input("Enter '}' to end addition to te block for now\nEnter the data to add to the block:\n"))
        blockchain.createBlock(proof = blockchain.getLastProof(), data=data)

