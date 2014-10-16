import pickle as p
import sys, os

if os.path.isfile('test.p'):
	f = open('test.p', 'rb')
	d = p.load(f)
	f.close()
	print d
else:
	d = []
	print d
print sys.argv[1]
d.append(sys.argv[1])
print d
f = open('test.p', 'wb')
p.dump(d, f)
f.close()
