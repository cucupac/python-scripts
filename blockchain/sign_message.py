from eth_account import Account
from eth_account.messages import encode_defunct

from web3.auto import w3

# Create an random account and private key
private_key = "d61cc104ba3c26326853f6d56cb5acc6810909369d16ffd2afef24eba2fb87df"
acct = Account.from_key(private_key)

# Sign a Message with the Private Key
msg = "0xf0b24551038f161000240c3164686029d75d7299c862836a65ddc23f8497b74b"
message = encode_defunct(hexstr=msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)

r = signed_message.r.to_bytes(32, byteorder="big").hex()
s = signed_message.s.to_bytes(32, byteorder="big").hex()
v = signed_message.v


print("\nPrivate Key:", private_key)
print("\nAddress:", acct.address)
print("\nHashed Message:", signed_message.messageHash.hex())
print("\nSignature:", signed_message.signature.hex(), "\n")
print("\nv:", v)
print("\nr:", r)
print("\ns:", s)
