# New-York-City-Dog-Bites
#### This is a link to my report on New York Dog Bites! -> [Dashboard](https://lookerstudio.google.com/reporting/db272abe-77fe-4810-b35a-b548c44501c8)
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
In the anlysis phase I began cleaning the data. This includes removing any duplicate values, null values, outliers, and potentially misleading data that would skew my results. I also used many advanced level formulas such as if statements, vlookups, conditional formatting to put the data into the correct form to start analyzing it. Then, I began to go into exploratory data analysis with the help of pivot tables so I could find trends and insights that I felt were excting to share and to put in my visualizations. Once I formualted what I wanted to show visually it was time to construct it. 

## Construct 
After the data was cleaned, exploratory data analysis within Google Sheets with the help of pivot tables, allows a visual representation of insights. For this project I used Google Data Studio which is now refered to as Looker Studio. Within this dataset I provided many visualizations such as tables, bar graphs, heat map, and straight text. Using this dashboard I am able to share my findings. 

## Share 
From analyzing the datset I found many insights that could help potential dog owners with their selection! 
- Pitbulls were the most vicious dogs in NYC from the dataset by a significant margin followed by mixed breeds, Shih Zhu, and German Shepards. (Pitbull - 35% of bites, Mixed- 13%, German Shepard 7%, and Shih Tzu at 9%)
- Most of the dogs that bite were between the ages of 1 and 5. This could mean that one is better off getting a dog from birth to self-train them or to obtain an older dog that has already been trained for a couple of years. 
- The borough with the most bite cases was Queens, followed by Manhattan, and lastly Brooklyn. Progressive years and dog bites have a negative relationship, this means that as the years have gone by between 2015 and 2022 dog bites have declined. 
- Male dogs accounted for more than 70% of bites, while females only accounted for 27%. One other insight I found interesting was whether a dog being spayed or neutered made it prone to attack more. From putting the data into a pivot table it seemed that 51% were neutered and spayed while 49.5% were not. At first it showed a difference was not apparent, but then I added breed and it showed that the top dogs that were prone to bite were not spayed or neutered!


