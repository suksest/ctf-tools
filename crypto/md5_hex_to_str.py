'''
	Created by: Sukma Setyaji
	Time created: 2017-07-02 09:55
	thanks for solution and inspiration from:
	[1] https://github.com/HackThisCode/CTF-Writeups/blob/master/2017/EasyCTF/Hash%20On%20Hash/README.md
	[2] https://stackoverflow.com/questions/11555468/how-should-i-read-a-file-line-by-line-in-python
'''

import hashlib
hashdict = []
decoded = ""

for i in range(255):
	hashdict.append(hashlib.md5(chr(i)).hexdigest())

with open('hashedtext.txt') as fp:
    for line in fp:
        for iterate in range(len(hashdict)):
        	if line.strip() == hashdict[iterate]:
        		decoded += chr(iterate)
        		
f = open('decodedtext.txt','w')
f.write(decoded)
