#############################################################################################

# Python script for creating the HTML file which contains the data points for event location.
# The data visualization format we will be leveraging in this code is of Google Maps API version 3.

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 18, 2015

# Central Idea: 
# -------------
# Google Maps API version 3 provides an interface for creation of heatmap by specifying the location 
# encoded in its latitude and longtitude format. 

# We have already obtained the data for the events' location using a separate python file, and 
# have the data available in LocationDateFormatData.txt file. We will be using the location values 
# from this file. 

# We use two pre-requisite files for this program: file1.html and file2.html which simply contain 
# the HTML code which needs to be present in the destination file for rendering purposes. 

# Usage: 
# ----------
# $ python CreateGoogleAPIHeatMapFile.py 
# The output of this program will be a file named - GoogleMapsHeatMapFile.html which will contain 
# all the data points encoded in the latitude and longitude format along with all the data required 
# for rendering the map.

#############################################################################################

# HTML Header information
file1 = open('file1.html')
heatMapFile = open('GoogleMapsHeatMapFile.html','wb')
for line in file1:
	heatMapFile.write(line)
file1.close()

# Start writing the data points value to the output file
pointsFile = open('LocationDateFormatData.txt')
for line in pointsFile: 
	heatMapFile.write("  new google.maps.LatLng("+line.split(' ,')[0]+","+line.split(' ,')[1]+"),\n")


# HTML Footer information
file2 = open('file2.html')
for line in file2:
	heatMapFile.write(line)
file2.close()
heatMapFile.close()
