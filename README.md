# New-York-City-Dog-Bites
#### This is a link to my report on New York Dog Bites! -> [Dashboard](https://public.tableau.com/views/NewYorkCityDogBites/NYCDogBites?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
#### If you would like to like to interact with the dataset please click the link, otherwise I have made a pdf copy within this repositry as a pdf to those who would prefer to view as it is.
#### Link to the original dataset -> [Original Dataset](https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg)

## Background 
Project Overview: Enhancing Dog Ownership Decisions through Data Analysis

As someone who has transformed a past fear of dogs into a profound passion for them, I now aim to leverage my enthusiasm to assist others in making informed decisions about dog ownership. This project is driven by my personal journey from a fearful encounter with a tiny, fluffy puppy to a deep love for dogs as perfect companions.

I am developing a comprehensive data analysis project focused on understanding the factors contributing to dog bite incidents. By examining various datasets, I intend to uncover key insights into the circumstances and characteristics associated with dog bites. The ultimate goal is to create an interactive dashboard that provides valuable information to prospective dog owners, enabling them to make well-informed decisions before adopting or purchasing a dog.

This dashboard will not only highlight top biters but also offer actionable insights for evaluating potential canine companions, ensuring a safer and more informed experience for future dog owners.

## Plan
**Objective:** Assist prospective dog owners about dog breeds and ages by analyzing dog bite incident data from New York City Open Data.
### **Phases:**
**Data Acquisition:** - Download and import data into Google Sheets for initial review <br>
**Data Cleaning and Preprocessing:** - Address missing values, duplicate values, incorrect values and standardize formats in Python.<br>
**Data Analysis:** - Conduct exploratory data analysis using Python (Pandas, numpy, Seaborn, Matplotlib)
                   - Create visualizations to highlight key insights<br>
**Tools and Technologies:** 
**Languages:** Python, Google Sheets<br>
**Libraries:** Pandas, NumPy, Seaborn, Matplotlib, datetime<br>
**Data Management:** Google Sheets<br>
**Visualization:** Seaborn, Matplotlib, Looker Studio<br>
**Expected Outcome:**
- Analysis of Dog Bite Incidents in Python with Insights<br>
- Visual Interactive Dashboard<br>
- Data-driven recommendations for dog owners<br>

## Analyze 
In the analyze phase we want to make sense of the data we have given and begin cleaning up the file in order for us to extract valuable information about dog bites. This includes import necessary packages needed for our analysis. In this case we needed pandas, numpy, matplotlib, seaborn, and datetime. Using pandas we imported our dataset and looked at the first 10 rows. We then moved forward with doing the following; gathered info and descriptive statistics using pandas built in functions .info() and .describe(). 
![Screenshot 2024-08-05 134843](https://github.com/user-attachments/assets/a93a7472-d938-418c-ba41-ce4e741141c4) <br>
***From the descriptive statistics, we observed the following:***
- **September 16th, 2017**, had the most dog bites on a single day.
- **Pit Bulls** were the top breed involved in bites.
- **Queens** had the highest frequency of dog bites among all boroughs.
  
## Data Cleaning 
From the two screenshots we see there are a number of object variable types. Object data types are stored as text(str) and these can take a lot of memory. To resolve this we can change these columns to category as they can be considered as categories as this will save up a lot of space. We can also change the `DateOfBite` variable to be datetime value so we can further manipulate that column to extract the month as well as the year to get deeper analysis. Also lets delete the `Species` column as they are all dogs. Lets implement those changes into our dataset. 
![Screenshot 2024-08-05 135656](https://github.com/user-attachments/assets/0ed634ed-0a3d-4fb2-a459-cd439ed26f24)
![image](https://github.com/user-attachments/assets/92e4d3d6-1dbf-43a2-a1cb-8a073b3a79d4)

Last thing that needs to be fixed is our `age` variable, there are many inconsistent values. 

In the first line we are converting the `Age` column to a string to use the string `.replace()` method on our dataset and replacing wherever we see a 'Y' with a blank. Then we add `regex= False` because we want python to treat `'Y'` as a literal string rather than as a regex pattern and assigns all that back to our age variable. <br>
![image](https://github.com/user-attachments/assets/f70e0550-1906-44ef-9071-cf715192aadd)

This next line takes our new text(str) variable and converts that variable to a number and for the values that give an error we handle them using `errors='coerce'`. What thisty does is makes all the values that give errors an `NaN` value. <br>
![image](https://github.com/user-attachments/assets/b0647c1a-df26-4de7-a1e7-1743fd8859fd)

We also have a number of items that are invalid values within this column, so for that we can replace them using the `.replace()` function, passing through infinite values, both negative and positive, and then replacing them with `NaN`. 
![image](https://github.com/user-attachments/assets/c964e6cb-3ffb-4190-a559-72b685ed8664)

Lastly, what I want to do is make all those nan values equal -1 so we know to filter it out to get a better read on our dataset. Then we can change the datatype of our dataset to int as all the values are numbers!
![image](https://github.com/user-attachments/assets/cb0a45a5-7717-4682-9fe8-e6090e0f4b28)

Lastly lets see the unique age values within our dataset after cleaning the column. 
![image](https://github.com/user-attachments/assets/c6d4365d-4f2a-449d-afb5-14bbef558140)

**With our dataset cleaned and prepped, we save the updated dataset to a CSV file for further analysis and visualization using Tableau. This cleaned dataset will enable us to build a detailed dashboard and extract meaningful insights about dog bites.**
![Screenshot 2024-07-04 171647](https://github.com/user-attachments/assets/93d4f9c3-6773-4db0-8716-ead0accf8187)

## Construct 
With the data now cleaned and prepared, we have generated a series of insightful visualizations to facilitate our exploratory data analysis (EDA). These charts are created using Matplotlib and Seaborn in Python, effectively presenting the data in a clear and comprehensive way!

![image](https://github.com/user-attachments/assets/04529a1a-15e8-4652-bc14-5898a4b068d9)
![image](https://github.com/user-attachments/assets/83ebe493-2187-4822-9812-912fede237b4)
![image](https://github.com/user-attachments/assets/8de86bcf-7dc5-472e-81d4-af9487b4cdb6)
![image](https://github.com/user-attachments/assets/d4828a24-8b5e-4211-9a48-48bc46d93996)
![image](https://github.com/user-attachments/assets/ad8ca5b5-f1e4-4d51-892f-506f6751b62c)

## Share 
**From analyzing the datset I found many insights that could help potential dog owners with their selection!** 

*Below are some of the Insights that I have found:*

- **Pitbulls** were the most vicious dogs in NYC from the dataset by a significant margin followed by **Shih Zhu,German Shepards, and Mixed/Other**. (Pitbull - 22% of bites, Shih Tzu at 4%,Chihuahua at 3.5%, German Shepard at 3.4%, and lastly Mixed/Other at 3.09%)
- Most of the dogs with the highest bite total were between the ages of 1 and 5. The breed associated with these dog teenager bites were Pitbulls, Shih Tzu, and German Shepards. This could mean that one is better off getting a dog from birth to self-train them or to obtain an older dog that has already been trained for a couple of years.
- The borough with the most bites cases was **Queens** followed closely by *Manhattan and Brooklyn*. ALso, progressive years and dog bites have a negative relationship, this means that as the years have gone by between *2015 and 2022* dog bites have declined.
- Another question I had was whether or not a dog being Spayed had a profound impact on dog bites?
Well, almost **74** percent of bites were commited by dogs that were not spayed, while dogs that were spayed only accounted for **25** percent of bites.
- Dog Bites were at a high from 2015 through 2019 , and dropped during 2020 and 2021.
- Bites were at a high during the *summer months (June-August)* and followed closely by *spring (April-May)*. These months were also very high during year **2017 and 2018**.
- **Saturday and Sunday** peaked as top bite days throughout the year. They also seemed to be especially high during the *summner months*.

