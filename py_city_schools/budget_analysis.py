#!/usr/bin/env python
# coding: utf-8

# In[ ]:


PyCity Schools Analysis

# 1. Overall school size played a rather large factor. As the bottom 3 schools in terms of population,
# averaged out to about $1,967,232. While the 3 largest schools averaged about $1,617,215. Smaller schools seemed
# to have larger budgets on average.

# 2. There was a three-way tie for highest average math score for both reading and math. Cabrera High School, 
# Pena High School, and Thomas High School. All of which scored 84% in both Math and Reading.

# 3. The smallest school overall was spending nearly 16 times more per capita ($2442.92), than the largest school ($383.97).


# In[ ]:





# In[488]:


## Importing dependencies 
import pandas as pd
import os


# In[490]:


## Importing in CSV files
school_data_csv = "Resources/schools_complete.csv"
student_data_csv =  "Resources/students_complete.csv"

## Reading in CSV files and convert into Pandas dataframes
school_data_df = pd.read_csv(school_data_csv)
student_data_df = pd.read_csv(student_data_csv)

## Merging the dataframes
school_data_complete = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[492]:


## Verifying data is clean
school_data_complete.count()


# In[494]:


## Total number of unique schools

## Printing out school dataframe to view all the school names
print(school_data_df)
## Counting the rows so row 0 is also included in the total
#school_data_df.count()
unique_schools = 15

print(f"Total number of unique schools: {unique_schools}")


# In[496]:


## Total students

## Counting each student ID
student_data_df.count()

total_students = 39170
print(f"Total number of students: {39170}")


# In[498]:


## Total budget

## Adding the budget for each school together
total_budget = school_data_df['budget'].sum()
#print(total_budget)

print(f"Total budget: ${total_budget}")


# In[500]:


## Average math score

## Finding the average math score, then rounding to the nearest whole #
average_math = (school_data_complete['math_score'].mean()).round()
#print(average_math)

print(f"Average math score: {average_math}")


# In[326]:


## Average reading score

## Finding the average reading score, then rounding to the nearest whole #
average_reading = (school_data_complete['reading_score'].mean()).round()
#print(average_reading)

print(f"Average reading score: {average_reading}")


# In[502]:


## % passing math (the percentage of students who passed math)

## Sorting to find students that passed math
math_pass = school_data_complete.loc[school_data_complete['math_score'] >= 70]
#print(math_pass)
#percent_pass_math = math_pass.mean()
## Counts how many students are in the new variable
math_pass.count()
## Setting a variable to hold the # of passing students for math
student_math_pass = 29370

## Finding the average
average_math_pass = ((student_math_pass/total_students)*100)
r_average_math_pass = round(average_math_pass)
#print(r_average_math_pass)

print(f"Average passing math: {r_average_math_pass}%")


# In[504]:


## % passing reading (the percentage of students who passed reading)

## Sorting to find students that passed reading
reading_pass = school_data_complete.loc[school_data_complete['reading_score'] >= 70]
#print(reading_pass)
#percent_pass_reading = reading_pass.mean()
## Counts how many students are in the new variable
reading_pass.count()
## Setting a variable to hold the # of passing students for reeading
student_reading_pass = 33610

## Finding the average
average_reading_pass = ((student_reading_pass/total_students)*100)
r_average_reading_pass = round(average_reading_pass)
#print(r_average_reading_pass)

print(f"Average passing reading: {r_average_reading_pass}%")


# In[506]:


## % overall passing (the percentage of students who passed math AND reading)

## Sorting to find students that passed reading and math
all_pass = school_data_complete.loc[(school_data_complete['math_score'] >= 70) &
    (school_data_complete['reading_score'] >=70)]
## Counts how many students passed both subjects
all_pass.count()
total_all_pass = 25528

## Finding the average
average_all_pass = ((total_all_pass/total_students)*100)
r_average_all_pass = round(average_all_pass)
#print(r_average_all_pass)

print(f"Overall passing: {r_average_all_pass}%") 


# In[332]:


## District Summary

district_df = pd.DataFrame({
    "Total Schools": [unique_schools],
    "Total Students": [total_students],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math],
    "Average Reading Score": [average_reading],
    "% Passing Math": [r_average_math_pass],
    "% Passing Reading": [r_average_reading_pass],
    "% Overall Passing": [r_average_all_pass]})
district_df
    


# In[ ]:





# In[508]:


## Listing out all the school names
unique_schools = school_data_complete['school_name'].unique()
unique_schools



# In[510]:


## Per school type

## Finding school types and converting to a list
per_school_type = school_data_df['type'].tolist()
per_school_type


# In[512]:


## Per school student total

## Finding students for each school then converting to a list
per_school_students = school_data_complete['school_name'].value_counts()
per_school_students_one = per_school_students.tolist()
per_school_students_one


# In[514]:


## Per school budget

## Finding budgets for each school and converting to a list
per_school_budget_one = school_data_df['budget'].tolist()
per_school_budget_one


# In[ ]:


per_school_budget = school_data_complete.groupby(['school_name']).mean()['budget']


# In[516]:


## Per capita budget

per_capita_budget = per_school_budget / per_school_students
per_capita_budget_two = per_capita_budget.tolist()
per_capita_budget_two


# In[518]:


## Per school average math score

## Conversion to ineteger so values can be used for calculations
school_data_complete['math_score'] = pd.to_numeric(school_data_complete['math_score'])
per_school_math = school_data_complete.groupby('school_name')['math_score'].mean()
per_school_math_two = per_school_math.round().tolist()
per_school_math_two


# In[520]:


## Per school average reading score

## Conversion to ineteger so values can be used for calculations
school_data_complete['reading_score'] = pd.to_numeric(school_data_complete['reading_score'])
per_school_reading = school_data_complete.groupby('school_name')['reading_score'].mean()
per_school_reading_two = (per_school_reading.round()).tolist()
per_school_reading_two


# In[ ]:


## 



# In[456]:


## Per school average passing math


#per_school_pass_math = school_data_complete.loc[school_data_complete["math_score"] >= 70]
#per_school_pass_math[['school_name', 'math_score']]




# In[458]:


## Per school average passing reading

#per_school_pass_reading = school_data_complete.loc[school_data_complete["reading_score"] >= 70]
#per_school_pass_reading


# In[454]:


## Per school average passing both subjects

##passing_math_and_reading = school_data_complete[(school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)]
##passing_math_and_reading = school_data_complete[''].value_counts()
##passing_math_and_reading


# In[460]:


#per_school_passing_math = per_school_math.groupby(["school_name"]).count()["student_name"] /
#per_school_counts * 100


# In[528]:


# Create the per_school_summary DataFrame
per_school_summary = pd.DataFrame({
    "School Name": unique_schools,
    "School Type": per_school_type,
    "Total Students": per_school_students_one,
    "Total School Budget": per_school_budget_one,
    "Per Capita Budget": per_capita_budget_two,
    "Average Math Score": per_school_math_two,
    "Average Reading Score": per_school_reading_two
})
#per_school_summary
## Filter by 'School Name"
updated_summary_df = per_school_summary.set_index("School Name")
updated_summary_df


# In[ ]:





# In[ ]:





# In[ ]:




