import os
import copy
import zlib
def save_compile(f1, data):
    comp = zlib.compress(data, level=9)
    
    f1.write(comp)

def load_compile(filename):
    with open(filename, "rb") as f:
        comp = f.read()
    return zlib.decompress(comp)

print("\033c\033[47;30m\ngive me the .txt .video file ? \n")
a=input().strip()
f1=open(a,"r")
f=f1.read()
f1.close()
ff=f.split("\n")
names=ff[0]
files=ff[1]
counter=0
f1=open(names+".video","wb")
f1.write(b"\x01\x00\x05\x04\x03\x07")
f1.write(b"JABA")
f1.write(b"\x01\x00\x05\x04\x03\x02")
f1.write(names.encode())

f1.close()

for d in ff:
    if counter!=0 and d.strip()!="":
        f1=open(d,"rb")
        fff=f1.read()
        f1.close()
        f1=open(names+".video","ba")
        f1.write(b"\x01\x00\x05\x04\x03\x07")
        f1.write(d.strip().encode())
        f1.write(b"\x01\x00\x05\x04\x03\x02")
        save_compile(f1,fff)
        f1.close()
    counter=counter+1
