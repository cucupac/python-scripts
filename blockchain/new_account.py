from web3 import Web3, Account

# Connect to the Ethereum network using an Infura API endpoint
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

# Generate a new Ethereum account
account = Account.create()
new_account_address = account.address
new_account_private_key = account.key

# Print the new account address and private key
print("Address: ", new_account_address)
print("Private key: ", new_account_private_key.hex())
