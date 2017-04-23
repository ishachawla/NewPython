                                                 #H1 GLOBAL EARTH TEMPERATURE DATA

Considering some 200 odd years of data which contains Average Temperature and Average Temperature Uncertainty along with the countries and dates it was recorded in.

#  ANALYSIS 1
Using Seaborn to plot all the temperatures and temperature uncertainties are plotted in the graph.

![tempdist](https://cloud.githubusercontent.com/assets/13572497/25310552/9e0b0ce4-27b4-11e7-9a36-9b7fe11c5a6c.png)

This figure shows the distribution of data over the course of time and how has it increased and decreased. To get a better idea about the Growth/Decrease Rate of Temperature, a slice of the entire data i.e from 2000-2013 is considered and then for every consecutive year, we find the rate of increase/decrease in temperature.

                                     FormulaUsed= ((CurrentYear-PastYear)/PastYear)*100


# **ANALYSIS 2**

This time the main aim is to determine that what is the relation between the Average Temperature and the months.
The process of Regression is mostly used for this to try and establish a relation.
Here, the months(x) are the independent variable whereas the average temperature(y) are the dependent variables.

![avgtemp](https://cloud.githubusercontent.com/assets/13572497/25310576/837afa32-27b5-11e7-8f66-0f5ba38dc141.png)

This is a scatter plot of the average temperature and average temperature uncertainty over the past 200 months.
Now we use the polyfit function to identify a relationship between x and y.

### Relation b/w Months and Average Temperature:
                    y=0.0468826*x + 25.274388724
                    y=mx + c
![avgtempregression](https://cloud.githubusercontent.com/assets/13572497/25310579/989893ac-27b5-11e7-8b1e-aa11a27d305c.png)

We, repeat the same process for Average Temperature Uncertainty and aim to find an equation for that.
Relation b/w Months and Average Temperature Uncertainty:
                   y=-0.00072124*x + 0.19090129
                    y=mx + c

![avgtempuncertainregression](https://cloud.githubusercontent.com/assets/13572497/25310583/afa424ee-27b5-11e7-8a60-c1be81c8bd99.png)

# **ANALYSIS 3**

In this analysis, we consider countries of very varied temperature and try to study the patterns between them. Our main aim is to do some Exploratory Data Analysis and see and visualize that how much values can change over a certain location.
For our first Exploratory Analysis lets consider USA and Brazil.
When we try to plot a graph it looks something like this.

![usbrazil](https://cloud.githubusercontent.com/assets/13572497/25310587/c70c0502-27b5-11e7-80fe-977d43d8f7cd.png)

We see that over the course of over a 100 years US and Brazil have never shared the same temperature due to their varied landscape.
One look at this graph and we can see that it is a scattered chart whose value is increasing and decreasing constantly. But when we consider a smaller slice of data i.e 10 years we see a difference in their representation.

![normaldistribution](https://cloud.githubusercontent.com/assets/13572497/25310588/da9e5cbe-27b5-11e7-9174-b8374119b497.png)

We see when we slice the data both US and Brazil show Normal Distribution the only significant difference being that the US has fewer values whereas Brazil has a steeper curve.

Now, we consider one country from each continent and try to plot a graph of their temperatures. This time rather than using matplotlib and Seaborn we use Bokeh to plot a graph.

![continents](https://cloud.githubusercontent.com/assets/13572497/25310592/ed49a7d8-27b5-11e7-9210-bef69e41810a.png)


After this, we try to plot a graph for US and Canada and then Canada and Denmark since all of these countries are quite cold and there is a high possibility of them having similar trends in temperature.

![uscanada](https://cloud.githubusercontent.com/assets/13572497/25310593/fc6c931a-27b5-11e7-8478-2c6cf7616d4f.png)

![denmarkcanada](https://cloud.githubusercontent.com/assets/13572497/25310599/0ec4ca0a-27b6-11e7-9f82-670b6e74dc8a.png)

US is quite warmer when compared to Canada and Denmark has substantially low temperatures when compared to Canada

Now we try to plot Greenland's Temperature with Denmark

![greelanddenmark](https://cloud.githubusercontent.com/assets/13572497/25310600/1ec364fc-27b6-11e7-9e56-551f91a7413a.png)

We see that Greenland and Denmark follow more or less the same trend in temperatures.

# **ANALYSIS 4**

This time we just take into consideration America's Data and divide it into the four seasons according to the month(Spring, Summer, Autumn, Winter) and then plot all the data in four subplots

![seasondistribution](https://cloud.githubusercontent.com/assets/13572497/25310605/3093d216-27b6-11e7-9bf3-73efe90cc86e.png)

Now we use this data to plot it using Seaborn and then we will be able to analyze better that how the temperature varies with the weather.

![avgtempdistribution](https://cloud.githubusercontent.com/assets/13572497/25310607/3efe243c-27b6-11e7-917c-a8fee58fd30a.png)

# **ANALYSIS 5**

Firstly we plot a horizontal bar chart showing all the countries in decreasing order of their temperatures.

![avgtempcountry](https://cloud.githubusercontent.com/assets/13572497/25310608/5232891c-27b6-11e7-81f4-985e7fb8c9c6.png)

After this we make csv files for the top 10 coldest and top 10 warmest countries by every year and save them separately to give us a better idea about the temperature changes that we see over the time.
