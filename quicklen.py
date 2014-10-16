import sys, pickle

o = sys.argv[1]
f = open(o,'rb')
d = pickle.load(f)
print len(d.keys())
