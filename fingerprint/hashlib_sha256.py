import hashlib

x="hello"
H =hashlib.new('sha256')
x_byte=bytearray(x,'utf-8')
H.update(x_byte)
y_hexa=H.hexdigest()
print(y_hexa)