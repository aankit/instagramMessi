from instagram.client import InstagramAPI
import keys

api = InstagramAPI(access_token=keys.access_token)

tags = ['leomessi','cristiano']
num_iterations = 100
count = 200

try:
	resultsFile = open('footie.pk1', 'r+b')
	data = pickle.load(resultsFile)
except:
	resultsFile = open('footie.pk1', 'wb')
	data = {}

for t in tags:
	max_tag_id = 0
	ans = api.tag_recent_media(count, max_tag_id, t)
	for a in ans[0]:
		data[t]=a

	parsed = urlparse(ans[1])
	params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

for i in range(num_iterations):
	for t in tags:
		max_tag_id = int(params['max_tag_id'])	
		ans = api.tag_recent_media(count, max_tag_id-1, t)
		for a in ans[0]:
			data[t]=a

		parsed = urlparse(ans[1])
		params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

pickle.dump(data, resultsFile)
dataFile.close()
