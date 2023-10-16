from eth_account import Account
from eth_account.messages import encode_defunct

from web3.auto import w3

# Create an random account and private key
private_key = "0x5f7bc1ba5fa3f035a5e34bfc399d1db5bd85b39ffac033c9c8929d2b6e7ff335"
acct = Account.from_key(private_key)

# Sign a Message with the Private Key
msg = "0xe1f4a6d2598effe3f078a3c8b73456b8868ba1aa57d48f92248d284eb4a482ef"
message = encode_defunct(hexstr=msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)


print("\nPrivate Key:", private_key)
print("\nAddress:", acct.address)
print("\nHashed Message:", signed_message.messageHash.hex())
print("\nSignature:", signed_message.signature.hex(), "\n")
