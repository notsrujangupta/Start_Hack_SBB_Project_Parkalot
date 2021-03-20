To go with our plan of using meteo data, sales data, and UNIX time to get appropriate expected values for spots being used at burgdorf, we cleaned all the sales data from the files provided and found that despite there being 7000+ data points for spots used (not more than 80 concurrent) in the burgdorf parking lot, there were only 397 total tickets sold whose ending dates were within 2021. After talking to representatives in SBB, the sales data is clearly incorrect enough for its use to not be warranted within the premise of our project. So for now, we intend to ignore the sales data altogether.
As a form of double checking, after removing unnecessary timings from data after feb 28 2021 and before jan 1 2021, we got the following information on the data of the duration of the tickets sold for burgdorf (on the app and otherwise): 

Output: (in days)
 mean       6.225888
 std.dev    14.886655
 min        0.041667
 25%        0.166667
 50%        0.333333
 75%        1.000000
 max       58.000000

~Data from "Sales Testing.py"

Describe() for vehicular time spent in burgdorf:
mean        0.202188
std.dev     0.742918
min         0.000706
25%         0.004583
50%         0.071817
75%         0.339334
max        43.280625

~Data from "Sales Testing.py"


The total number of vehicles that entered burgdorf during this time period was 7148. The average number of times each vehicle enters should be number of vehicles entering/number of tickets in the timeframe = 7148/379 = 18.86
The rough average amount of time spent (in days) by each such vehicle should be number of times each vehicle enters* average amount of time each entry lasts = 3.81.

However, the mean number of days each ticket last was 6.23 days, so it is a fair ballpark figure to use despite the odd values.

