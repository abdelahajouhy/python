import hashlib

fingerprints = []
messages = [
    b"hello",
    b"Hello",
    b" hello",
    b" Hello",
    b"hello ",
    b"Hello ",
    b"hello",
]

for message in messages:
    hashes = hashlib.sha256(message).hexdigest()
    fingerprints.append((hashes, message))

lv2=list(enumerate(fingerprints))
for i,fpname in lv2:
    for j,fpname2 in lv2:
        if j>i and fpname[0]==fpname2[0]:
            print(
                f'collision between :\nmsg n°{i+1} - {fpname[0]} - message : "{messages[i].decode()}"\n' 
                f'msg n°{j+1} - {fpname2[0]} - message : "{messages[j].decode()}"'
                )
