# AffinityAnswers Data Engineer Profile Assignment 

Program to check degree of profanity in a file full of Twitter tweets by various users provided by a set of words that indicates racial slurs.

## Assumptions:
 - Degree of profanity: 
     1. 0 for not racially profane.
     2. 1 for racially profane.
              
 - Racial slurs that are provided are in a text file each word in a new line.
          
 - tweets are provided in a csv file such as `@user, tweet`
          
 ## Running the code:
 
 **usage: main.py <racial_slurs_text_file> <tweets_csv_file>**
          
 
## Questions:

### **Interesting dataset**
>**NYC TLC Trip Record Data**

The dataset contains Yellow, Green taxi trips, and For-Hire Vehicle trips records containing fields capturing pick-up date, drop-off dates/time, pickup and drop-off location, and trip distance in their respective dataset. I used this dataset to orchestrate the ETL pipeline in the Databricks and create the report. 
The dataset contains many opportunities to explore and perform your analysis. It even contains geographical data for mapping. Fare price to perform Finance representation such as total earning by Yellow Taxi. I get to explore many insights from it. Overall It is really enjoyable data with Big Data Tools.

dataset avaiable at: 
[link](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

my project related to the dataset available at :
[link](https://addy024.github.io/Portfolio/)

### Why do we need a database?

Primarily we use databases for storing data. But databases have advantages over other, simpler data storage systems such as text files or spreadsheets.

**Access** 
Large volumes of data can be stored in one place. 
Multiple users can read and modify the data at the same time.
searchable and sortable quickly and easily.

**Integrity** 
each change transaction must conform to a set of rules (ACID for RDBMS)

**Security**
Databases allow access to be controlled, allowing users to have different privileges: for example, some users may be able to read data, but not to write it.

### Unix command line 

I used to use mostly ubuntu 20 virtual machines on the virtual box in my windows machine for practising Big Data ecosystem tools such as Spark, Hive, etc. Currently, I switched over to WSL2 (Windows Subsystem for Linux) so I am quite familiar with command line navigation, env file, file system and permission, Bash scripting, editors such as vim and nano, etc. 
