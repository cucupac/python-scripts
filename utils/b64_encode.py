import json
import base64

"""ENCODE"""

thing_to_encode = [
    {"chain_id": 2, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 4, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 5, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 6, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 10, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 14, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
    {"chain_id": 23, "emitter_address": "0x4800c8d6ba7176f084004c0294320b634e3476f8"},
]

json_string = json.dumps(thing_to_encode).encode()
encoded_string = base64.b64encode(json_string).decode()
print("Base64 Encoded String:\n\n", encoded_string)
