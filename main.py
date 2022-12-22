from rasputin import getIds, getSongsFromWeb, putToCsvFile
from lauluja import getSongsFromJson

if __name__ == "__main__":
	url = "https://rasputin.fi/api/song"
	songFileName = 'test.csv'
	ids = getIds(url)
	tuples = getSongsFromWeb(ids, url)
	putToCsvFile(songFileName, tuples, ("Url", "Song", "Theme"))

	fileName = "lauluja.json"
	tuples = getSongsFromJson(fileName)
	putToCsvFile(songFileName, tuples, ("Url", "Song", "Theme"))
