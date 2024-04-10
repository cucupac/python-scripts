from Crypto.Hash import keccak


def get_function_selector(function_signature):
    k = keccak.new(digest_bits=256)
    k.update(function_signature.encode())
    return k.hexdigest()[:8]  # Take only the first 4 bytes (8 characters in hex)


# Example
function_signature = "entryPoint(address,bytes)"
selector = get_function_selector(function_signature)
print(f"Function selector for '{function_signature}': {selector}")
