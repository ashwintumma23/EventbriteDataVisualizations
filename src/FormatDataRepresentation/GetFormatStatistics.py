# Start writing the data points value to the output file


        # The token mentioned in the URL is the token which I got generated from the Event Brite API User Interface
        # For security purposes I have masked the token with all Xs in the published version of this Python code, 
        # but you can get yours generated similary from Event Brite's Generate Token Page.
import urllib2
import json
 
response = urllib2.urlopen('https://www.eventbriteapi.com/v3/formats/?token=CVFVRR3UQX4IGUCYTFBK')
data = json.load(response)

formats = data['formats']


formatDict = {}
formatNamesDict = {}
formatLongNamesDict = {}

print "Printing the ids now"
for k in formats:
	# Initialize the dictionary with the format ids as the key and ZERO as its value
	formatDict[k['id']] = 0;
	print k['short_name']
	formatNamesDict[k['id']] = k['short_name'].strip();
	formatLongNamesDict[k['id']] = k['name'].strip()
	

# Populate the dictionary from the values that we have fetched earlier

pointsFile = open('LocationDateFormatData.txt')
for line in pointsFile:
	formatID =  line.split(' ,')[3].strip()
	if formatID.strip() != "None":
		formatDict[formatID] = formatDict.get(formatID) + 1

pointsFile.close()

# Generate a new JSON file to be read by the FormatBubbleChart.html file
jsonOutputFile = open('format.json','wb')
jsonOutputFile.write('{\n "name": "format",\n "children": [\n')

formatDictLen = len(formatDict)
index = 0 
for formatID, size in formatDict.items():	
	jsonOutputFile.write('{"name": "'+formatNamesDict.get(formatID)+'", "longName":"' + formatLongNamesDict.get(formatID)+'", "size":'+str(size)+'}') 
	print index
	if index < formatDictLen -1:
		jsonOutputFile.write(',\n') 
	index+=1

jsonOutputFile.write('\n]}')
jsonOutputFile.close()

