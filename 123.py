import re

def lcschecker(M,N):
	c = 0
	l1 = len(M)
	l2 = len(N)
	for i in M:
		for j in N:
			if i == j:
				if len(i)>c:
					c = len(i)
	return c

def plagarism(f1,f2):
	f = open(f1,'r')
	L1 = f.read()
	L1 = re.sub(r'[^a-z A-Z0-9_\n]', ' ', L1)
	f.close()
	s1 = len(L1)
	L1 = L1.lower().split()

	f = open(f2,'r')
	L2 = f.read()
	L2 = re.sub(r'[^a-zA-Z 0-9_\n]', ' ', L2)
	f.close()
	s2 = len(L2)
	L2 = L2.lower().split()

	print(f1,"and",f2,"are",(lcschecker(L1,L2)*2*100)/(s1+s2),"% matching")
				
import os
files = []
for file in os.listdir('.'):
     if (os.path.isfile(file)) and (file.endswith(".txt")):
     	files.append(file)

for i in range(len(files)):
	for j in range(i,len(files)):
		if i!=j:
			plagarism(files[i],files[j])