# surfs_up

## Project Overview

### Purpose of Analysis
W. Avy has asked me to do a deeper dive into the temperature trends in June and Dember in Oahu in order to determine if the surf and ice cream shop business is sustainable year round.
I will complete this analysis by comparing the minimum,maximum, and average temperatures for each month.

## Results
![June temperature stats](https://github.com/secicciari/surfs_up/blob/main/Images/June_temp_stats.PNG)
![December temperature stats](https://github.com/secicciari/surfs_up/blob/main/Images/December_temp_stats.PNG)
### Overview
My analysis revealed the below differences in weather between June and December in Oahu:
- June has an average temperature of about 75 degrees, while December has an average temperature of about 71 degrees.
- The minimum temperature that we have recorded in December is 56 degrees. The minimum temperature for June is 64 degrees.
- The maximum temperatures are much more similar; June has a maximum temperature of 85 degrees while December has a maximum of 83 degrees.

### Summary
Although there are some recognizable differences in the temperatures in Oahu in June and December, ultimately the climate appears to be very temperate.
My initial analysis shows that temperature changes throughout the year should not be a deterrent in opening up a surf and ice cream shop year round.

### Recommendations for Additional Queries
- I would recommend doing a similar analysis on the precipitation in June and December. Periods of high precipitation will likely have an impact on the success of a surf and ice cream shop, so it will be important to look at that data alongside the temperature data.
You can accomplish this analysis by running the following queries:
'''
june_date_str = "06"
session.query(Measurement.date, Measurement.prcp).filter(func.strftime("%m", Measurement.date) == june_date_str)

dec_date_str = "12"
session.query(Measurement.date, Measurement.prcp).filter(func.strftime("%m", Measurement.date) == dec_date_str)

'''
- I would also recommend identifying a temperature that may be too cold for ice cream and surfing (i.e., 60 degrees) and count how many days in each month fall below that temperature.
'''
june_date_str = "06"
session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%m", Measurement.date) == june_date_str).filter(Measurement.tobs <= "60")

dec_date_str = "12"
session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%m", Measurement.date) == dec_date_str).filter(Measurement.tobs <= "60")
'''