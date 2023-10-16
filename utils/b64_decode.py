"""DECODE"""
import base64

encoded_string = "W3siY2hhaW5faWQiOiA1LCAiZW1pdHRlcl9hZGRyZXNzIjogIjB4QkY4YTEzODdENDY4MkI1QjQzMUNlYThmNTNFREQ1RTdhNzgzNDg2MSJ9XQ=="  # Old
message_bytes = base64.b64decode(encoded_string)
print("Message Bytes:", message_bytes)
