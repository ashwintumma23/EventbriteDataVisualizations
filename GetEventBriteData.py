#############################################################################################
# Python script for fetching the following data from the Event Brite JSON API: 
# 1. Location (Latitude and Longitude) of the event 
# 2. Start date of the event 
# 3. Format ID of the event

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 18, 2015

# Central Idea: 
# -------------
# This script is used to get data for various data visualization pages that I have created. 
# Here is a brief explanation of how data related is fetched: 
# 1. Location (Latitude and Longitude) of the event: 
# The address of each event is encoded in the JSON string for the event. It is readily accessible 
# through [events].[venue].[latitude] and [events].[venue].[longitude] values. 

# 2. Start date of the event: 
# Fetched through: [events].[start].[local] : Gets the value of the start date and time (local to that time zone)

# 3. Format ID of the event: 
# Fetched through [events].[formatid] : get the events format (For instance: conference, convention, rally, tournament, etc.)

# Usage: 
# ----------
# $ python GetEventBriteData.py > LocationDateFormatData.txt
# The output of this program is redirected to the LocationDateFormatData.txt file

# Alternatives for usage: 
# ------------------
# I chose to redirect the output of this program to a text file from commmand line, to avoid 
# increasing lines of code in this file. But having said that, alternatively, we can also write the 
# data to a file mentioned by the user at command line. 

#############################################################################################
import urllib2
import json

# 4087 was the page count (with each page having 50 entries) on the day this script was written
for page in range(1, 4087):
        # The token mentioned in the URL is the token which I got generated from the Event Brite API User Interface
        # For security purposes I have masked the token with all Xs in the published version of this Python code, 
        # but you can get yours generated similary from Event Brite's Generate Token Page.
	response = urllib2.urlopen('https://www.eventbriteapi.com/v3/events/search/?token=XXXXXXXXXXXXXXXXXXX&page='+str(page))
	data = json.load(response)   

	events = data['events']
	
	for k in events: 
		if k['venue'] is None:
			continue	
		else:
			# Use fileoutput.write instead of print, when writing to a file
			print k['venue']['latitude'], ",",k['venue']['longitude'],",",k['start']['local'],",",k['format_id']

