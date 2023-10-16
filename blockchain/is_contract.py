from web3 import Web3

from dotenv import load_dotenv

load_dotenv(".env")

web3_client = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

# Address to check
address = web3_client.to_checksum_address("0xD2AD2cAb15FC7cf2387421DFe688569AEba9bC89")

# Get the address bytecode
byte_code = web3_client.eth.get_code(address)

if byte_code == "0x":
    print(f"EOA.")
else:
    print("Contract.")
