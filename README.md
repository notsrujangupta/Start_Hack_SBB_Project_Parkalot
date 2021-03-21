# START HACK 2021 | Team Savantium | Case SBB | Project Parkalot

## Team 
### [Sehan Shetty](https://github.com/yttehs123)
MSc in geo - data sciences and remote sensing with a background in climate sciences and forestry | [LinkedIn]
### [Srujan Gupta](https://github.com/notsrujangupta) 
AI scientist with a bachelors in Mathematics | [LinkedIn]
### [Swapnil Dubey](https://github.com/patelviralb)
Data scientist with a double major in Electrical engineering and Astrophysics | [LinkedIn]

## Case Problem Statement
SBB is focusing their energy on increaasing efficiency and puntuality and are aiming to stay stay ahead of the environmental curve with technological innovations. In doing so they focus on rail strengths, good value for money for their customers and affordability for ordering parties. Their overlying goal being an attempt to simplify and personalise their products and services for customers in order to create a simple, personal and connected future for mobility. 

This brings us to the problem. One of the roadbumps along the path to a simple future is parking. SBB wants to be able to forecast parking space availability for SBB train station parking lots in order to inform customers ahead of time if whether a parking lot will have spaces available or not. 

A side challenge, along with forecasting, was to identify a few parking spots where SBB can record addictional parking data. SBB does nto want to install hardware at every location in order to save costs but they also want just about enough locations that help accurately depict the traffic conditions of Switzerland.


## Our appraoch

We realised that solving for forecasting falls directly in line with SBB's vision of a simple, personalised and connected future. By providing forecasts on their app for parking spots, customers can easily plan ahead of time which parking lots they want to park at, what time they need to arrive at a parking lot in order to to easily get a space, etc. This simplifies for the customer by helping customers make better informed decisions, it perosnalises the experience for each user as they can conveniently pick from hours in advance upto days in advance to check if a parking spot might be avaialble avaiable and all of this is achieved while making their users feel more connected to SBB.

We had to make a decision early on. We decided to focus all our energy on a technical solution and not design a UI. Reason being that SBB first and foremost wants to ensure that accurate forecasts are made. Poorly made forecasts can cause customers to loose trust in a company. Nobody trusts a weahter channel that tells you it's going to snow in the middle of a tropical summer. While humans might never make such a blunderous error, a poorly designed forecasting model can definetely make such an error. We want to avoid extreme scenarios where SBB looses customers because the forecast mentioned that all parking spots might be full while most turned out to be actually empty and the opposite where customers are disatisfied when they arrive at an occupied parking spot when the forecst was actualy in their favor.

We also are aware that SBB already has a functioning app with a parking feature in it. Therefore, rather than designing a UI for them, which they already seem to have done a good job at, we want to provide them with an as accurate as possible forecasting model which can directly be integraated into their app.

We analysed the data given to us, performing as many statistical and validation tests on them as possible in order to fully realise the data's potential. This led us to using parking sales, weather data and parking lot occupancy data to create models that accounts for multiple variables. We then tested several forecasting models like...Results being....This model showed to be the most promising however the data we had was limiting. As SBB aqcuires more data with time, a more complex model can be  designed in the future that creates much more accurate forecasts. 

Furthermore, with the geospatial technical expertise in our team, we were also able to tackle the side challenge of identifying ideal locations for SBB to install their hardware at. Using Kmeans on passenger traffic data and the weather data, we were able to spatially identify 50 locations out of all the parking lots where SBB can install their hardware at in order to gain data that will help accurately represent the parking conditions for the whole of Switzerland.

This map shows the spread of the 50 chosen locations for aquiring traffic data and are highlighted in orange. 
Read more about our solution in depth in the next section.
## Our solutions in depth

### Forecasting Model

### Hardware Location Identification

### Scalable Ideas
