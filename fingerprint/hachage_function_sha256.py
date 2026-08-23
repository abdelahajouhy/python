import hashlib
message= b"Hello"
fingerprint=hashlib.sha256(message).hexdigest()
print(fingerprint)
