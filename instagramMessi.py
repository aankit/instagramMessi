#!/usr/bin/env python2.7

from instagram.client import InstagramAPI
from urlparse import urlparse
import pickle, os
import networkx as nx
import keys

api = InstagramAPI(access_token=keys.access_token)

tags = ['leomessi','cristiano']
num_iterations = 1000
count = 200

#data = dict()
#mediaSeen = set()

try:
	print 'here'
	dataFile = open('combined.pk1', 'rb')
	mediaFile = open('mediaSeen.pk1', 'rb')
	maxTagFile = open('maxTag.pk1', 'rb')
	print 'opening works'
	data = pickle.load(dataFile)
	mediaSeen = pickle.load(mediaFile)
	max_tag_id = pickle.load(maxTagFile)
	print 'loaded data!'
	dataFile.close()
	mediaFile.close()
	maxTagFile.close()
	print 'successfully loaded pickles'
except:
	print 'new new new'
	mediaSeen = set()
	data = dict()
	max_tag_id = 0

count = 0
def getData(mediaList,tag):
	for m in mediaList:
		mediadata = dict()
		#this is the key for the data dictionary
		mediaID = m.id
		if mediaID in mediaSeen:
			continue
			count += 1
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
if max_tag_id = 0:			
	for t in tags:
		max_tag_id = 0
		ans = api.tag_recent_media(count, max_tag_id, t)
		getData(ans[0],t)

		parsed = urlparse(ans[1])
		params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

else:
	for i in range(num_iterations):
		for t in tags:
			ans = api.tag_recent_media(count, max_tag_id-1, t)
			getData(ans[0],t)

			parsed = urlparse(ans[1])
			params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}	
			max_tag_id = int(params['max_tag_id'])	
maxTagFile = open('maxTag.pk1', 'wb')
dataFile = open('combined.pk1', 'wb')
mediaFile = open('mediaSeen.pk1', 'wb')
pickle.dump(data, dataFile)
pickle.dump(mediaSeen, mediaFile)
pickle.dump(max_tag_id, maxTagFile)
dataFile.close()
mediaFile.close()
maxTagFile.close()
