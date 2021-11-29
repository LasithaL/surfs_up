# Surf's Up
An Analysis of a Business Opportunity

## Overview
The research company is tasked with finding general weather data in preparation of a business venture of a Surf Shop that rents out surfing equipment whilst serving Ice Cream to the tourists.

Pandas, SQLAlchemy and Numpy was used throughout the analysis.

## Process
Weather data was provided in a sqlite database file to be analyzed. The data was collected via nine stations spread throughout the Hawaiian Island of Oahu. The focus dataset was selected to be the June and December weather data. An analysis of the June and Weather data was performed to understand weather effects on the business.

## Results
The analysis of the weather data for June revealed a total of 1700 measurements with a mean temperature of 74.9F and a standard deviation of 3.26F. Furthermore, the data show a minimum temperature of 64.0F and a maximum of 85.0F.  The quartiles for the June dataset fell at 73.0F, 75.0F, and 77.0F for 25%, 50%, and 75% respectively.

In comparison the December data suggests a total of 1517 data points with an average temperature of 71.0F and a standard deviation of 3.75F. Also, the December data has a minimum temperature of 56.0F and a maximum of 83.0F. The quartiles for the December fell at 69.0F, 71.0F, and 74.0F for the 25%, 50% and 75% respectively.

June Data

![June_Temperature_Summary_Data](june_temp_stats.PNG)

December Data

![December_Temperature_Summary_Data](dec_temp_stats.PNG)

The differences found in the June and December temperature data are recorded below.
- The first difference that I see is that there are approximately 200 more data points in the June data set over December. In knowing that December has more days in the month that June, I would have expected to see more data points in the December dataset. This may warrant a closer look at the data collection process.
- The temperature range (Max - Min) in June was 21.0F in comparison to 27.0F for December. This can be attributed to the low temperature in June being 64.0F compared to 56.0F for December.
- The data also show that on an average the June temperatures were approximately 4F higher than December.
- Another difference is the standard deviation. June temperature standard deviation was calculated to be 3.26F in comparison to the 3.75F in December.

## Summary
As described above there is a seasonal dependency in the temperature of Oahu when comparing the June and December data. There may be other factors that should be taken into consideration. Some possible factors are listed below.

An area of further analysis would be the dependency of the temperature across the nine stations to see if the temperature is uniform across the stations for any given period, i.e.: June vs. December.

Another area would be to look at the precipitation data recorded at the stations for the months of June and December. This data may provide more insight to the possible locations of the Surf Shop.