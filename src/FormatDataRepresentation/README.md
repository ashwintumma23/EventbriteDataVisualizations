Through this data visualization, we see the distribution of different formats of events that occur on Eventbrite. Eventbrite's data is accessible through their JSON API. This visualization makes use of the same API to query and get the data related to the format. 

### Features
This section enlists the features of the D3 Bubble Chart data visualization. 
* Displays a bubble in the Bubble chart for each type/ format of event on Eventbrite.
* Upon hovering the mouse over each format, a detailed view of the format, along with the number of events occuring/ occured in the state is displayed as a tooltip (See screenshots below).
* The larger the size of the format, more the number of events that were held with that particular format and vice versa.

### Files
This section provides a brief description of the all the files and their purpose in this directory. 
* `FormatBubbleChart.html`: HTML5 code for rendering the Javascript Bubble Chart in the browser
* `GetFormatStatistics.py`: Python script for the following tasks: (1) Get the different format types from the Eventbrite JSON API, (2) Create a dictionary to store the values of the formatIDs for all the events n Eventbrite, and (3) Generate a JSON file which will be the input to the bubble chart D3 rendering.  (See file header  comments for detailed description and elaborate comments).
* `LocationDateFormatData.txt`: Text file containing the data extracted from `src/GetEventBriteData.py`. FormatID value is used from this file. 
* `README.md`: This file
* `format.json`: File which is generated by the `GetFormatStatistics.py` script and which is fed as the input to the `FormatBubbleChart.html` for rendering purposes.

### Code References
* Bubble Charts D3 [Website](http://bl.ocks.org/mbostock/4063269) - For displaying the bubbles

### Screenshots 
Following figure shows the screenshot of distributions of events based on their format. 
  ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/BubbleChart.png)
 
Following figure shows the screenshot of distributions of events based on their format. 
  ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/BubbleChartOne.png)

 
### Other Enhancements: 
 This section lists some of the enhancements that are possible for in this data visualization. 
 * Coloring the circles with different color codes can be done to represent yet another dimension of the data.