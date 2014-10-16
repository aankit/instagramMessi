#!/usr/bin/env python2.7

from instagram.client import InstagramAPI
from urlparse import urlparse
import pickle, os
import networkx as nx
import keys

api = InstagramAPI(access_token=keys.access_token)

tags = ['leomessi','cristiano']
num_iterations = 100
count = 200

try:
	dataFile = open('combined.pk1', 'r+b')
	mediaSeen = open('mediaSeen.pk1', 'r+b')
	data = pickle.load(dataFile)
	mediaSeen = pickle.load(dataFile)
	print 'successfully loaded pickles'
except:
	dataFile = open('combined.pk1', 'wb')
	mediaFile = open('mediaSeen.pk1', 'wb')
	data = dict()
	mediaSeen = set()

def getData(mediaList,tag):
	for m in mediaList:
		mediadata = dict()
		#this is the key for the data dictionary
		mediaID = m.id
		if mediaID in mediaSeen:
			continue
		else:
			mediaSeen.add(mediaID)
			screenName = m.user.username
			likes = [u.username for u in m.likes]
			if screenName in data.keys():
				data[screenName]['tags'].append(tag)
				if hasattr(m, 'location'):
					data[screenName]['location'].append(m.location)
				for l in likes:
					data[screenName]['likes'].append(l)
			else:
				data[screenName] = dict()
				data[screenName]['tags']=list()
				data[screenName]['location']=list()
				data[screenName]['tags'].append(tag)
				if hasattr(m, 'location'):
					data[screenName]['location'].append(m.location)
				data[screenName]['likes']=likes
			
for t in tags:
	max_tag_id = 0
	ans = api.tag_recent_media(count, max_tag_id, t)
	getData(ans[0],t)

	parsed = urlparse(ans[1])
	params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

for i in range(num_iterations):
	for t in tags:
		max_tag_id = int(params['max_tag_id'])	
		ans = api.tag_recent_media(count, max_tag_id-1, t)
		getData(ans[0],t)

		parsed = urlparse(ans[1])
		params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

pickle.dump(data, dataFile)
pickle.dump(mediaSeen, mediaFile)
dataFile.close()
mediaFile.close()
