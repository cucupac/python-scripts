from Crypto.Hash import keccak


def keccak256(string_data):
    data = string_data.encode("utf-8")
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.hexdigest()


thing_to_hash = (
    "EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"
)
hash = keccak256(thing_to_hash)
print(hash)
