Through this data visualization, we see the distribution of events date-wise for the year 2015. Eventbrite's data is accessible through their JSON API. This visualization makes use of the same API to query and get the data related to the start dates of the events. 

##### Features:
* Displays the data for the entire year 2015 (the year for which the data was queried)
* Upon hovering the mouse over each date, 
* Makes use of UNIX epoch time for keeping track of the dates of the year. The data available from Eventbrite API is in "YYYY-mm-ddTHH:MM:SS" format. This is converted into UNIX epoch time using the time.mk_time function available in Python.
* On hovering the mouse over each date, it displays the date value and the number of events that have occured/ will occur on that particular day.

##### Screenshots: 
The following screenshot displays a sample value for a day in month of June 2015
 ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/CalendarJune.png)

The following screenshot displays a sample value for a day in month of December 2015
 ![My image](https://github.com/ashwintumma23/EventbriteDataVisualizations/blob/master/Images/CalendarDecember.png)
