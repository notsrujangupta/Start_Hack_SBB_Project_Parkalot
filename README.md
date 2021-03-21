# START HACK 2021 | Team Savantium | Case SBB | Project Parkalot

## Team 
### [Sehan Shetty](https://github.com/yttehs123)
MSc in geo - data sciences and remote sensing with a background in climate sciences and forestry | [LinkedIn](https://www.linkedin.com/in/sehan-shetty/)
### [Srujan Gupta](https://github.com/notsrujangupta) 
AI scientist with a bachelors in Mathematics and PGP in AI/ML | [LinkedIn](https://www.linkedin.com/in/notsrujangupta)
### [Swapnil Dubey](https://github.com/swapdub)
Data scientist with a double major in Electrical engineering and Astrophysics | [LinkedIn](https://www.linkedin.com/in/swapnil-dubey/)

## Case Problem Statement
SBB is focusing their energy on increasing efficiency and puntuality and are aiming to stay ahead of the environmental curve with technological innovations. In doing so they focus on rail strengths, good value for money for their customers and affordability for ordering parties. Their overlying goal being an attempt to simplify and personalise their products and services for customers in order to create a simple, personal and connected future for mobility. 

This brings us to the problem. One of the roadbumps along the path to a simple future is parking. SBB wants to be able to forecast parking space availability for SBB train station parking lots in order to inform customers ahead of time if whether a parking lot will have spaces available or not. 

A side challenge, along with forecasting, was to identify a few parking spots where SBB can record additional parking data. SBB does not want to install hardware at every location in order to save costs but they also want just about enough locations that help accurately depict the traffic conditions of Switzerland.


## Our appraoch

We realised that solving for forecasting falls directly in line with SBB's vision of a simple, personalised and connected future. By providing forecasts on their app for parking spots, customers can easily plan ahead of time which parking lots they want to park at, what time they need to arrive at a parking lot in order to to easily get a space, etc. This simplifies for the customer by helping customers make better informed decisions, it personalizes the experience for each user as they can conveniently pick from hours in advance upto days in advance to check if a parking spot might be available and all of this is achieved while making their users feel more connected to SBB.

We had to make a decision early on. We decided to focus all our energy on a technical solution and not design a UI. Reason being that SBB first and foremost wants to ensure that accurate forecasts are made. Poorly made forecasts can cause customers to lose trust in a company. Nobody trusts a weather channel that tells you it's going to snow in the middle of a tropical summer. While humans might never make such a blunderous error, a poorly designed forecasting model can definitely make such an error. We want to avoid extreme scenarios where SBB loses customers because the forecast mentioned that all parking spots might be full while most turned out to be actually empty and the opposite where customers are dissatisfied when they arrive at an occupied parking spot when the forecast was actually in their favor.

We also are aware that SBB already has a functioning app with a parking feature in it. Therefore, rather than designing a UI for them, which they already seem to have done a good job at, we want to provide them with an as accurate as possible forecasting model which can directly be integrated into their app.

We analysed the data given to us, performing as many statistical and validation tests on them as possible in order to fully realise the data's potential. This led us to using parking sales, weather data and parking lot occupancy data to create models that account for multiple variables. We then tested several forecasting models like VAR, LSTMs, and even much more complex solutions like a Multivariate AutoEncoder. Out of the models we tested, VAR ended up being nigh useless because the data was indeed time dependent, Multivariate AutoEncoder was far too complex and ended up overfitting the training data, but the relatively simple 50 unit LSTM worked relatively well. This model showed to be the most promising however the data we had was limiting. As SBB acquires more data with time, a more sophisticated model can be  designed in the future that creates much more accurate forecasts.

Furthermore, with the geospatial technical expertise in our team, we were also able to tackle the side challenge of identifying ideal locations for SBB to install their hardware at. Using K Means on passenger traffic data and the weather data, we were able to spatially identify 50 locations out of all the parking lots where SBB can install their hardware in order to gain data that will help accurately represent the parking conditions for the whole of Switzerland.

<img src="/50LocationSpread.png">
This map shows the spread of the 50 chosen locations for acquiring traffic data and are highlighted in lightblue. 

## Our solutions in depth

### Forecasting Model
Since SBB has so far been able to put sensors in 2 stations, "Burgdorf" and "Rapperswil," we were limited to tangible parking spot fill data from both of them. Of the two, Rapperswil's data was daily as opposed to hourly, and since we intended to give a proof of concept of our models on an hourly basis (this can get even more precise, allowing for computation time, upto second-by-second results!), we ignored Rapperswil altogether and stuck to Burgdorf because it gave information on all the entries and exits of vehicles from Jan 1 2021 to Feb 28 2021.

Using that data, we had information on the vehicles that were present within the parking space (upto specific parking spots) for every single second. To fit it within the hackathon's timings, we chose to make hourly data, and generated a dataset for the number of vehicles present in burgdorf at every given hour from 0000 hours Jan 1 2021 to 2359 hours Feb 28 2021.

We did the same thing for sales data. The historical and 2018 datasets for sales had no entries that ended after Jan 1 2021, so we chose to ignore them altogether. From the backend and App sales that ended in 2021, we first did further statistical analysis to figure out whether the sales data is truly usable. There were 7000+ entries of vehicles entering the parking lot but only 397 ticket instances after all! After some rough estimation and thorough data extraction, we realised that while the (rough) average duration of each vehicle in burgdorf was 3.81 days but the average duration of a ticket was 6.22 days. After consulting with a fwe experts from SBB, we came to the conclusion that this is perfectly reasonable and we can move on with the data as being complete enough to not adversely affect the model. This was a very real fear because a nontrivial chunk of sales data is lost in parking meters and other such thigns, making it harder to track it precisely.

To retrieve weather data (meteodata) for Burgdorf, we need to use an API from “https://weather-int.api.sbb.ch/”, also known as the API’s base URL. After receiving the authentication token by using credentials provided by our case sponsors, we are able to retrieve data as per our requirements. First select parameters that you are interested in retrieving. Add them to the end of the base URL following the rules and convention given in the Meteomatics documentation. The time period for which to retrieve the data. For our use, we have chosen hourly data for Temperature above 2 meters, Precipitation and Snowfall. This is followed by the location in Latitude and Longitude coordinates. This gives us our final link to call our dataset in csv as:
https://weather-int.api.sbb.ch/2021-01-01T00:00:00.000+05:30--2021-02-28T23:59:59.000+05:30:PT1H/t_2m:C,precip_1h:mm,fresh_snow_1h:cm/47.0607007264,7.62169447355/csv


For the model, our preferred one seemed to be the 50 unit LSTM. In a heavily right skewed distribution with mean 24 and max possible occupancy of 155, our mean absolute error was just 12, and given the dataset's length and downsampling to hourly data (as opposed to second-basis), this is extremely powerful. As we're able to work on it in the future, we will certainly be able to create something much mroe sophisticated, powerful, and useful for SBB.

### Hardware Location Identification
In order to find the best spatial distribution of parking lots across Switzerland which also accurately portray parking lot information across the country, we decided to perform a Kmeans analysis on the passenger traffic data provided by SBB. It contained a spatial attribute with coordinates provided for each station/ parking lot and also provided traffic information for the whole week, weekdays and weekends. This allowed us to perform a multivariate Kmeans analysis on the data. the result was as displayed in the mapa above. 

The analysis resulted in 5 clusters. This told us that Switzerland has upto 5 categories of traffic data when it comes to passengers. If SBB wants to collect data that represents parking information for switzerland, they need to appropriately aquire information from stations thatthat are distributed across all 5 categories. To make things a clear, one station can only appear in one category. We then identified 10 different stations within each category by finding data points closest ot the centers of the clusters formed within the kmeans analysis. The list of recommended stations are provided in the hardware location folder as an image file named recommendations.

<img src="/Kmeans_5_Clusters.png">
This image shows the clusters of the data. There appear to be 6 clusters due to the image being displayed in 2D. the Kmeans analysis created a 3D clustering which when viewed in 2D appears to form 6 clusters instead of 5.



### Scalable Ideas
1. Our clustering method will very easily get much more sophisticated the moment we're able to have access to more computational time and
2. Spot specific information - Customers love getting the aisle seat in planes. If the data ssuggests it, we can implement a spot specific predictor so that the customer can not only judge whether there will be a spot available for them at the parking lot, but whether the specific spot that they want is available.
3. Routing - The current solution we have made will help SBB place sensors at appropriate parking lots to effectively gain data for all 590 of them, but once the system is online, we will also be able to help SBB route the traffic to other parking spots the customers may want to access in case the one the one they are looking for is closed. This offers a very simple yet effective revenue strategy: that of making people feel increasingly reliant on SBB parking spots when people want to be in an area for any reason, thus allowing SBB to get revenue form non SBB parking lots to let customers be routed to those other parking lots. It can help SBB become a sort of umbrella organisation even within the parking lot infrastructure of Switzerland, actively impacting people's choices rather than passively providing information.
spot specific information (spot 1/spot 2, kinda like plane seats)
