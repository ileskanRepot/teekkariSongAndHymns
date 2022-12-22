import requests
import json
import os

def getIds(url):
	try:
		data = json.loads(requests.get(url).text)
	except requests.exceptions.ConnectionError:
		return []

	ids = []
	for p_id in data:
		ids.append(p_id['id'])
	return ids
	
def getSongsFromWeb(idS, url):
	pairs = []
	size = len(idS)
	for j, i in enumerate(idS):
		try:
			data = json.loads(requests.get(f'{url}/{str(i)}').text)
			pairs.append((f'{url}/{str(i)}', data['name'], data['tune']))
		except requests.exceptions.ConnectionError:
			print("Not found")
		print(f'{round(j / size * 100,2)}%')
	
	return pairs

def putToCsvFile(file, data, title):
	with open(file, 'a') as f:
		if os.stat(file).st_size == 0:
			f.write(f"{title[0]}, {title[1]}, {title[2]}\n")
		for row in data:
			f.write(f"{row[0]}, {row[1]}, {row[2]}\n")

if __name__ == "__main__":
	url = "https://rasputin.fi/api/song"
	# url = "https://rasroathearshasputin.fi/api/song"
	print("Start")
	ids = getIds(url)
	print("Got Ids")
	tuples = getSongsFromWeb(ids, url)
	print("Got songs")
	putToCsvFile("test.csv", tuples, ("Url", "Song", "Theme"))
	print("All done")
