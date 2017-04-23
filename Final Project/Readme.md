
# INFO 7374 Data Analysis Using Python - Final Project

## IMDB API Data Analysis

![imdb_logo](https://cloud.githubusercontent.com/assets/25204050/25309959/a1cbd582-27a7-11e7-9f7f-7ac4840893a6.png)

- Data collected from TMDB API is used to collect data from the **IMDB Website**. 
- Data that has been taken from the IMDB API has been analyzed.
- One other datasets have been used. Crime in the United States for years 1975-2015 has been downloaded from the **FBI Gov website**. The websites for the datasets have been listed below.

## Data Formats

    1.TMDB API- https://api.themoviedb.org/3/movie/ - API Requests

    2.IMDB API - http://www.myapifilms.com/imdb/idIMDB/ - API Requests

    3.Crime data - https://ucr.fbi.gov/ - ZIP Files of temperature data

    

## Data Collection and Processing

### *TMDB API:*
   
        1. TMDB Movie ID
        2. TMDB Movie ID Details
       
### *IMDB API:*

        1. IMDB ID

## Fetching the Data 

### *Steps invloved in fetching data from TMDB API:*

        1. API requests are placed to the TMDB API based on the start Date,end Date and number of pages attributes to get the           TMDB Movie ID's
        2. API requests are placed to the TMDB API to get the IMDB MovieID based on the above collected TMDB movie ID's
        
### *Steps invloved in fetching data from IMDB API:*

        1. API requests are placed to the myapifilms API to get the IMDB movie details by passing the IMDB movie ID as 
        parameter
        
## Storing the Data

### *Steps involved in storing TMDB Movie ID's:*

        1. Loop through a range of 150 pages per startdate and enddata
        2. Hit the TMDB API which collects 100 TMDB movie ID's  
        2. Write the Data to a file named as 'startDate_endDate_datetimeofhit.json' extenstion file to the destination folder
        3. Files are stored in json format
        
### *Steps involved in storing IMDB Movie ID's Using TMDB Movie ID:*

        1. Read the files that are stored in above step and get the TMDB movie ID's
        2. Loop through the movie ID's and hit the TMDB API to get the IMDB movie ID's for each TMDB Movie ID
        3. Fetched Data is writen to a file named as 'tmdbID.json' to the destination folder
        4. Files are stored in json format
        
### *Steps involved in storing IMDB Movie Detailsfrom IMDB API:*

        1. Read the files that are stored in above step and get the IMDB movie ID's
        2. Loop through the IMDB movie ID's and hit the myapifilms API to get the movie details for each IMDB ID.
        3. Fetched Data is written to a file named as 'imdbID.json' to the destination folder
        4. Files are stored in json format

## Analysis Performed

## Anaysis 1:

## Number of movies releasing every year [2012-2015]

### *Analyzing the number of movies which are releasing per month for the years 2012-2015*
    
### Steps:

    1. Read the IMDB_Movies.csv file and get the input parameters
    2. Release Date is in YearMonthDate format so we are splitting the year and month from the parameter
    3. Assigning the year and month to a new columns for each movie
    4. Grouping the dataframe with Year and Month column and finding the frequency of movies released per month per year
    5. Filtering the grouped data to get the years 2012-2015
    6. Plotting the grouped bar graph using matplotlib library

### Outputs:

### *Table of values to plot*

![1 1_1](https://cloud.githubusercontent.com/assets/25204050/25309990/640a8af8-27a8-11e7-84fa-533a7f7df43f.JPG)

### *Number of movies released for per month for year 2012-2015*

![1 1_2](https://cloud.githubusercontent.com/assets/25204050/25310007/9e89b55a-27a8-11e7-8ec2-1525519bf4a2.JPG) 

### *Inference from above plot*

- The number of movies releasing is increasing for every month of the year 2014 but its decreasing for year 2015


## Good Movies Vs Bad Movies

## *Next we shall analyze how the ratings for the above released movies has been distributed*
    
### Steps:

    1. Filter the rating columns for all the years of each movie 
    2. Groubythe rating and claculating the frequency of each rating for all the years
    3. Removing the rating which are 0
    4. Plotting the histogram for the rating frequency using matplotlib.pyplot

### Outputs:

### *Table of values to plot*

![1 2_1](https://cloud.githubusercontent.com/assets/25204050/25310014/bda28d9a-27a8-11e7-84ec-024a5d1b9e18.JPG) 

### *Movies to watch and not to watch*

![1 2_2](https://cloud.githubusercontent.com/assets/25204050/25310021/dd7bdaea-27a8-11e7-8491-b4d1018d93b5.JPG)

### *Inference from above plot*

- The rating which are below 5 marked as red are poor movies not recommended to watch whereas above 7 marked as green are good movies to watch

## Top 3 movies from the released movies [2012-2015]

## *Finally we shall find out what are top 3 released movies with high IMDB rating for the year 2012-2015*

### Steps:

    1. Reading the year, urlposter, rating, title fields
    2. Grouping the movies based on rating and sorting it in descending order to get the top rated mmovies
    3. Display the top three rated movies
    4. Iterate through the movies and get the URL for posters of 3 movies*
    5. Request the url using urllib.request and download the poster to the destination folder
    6. Open the downloaded file and display the top three posters using IPython.display along with its movie details like           Rating, Release Year and Title

### Outputs:

### *Table of values*

![1 3_1](https://cloud.githubusercontent.com/assets/25204050/25310026/efb61504-27a8-11e7-8aca-75f4aae11987.JPG)

### *Top 3 Movies with High IMDB Rating for year 2012-2015 Posters*

![1 3_2](https://cloud.githubusercontent.com/assets/25204050/25310505/c6ebd31a-27b3-11e7-84b8-10f010b185c0.JPG)

![the day of the doctor17-04-22-10-10](https://cloud.githubusercontent.com/assets/25204050/25310035/1c7447be-27a9-11e7-86df-f81c59f17efd.jpg)

![1 3_2 1](https://cloud.githubusercontent.com/assets/25204050/25310038/32e1b61c-27a9-11e7-9d4d-0029efb64e87.JPG)

![mcbusted- tourplay17-04-22-10-10](https://cloud.githubusercontent.com/assets/25204050/25310040/3c937d94-27a9-11e7-9313-6d3dcc84f52f.jpg)

![1 3_2 2](https://cloud.githubusercontent.com/assets/25204050/25310045/4c66bc68-27a9-11e7-907f-09461ba11f5b.JPG)

![fuse17-04-22-10-10](https://cloud.githubusercontent.com/assets/25204050/25310048/5ad7d12e-27a9-11e7-99fa-4bdc00364ecc.jpg)

## Analysis 2:

## IMDB Rating Distribution for each country

## *Now let's analyse how many movies are being produced by countries across the world and what type of rating distribution is being followed by those movies per country*

### Steps:

    1. Read the Movies_Gross.csv file and get the parameters year, title, gross, rating for overall countries
    2. Filter the meaningful countries movie's.
    3. Filter the countries and the rating of each movie
    4. Group based on countries and plot the boxplot
    5. Boxplot is plotted using the seaborn library

### Outputs:

### *Table of values to plot*

![2_1 1](https://cloud.githubusercontent.com/assets/25204050/25310050/6f258784-27a9-11e7-929a-f7b41b079d9a.JPG)

### *Rating Distribution Worldwide*

![2_1 2](https://cloud.githubusercontent.com/assets/25204050/25310055/7c74580c-27a9-11e7-8dc5-d5d91d6b0df2.JPG)

### *Inference from above plot*

- We can infer that country USA and UK are producing more movies and their movies falls in all ranges of rating i.e from the lowest to highest 

## Profits of USA UK and Worldwide

## *Since USA and UK are producing more movies let's analyze how much profits they are have gained from the top 10 produced movies*

### Steps:

    1. Read the Movies_Gross.csv file and get the parameters title, gross, rating, country
    2. Group by movies countrywise and calculate the sum of the gross.
    3. Filter the movies for USA country and sort the gross in descending order
    4. Repeat the step 3 for county UK and other countries except USA and UK
    5. Plot a scatter plot with hover on points functionaly using mpld3 and matplotlib library

### Outputs:

### *Sample table of values to plot by each country*

![2_2 1](https://cloud.githubusercontent.com/assets/25204050/25310057/90dc1eec-27a9-11e7-8cc9-8bd0a452b607.JPG) 

### *USA, UK and Wordwide top profitted movie*

![2_2 2](https://cloud.githubusercontent.com/assets/25204050/25310061/9b556a9a-27a9-11e7-8432-2f680e24f9de.JPG)

![2_2 3](https://cloud.githubusercontent.com/assets/25204050/25310063/a5194e0c-27a9-11e7-9bf2-706b7db214ed.JPG)

![2_2 4](https://cloud.githubusercontent.com/assets/25204050/25310064/b2a7a97e-27a9-11e7-98fd-4ec13df2bd85.JPG)

### *Inference from above plot*

- We can infer that whatever the country is movie Titanic is in top 3 and has gained profit worldwide, irrespective of its native country and has attained immense popularity across the world

## *Movie Titanic Reached Highest Popularity Worldwide*

### Steps:

    1. Read the imdb_movies csv and get the title and urlposter
    2. Get the Tittanic movie and its poster URL.
    3. Request the url using urllib.request and download the poster to the destination folder
    5. Open the downloaded file and display the the poster using IPython.display library

### Outputs:

### *Table of values*

![2_2 5](https://cloud.githubusercontent.com/assets/25204050/25310069/d238eb40-27a9-11e7-88aa-1d85e38451d9.JPG)

### *Movie Titanic Gained More Popularity Worldwide Poster*

![titanic17-04-22-10-18](https://cloud.githubusercontent.com/assets/25204050/25310071/dcae6280-27a9-11e7-8f52-c01054b4d09d.jpg)

## Analysis 3:

## Genres Released for 2012-2015 years

## *Moving further lets's analyze the how many Crime, Mystery, Thriller, War and Action movies are released for 2012-2015 years*

### Steps:

    1. Read the imdb_movies.csv file and get the parameters genre,year
    2. Group by year and genre and calculate the number genres released per year
    3. Filter the movies for year 2012-2015
    4. Plot the pie chart for each year using the matplotlb library

### Outputs:

### *Sample Table of values to plot*

![3_1 1](https://cloud.githubusercontent.com/assets/25204050/25310073/f2e6a67a-27a9-11e7-9646-eb6d21da898d.JPG)

### *Crime, Mystery, Thriller, War and Action Genres for year 2012-2015*

![3_1 2](https://cloud.githubusercontent.com/assets/25204050/25310075/ff18854e-27a9-11e7-9d62-7ebdcd887910.JPG)

### *Inference from above plot*

-- We can infer that thriller is the highest genre being released and we can also infer that genre crime is increasing and decreasing and then increasing again, on the whole these strong genres entertains the public with more of voilence scenes


## *So let's analyse the population of the USA*

### Steps:

    1. Read the crime data .csv file and get the parameters state, year,total population
    2. Group by state and calculate the total population per year
    3. Filter the year 2012-2015 population.
    4. Finding the density of population for just one year 2015 using basemap library
    5. A scatter plot is plotted to display the increase in population from 2012-2015
    

### Outputs:

### *Table of values to plot*

1. USA Population Table for year 2015

![3_2 1](https://cloud.githubusercontent.com/assets/25204050/25310080/0974115c-27aa-11e7-824e-a522b01a3f68.JPG)

2. Increase in population 2012-2015

![3_2 2](https://cloud.githubusercontent.com/assets/25204050/25310082/15a319c8-27aa-11e7-9c4b-eb072ebb37f8.JPG)

### *USA Population density for year 2015*

![3_2 3](https://cloud.githubusercontent.com/assets/25204050/25310084/21e1829c-27aa-11e7-8e54-4eb05daabd2d.JPG)

### *Increase in population of USA 2012-2015*

![3_2 4](https://cloud.githubusercontent.com/assets/25204050/25310088/381928e4-27aa-11e7-934e-2d6e4620d39d.JPG)

### *Inference from above plot*

- We can infer that the population of USA is increasing periodically for year 2012-2015

## Rate of crimes happening in years 2012-2015

## *Now let's analyse whether the rate of crimes in USA is decreasing or increasing irrespective of the increase in the population [2012-2015]*

### Steps:

    1. Read the crime data .csv file and get the parameters state,year,homcide, rape, robbery, voilent crimes
    2. Group by state and calculate the total crimes by summing all the crimes per state
    3. Filter the year 2012-2015 total crimes.
    4. Finding the density of crimes for just one year 2015 using basemap library
    5. A bar graph is plotted to display the increase in voilent crimes 2012-2015
    

### Outputs:

### *Table of values to plot*

1. USA Crime Table for year 2015

![3_3 1](https://cloud.githubusercontent.com/assets/25204050/25310095/643b90ce-27aa-11e7-847d-a2b0f7f058f2.JPG)

2. Total crimes by category for year 2012-2015

![3_3 3](https://cloud.githubusercontent.com/assets/25204050/25310098/70102a68-27aa-11e7-897e-67e8236bda3b.JPG)

### *USA Crime density for year 2015*

![3_3 2](https://cloud.githubusercontent.com/assets/25204050/25310101/7db7f1aa-27aa-11e7-9a34-b1f3a76b708d.JPG)

### *Number of crimes by category [2012-2015]*

![3_3 4](https://cloud.githubusercontent.com/assets/25204050/25310104/876aa4f4-27aa-11e7-9eec-f0e585be11ee.JPG)

### *Inference from above plot*

- We can infer that the though the population of USA is increasing, the crime rates of some category is decreased but the voilent crimes are in its peak for all the 4 years. Hence the crimes are not getting decreased in USA

## Influence of Movies on the increase of voilent crimes in the USA

## *Since the voilent crimes have not decreased for any year let's analyse whether the movies have any influence on these voilent crimes.*

### Steps:

    1. Get the yearwise genre count and select oly the crime count for 4 years 
    2. select the voilent crimes count of the crime data for 4 years
    4. Plot the line graph for each year using the matplotlb library

### Outputs:

### *Sample Table of values to plot*

![3_4 1](https://cloud.githubusercontent.com/assets/25204050/25310108/9927ceec-27aa-11e7-8ff6-4dd8a192dd82.JPG) 

### *Influence of movies on Crimes [2012-2015]*

![3_4 2](https://cloud.githubusercontent.com/assets/25204050/25310110/a19c5d86-27aa-11e7-8573-31386b4bed2a.JPG)

### *Inference from above plot*

- We can infer that though the movies entertain public with voilent scenes the society is not getting affected with it, they just watch movies for entertainment and being matured enough in real world. Hence movies doesn't have any influence on Crime rate 
