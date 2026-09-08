import hashlib
import time


messages = [
    b"document_001",
    b"document_002",
    b"document_003",
    b"document_004",
    b"document_001",  # doublon
    b"document_005",
    b"document_002",  # doublon
]

while True:
    for message in messages:
        fingerprint= hashlib.sha256(message).hexdigest()
        print(f'"{message.decode()}"-> {fingerprint}')
        time.sleep(0.01)
    
