#!/usr/bin/env python

from instagram.client import InstagramAPI
from urlparse import urlparse
import pickle
import networkx as nx
import keys

api = InstagramAPI(access_token=keys.access_token)

tag = 'leomessi'
num_iterations = 1000
count = 50

try:
	dataFile = open('data.pk1', 'rb')
	data = pickle.load(dataFile)
	print 'successfully loaded pickle'
except:
	data = dict()

def getData(mediaList):
	for m in mediaList:
		mediadata = dict()
		#this is the key for the data dictionary
		mediaID = m.id
		#put stuff in mediadata
		if hasattr(m, 'location'):
			mediadata['location'] = m.location
		mediadata['user'] = m.user.username
		mediadata['like_count'] = m.like_count
		mediadata['comment_count'] = m.comment_count
		if mediaID in data.keys():
			continue
		else:
			data[mediaID]=mediadata

max_tag_id = 0
ans = api.tag_recent_media(count, max_tag_id, tag)
getData(ans[0])

parsed = urlparse(ans[1])
params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

for i in range(num_iterations):
	max_tag_id = int(params['max_tag_id'])
    	ans = api.tag_recent_media(200, max_tag_id-1, tag)
    	getData(ans[0])

print data
output = open('data.pk1', 'wb')
pickle.dump(data, output)
output.close()
