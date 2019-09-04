from web3 import Web3, IPCProvider, HTTPProvider

w3 = Web3(HTTPProvider("https://ropsten.infura.io"))
block = w3.eth.getBlock(
    6329069 - 1)
timestamp = w3.eth.getBlock(
    6329069)['timestamp']
answerHash = w3.solidityKeccak(['bytes32', 'uint256'], [
                               block['hash'].hex(), timestamp]).hex()
print("Answer hash:", answerHash)
print("Answer is", w3.toInt(hexstr=answerHash) % 256)
