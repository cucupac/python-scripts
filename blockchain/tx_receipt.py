from web3 import Web3
from web3.exceptions import TransactionNotFound

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

transaction_hash = "0xee6d83e952211d845f1cd09cc7764989085916d96d09d82ca417a7e56cc56bfa"

try:
    transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)
except TransactionNotFound as e:
    print(f"[TRANSACTION NOT FOUND]: {e}")
else:
    for key, value in transaction_receipt.items():
        if isinstance(value, bytes):
            value = value.hex()
        print(f"{key}: {value}")
