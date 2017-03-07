
# Question 1 : 

# Using Enron data-set, perform 3 analysis.

## Introduction:

- Enron Corp. is a company that reached dramatic heights, only to face a dizzying collapse.
  The story ends with the bankruptcy of one of America's largest corporations. Enron's collapse affected the lives of thousands   of employees and shook Wall Street to its core. At Enron's peak, its shares were worth 90.75 dollar, but after the company declared   bankruptcy on December 2, 2001, they plummeted to 0.67 dollar by January 2002. To this day, many wonder how such a powerful business   disintegrated almost overnight and how it managed to fool the regulators with fake, off-the-books corporations for so long.



## Intial Data analysis:
- The given data set contains nearly 150 users of the top executives of the company
- The dataset contains more than 5 million files
- The data is stored in a folder structure as the persons name and their respective email system folders like inbox,sent,deleted_items

## Process of Data Storage:
- The enron dataset is downloaded from this "CMU Enron data 1.82 GB tgz file"
- The data is extracted and stored in the desired folder
- The data is unziped to find the folder structure of data
 

# Analysis 1:

# Finding the number of emails exchanged between the employees per year, to find which year the mail communication was happened.


## Process involved:
- Traversing through the folders of each employee, and checking the sent emails of the employee 

- For each sent folder of the mail, the date of the email is checked 

- Year and the month of the date is split using datetime package

- Calculating the frequency of the mails occuring in each month and incrementing the value if month already exists, otherwise a new month is added to the dictionary as key and assigning the value as frequency of mails.

- Calculating the complete count of the mails occured in every year and that count is added to the dictionary

- A new dictionary is created and each unique year is added as the key

- Finally, the each month and its frequency  which is calculated in the previous steps is assigned as the value of the each unique year



## Code Result:
!['yearly mails'](Question 1/Analysis 1/q1_a1_first.jpg)

## Representation Result:

- The year and the email frequency is exported as a csv file to make a further analysis on the data. The output looks like below
!['yearly mails'](Question 1/Analysis 1/Q1_A1_Result.jpg)

## Inference:
- From the above Result we can conclude that during the year 2000 and 2001 highest email communication has happened

    - for 2000 year, months 6 to 12 has highest mails( calculated through implementation by following above process steps)
    
    - for 2001 year, months 1 to 5 has highest mails(calculated through implementation by following above process steps)

# Analysis 2

# With the above inference we can proceed further by analysising who are the persons involved in those highest mails communication for the year 2000 and 2001

## Process:
- Calculating the months which has the highest mails and concentrating on those months of the years to check the persons involved

!['yearly mails'](OutputFiles/q1_a2_first.jpg)

- Iterating through the mails and finding the 'Date' tag of the email

- Spliting the date to year,month and date and assigned to respective varaibles

- A condition is checked whether the year is 2000 0r 2001 and the month of the incoming email is equal to any one of the months mention in above image.

- If the condition is true, the 'From' and 'To' tag of the email is fetched and assigned to the respective varaibles

- Another condition check is made if the 'to' is empty and whether it contains more than one 'to' addresses

- If the 'To' contains more than one mail id, the emails are split by '\n' in original mail, so we are replacing the '\n' with empty string so that the whole to list becomes on string sperated by commas.

- Next we are extracting each of 'to' addresses by stripping with ',' and finding the frequency of the 'to' addrtesses

- A dictionary is created with unique 'to' address and its frequency of each of the 'From' address name.

- Finally to a new dictionary the unique 'From' address person is added with the value as the dictionary of a unique 'to' addresses with its frequency and the frequency whole mails sent by each person is also added to the dictionary

- From this we can get the counts of all the mails sent by individual person who belong to enron


## Results of the Analysis:

!['yearly mails'](Question 1/Analysis 2/q1_a2_Second.jpg)

## Inferences can be made:

- We analysed that Mann Kay and Vince Kaaminski has communicated more

    - Mann Kay is the "President & Chief Executive Officer at Noble Environmental Power LLC" who was convicted and involved in         the enron scandal
            " She is a global natural gas worker prior and she invested in supplying the gas of the state government ilegally which was to the enron company. Due to which Utilities try to keep customers' bills low by buying natural gas at cheaper prices in the summer, when it is in lower demand. They then release the gas in the winter, when consumers need it to heat their homes.
              Thus increasing the cost of the electricity during the winter which was a difficulty for the public. So she is the key person in the Scandal."
    
    - Vince Kaaminski is the "Managing Director for Research at the failed energy trading corporation Enron until 2002" who           was also involved in scandal who belongs to poland.
    
    - Below is the piece of news publication on vince:
    
            "A former Enron Corp. risk manager testified Tuesday that he was pushed out of a key assignment at the energy trading company because he objected to what he believed were questionable financial maneuverings
            
            Wincenty "Vince" Kaminski said Jeffrey K. Skilling, then Enron's president, called him in July 1999 to say that Kaminski and his team of analysts were being transferred. The call came a month after Kaminski had raised objections to LJM, an off-the-books partnership created by then-Chief Financial Officer Andrew S. Fastow to provide financial insurance for an important Enron investment.

            The testimony came in the fraud and conspiracy trial of Skilling and former Enron Chairman Kenneth L. Lay. The charges grew out of a federal probe sparked by Enron's 2001 collapse. Lay, 63, and Skilling, 52, face decades in prison if convicted.

            The jury also heard from a former Enron pipeline worker who lost most of his life savings when the company's stock became worthless"
    
- Hence this analysis proves that we investigated and found out the top 2 'KEY' person involved in this whole scandal

# Analysis 3

# Finally lets analyse what the two key people were speaking about in those mails 

## TOPIC MODELLING USING LATENT DIRICHLET ALGORITH(LDA) 

- The content of the emails are analysed further by understaning and preprocessing the data before implementing the topic modelling on it to find the key topics what the two persons were speaking about

- The text analysis is made on the subject of the emails

- The subject of the email is appended to the dictionary for both the person kay and mann by iterating through the mails and statisfying the year, month condition as specified above

- So the data cleaning is done by the following steps:

    - First the data is converted to lower 
    
    - Next the NLTK package, "tokenizer" is used tokenize the raw data to words.
                tokens = tokenizer.tokenize(tagRemoval)
                
    - Next the frequent patterns like FWD, RE.. is removed by Regular Expression
    
    - All the numbers are removed form the texts and all the punctuations are also removed
    
    - The Stopwords are removed by using "en_stop" package
    
    - Finally the words are lemmatized using the NLTK.stem, WordNetLemmatizer
                wordnet_lemmatizer = WordNetLemmatizer()

- Turn our tokenized documents into a id <-> term dictionary which done using below snippet
                dictionary = corpora.Dictionary(texts)
- Convert tokenized documents into a document-term matrix
                corpus = [dictionary.doc2bow(text) for text in texts]
- LDA algorithm is applied finally to the corpus to get the topics 5 topics of 15 words using the "Gensim" Package
                ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary)
    

## Results

- The topics which were spoken by vince kaminski is as follows

!['yearly mails'](Question 1/Analysis 3/topic_vince.jpg)


- From the above image the different topics infers conclusions like below

     - Topic 1 : Rice university of vince, his researches and going on vacation from polan it means
     
     - Topic 2 : It is mostly about conversation they are having and arranging meetings for the scandal issue
     
     - Topic 3 : This topic gives hints like he is travelling to california between capital of Poland where he belongs to (dyplomowas capital of poland) for the management purpose
     
     - Topic 4 : This is about generating the weekly report on enron to know to keep track of the risk 
     
     - Topic 5 : This is meaning something core business related where the electricity bill raising and power from houston proves he his comminication with Mann Kay about the scandal

- The topics which were spoken by mann kay is as follows

!['yearly mails'](Question 1/Analysis 3/topics_mann.jpg)

- From the above image the different topics infers conclusions like below

     - Topic 1 : Speaking more about marketing and agreement on rotation
     
     - Topic 2 : It is mostly the discussion they had previously or in past conversion recalling what can be done
     
     - Topic 3 : This is meaning something core business related executing some agreement with the enron and natural gas power
     
     - Topic 4 : Keywords speaking more about vacation spots and there sceret meeting
     
     - Topic 5 : This is about business related issue purchasing and some illegal transactions are happenening

- Hence from the above topics spoken by both the people this proves that they are involved in the enron scandal.

# Question 2 

# Use NYT API to collect NYT data. Perform 3 analysis on the collected data.

## Intial Data analysis:

- There are many API in the NYT times. The data from the nyt times is generated by the API key 

- We can select any API which is well suited for the analysis

# Process of Data Storage:

- The data is fetched from the API by writing the code to dump the data as json file 

- The is fetched from the nytimes by passing the api key, parameters that are required by the API to the link 

- By doing so the data is fetched as a response to us and the data in stored in the specified location of out file system as json file

# Analysis 1 

# Using Article Search API, find during which year there was high rate of voilent crime happenings in the USA

## Process involved:

- The Crime related data is downloaded by the implemented data fetching code

- A list of negative words are created like gun,terrorism,terrorist,rape..

- Iterate through the files of the the crime data

- The values of abstract, lead_paragrapgh, keywords are taken from the dictionary of the json file

- Next find whether there any words in the created negative wordlist is present of not in the json values

- If present the extract the year of the article through pub_date key of the dictionary and add to the new dictionary if the year is not alreday present

- If year is already present then the year value is incremented by 1

- The process is reapeted for all the files

- Finally we get the list of all the crimes happend in the year 2016,2015,2014

- The is represented in pie chart.

- The file extracted to the csv file to show the representation of crimes per year

## Results

!['yearly mails'](Question 2/Analysis 1/q2_a1.jpg)

!['yearly mails'](Question 2/Analysis 1/q2_a2.jpg)

## Inference:

- From the above pie chart it is very clear that during 2015 there were more of voilent crimes has occured like attacks, terrorism, rape compared to the previous year(2016)

- Thus it is infered that the during 2014 it was low and it got drastically increased in the year 2015. But in the previous year the rate of voilent crimes decreased

# Analysis 2:

# Analysing how the trend of sharing information has improved, using Most popular API

## Data collection:

- The data is collected my passing the parameters of section and period to the most popular search api learch

- Using the api key that is generated the data is dumped to the as a json file

## Process Involved:

- Iterate through the list of file that is downloaded from the api

- Iterate through the most shared files 

- From the files the date is fetched from the published date

- And the date is sperated as year month and date 

- If the month is equal to 2(Feb) then the date of the file is added to the dictionary and the total_shares value is fetched from the tag of the dictionary and assigned as the value of the date.

- Above step reapeated for all files at the end the dictinary will have the unique dates and its total shares as the value

- Next Iterate through the most viwed files and store the files

- And follow the same steps mentioned above and get a dictionary with unique dates and it total views as the values

- Now the comparasion is made in the bar graph

## Results:
!['yearly mails'](Question 2/Analysis 2/q2_a3.jpg)


## Inference:

- The above graph proves that now a days people are not just viewing the news  or information they are just spreading the information also as the count of shares are higher than views.

- Due to the invention of technology and social networking the words are spreading fast thorugh out the worldwide. Thus proving the trend of sharing information has increased a lot. 

# Analysis 3

# Using the Article search API, track the popularity of football by comparing to baseball and basketball for the year 2013-2014 

## Process:

- The basketball files that is collected from the api search is iterated first

- Fetching the section name and subsection name of the article.

- Fetch the year of the article through the pub date and split the year to the date year and month

- If the section name is 'sports' and the subsection name is 'Pro basketball' then add the year to the dictionary and assign the counter

- Increment the counter of the value if the year is already otherwise add the new year as key

- Reapeat the same process for the baseball also

- Repeat the same process for the football also

- We get the dictionaries of all the unique years with there assigned counter.

- Plot the information in the multiple bar grapgh using matplotlib library

## Results:

!['yearly mails'](Question 2/Analysis 3/q2_a4.jpg)

## Inference

- From the above graph we conclude that the football sport is getting popular year by year compared to baseball, basketball

- Thus US is very famous in football sport.


```python

```
