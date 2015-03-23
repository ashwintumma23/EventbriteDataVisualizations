# Eventbrite Data Visualizations
This repository contains data analysis and visualization of data from [Eventbrite](https://www.eventbrite.com/). The data required for these optimizations is obtained from the API provided by [Event Bride API](http://eventbriteapi.com/). 

#### Development Platforms and Languages
Python, [D3.js](http://d3js.org/), [Google Maps API v3](https://developers.google.com/maps/), jQuery

#### Author
[Ashwin Tumma](https://sites.google.com/site/ashwintumma23) 
Computer Science Graduate Student,  
Stony Brook University,  
New York, United States  

#### License
GNU GPL v2 (Please read License File)

#### Visualizations
This section lists the various visualizations that are developed for this project
* Heatmap of geographical location of events across the world (with integration to Google Maps)
* Heatmap of count of events in the United States
* Bubble Chart showcasing the different types/ formats of events that occur on Eventbrite.

 Heatmap of Geographical Location of Events across the world (Google Maps API)
 ================================================================================
In this visualization, the geographical location of Eventbrite events is plotted on the global map. Google Maps API is used, so the values for the location are encoded as the `latitude` and `longitude` values of the location. We leverage the power of Google Maps to zoom in and zoom out to have a closer look into any geogprahical location in the world.

###### Code Details: 
* Source Code Directory: `GoogleMapsAPIHeatMap` (Read the README.md file in the corresponding directory)

* References: Google maps API code samples from Google Developers [website](https://developers.google.com/maps/).

Following figure shows the screenshot of the data visualization looking from the global perspective
 ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/GMapFull.png)
  
While, the next figure shows the screenshot of the event location plots for United States:
![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/UnitedStates.png)

Heatmap of count of events in the United States (using D3.js)
================================================================================
In this data visualization, we create a heatmap of the states in the United States of America indicating the number of events which have occured/ will occur in that particular state. The heatmap allows us to have a glance of the event distribution, while on hovering the mouse over the state, the count of the events in that state are displayed.

###### Code Details: 
* Source Code Directory: `D3HeatmapUnitedStates` (Read the README.md file in the corresponding directory)

* References: DataMaps - Open Source code for creating maps [website](http://datamaps.github.io/).  
Tipsy [Website](http://bl.ocks.org/ilyabo/1373263) - For displaying tips on mouse hover

Following figure shows the screenshot of distributions of events based on their count in the United States
 ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/D3Maps.png)
  
  
 ##### Bubble Chart showcasing the different types/ formats of events that occur on Eventbrite (using D3.js)
This is a simple visualization showcasing the weight of the formats of the events on Eventbrite globally. On the event of hovering the mouse over the bubble, shows a detailed description of the format, and also its count.

###### Code Details: 
* Source Code Directory: `FormatDataRepresentation` (Read the README.md file in the corresponding directory)

* References: Bubble Charts D3 [Website](http://bl.ocks.org/mbostock/4063269) - For displaying the bubbles

Following figure shows the screenshot of distributions of events based on their formats
 ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/BubbleChart.png)
  
#### Enhancements
This section lists some of the enhancements that can be done on the visualization charts. 
