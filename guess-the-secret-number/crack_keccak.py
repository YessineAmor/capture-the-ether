from web3 import Web3, IPCProvider

w3 = Web3(IPCProvider())

for i in range(0,256):
    if(w3.solidityKeccak(['uint8'], [i]).hex() == "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365"):
        print("hash cracked: ",i)