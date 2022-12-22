import json
import os

def getSongsFromJson(fileName):
	pairs = []
	with open(fileName, 'r') as f:
		# print(json.loads(f.read()))
		data = json.loads(f.read())
		print("Wee")
		for dat in data:
			if dat['metadata'] == []:
				pairs.append(('https://laulukirja.asteriski.fi', dat['title'], ""))
			else:
				pairs.append(('https://laulukirja.asteriski.fi', dat['title'], dat['metadata'][0]))
	return pairs
			
def putToCsvFile(file, data, title):
	with open(file, 'a') as f:
		if os.stat(file).st_size == 0:
			f.write(f"{title[0]}, {title[1]}, {title[2]}\n")
		for row in data:
			f.write(f"{row[0]}, {row[1]}, {row[2]}\n")

if __name__ == "__main__":
	fileName = "lauluja.json"
	tuples = getSongsFromJson(fileName)
	putToCsvFile("test.csv", tuples, ("Url", "Song", "Theme"))

