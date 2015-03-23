import time

epochTimeDictionary = {}

pattern = '%Y-%m-%d %H:%M:%S'

pointsFile = open('LocationDateFormatData.txt')


for line in pointsFile:
	try:
		dateTimeValue = line.split(' ,')[2]
		if dateTimeValue != "None".strip():
			dateTimeValue = dateTimeValue.replace("T"," ")
			print dateTimeValue
			epoch = int(time.mktime(time.strptime(dateTimeValue.strip(), pattern)))
			
			if epoch in epochTimeDictionary: 
				epochTimeDictionary[epoch] = epochTimeDictionary.get(epoch) + 1
			else: 
				epochTimeDictionary[epoch] = 1
			print "EPOCH = ", epochTimeDictionary[epoch]
	except:
		continue



jsonOutputFile = open('dateTimeJSON.json','wb')
jsonOutputFile.write("{") 

for epochTime, value in epochTimeDictionary.items():
	jsonOutputFile.write('"'+str(epochTime)+'":'+str(value)+',')

jsonOutputFile.write('"0":0 }')
jsonOutputFile.close()
pointsFile.close()




