#!/usr/bin/env python
# coding: utf-8

# # <font color='violet'> On-line Dashboard For Monitoring of the Health Status of the Students for Prevention of Spread of COVID-19</font>

# #### <font color='turquoise'> Designed and Developed By: Dr. Arkaprabha Sau, MBBS, MD (Gold Medalist), Dip. Public Health, Dip. Geriatric Medicine, Ph.D. (Research Fellow-Health Informatics)</font>

# ## <font color='blue'> Institute Name: ABC</font>

# ## <font color='blue'> Department: XYZ</font>

# In[59]:


# Python program to get 
# current date 
# Import date class from datetime module
from __future__ import print_function
from datetime import date 
from datetime import datetime
from datetime import date 
from datetime import timedelta
today = date.today()
today_str = today.strftime("%Y-%m-%d")
yesterday = today - timedelta(days = 1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
daybeforeyesterday = today - timedelta(days = 2)
daybeforeyesterday_str = daybeforeyesterday.strftime("%Y-%m-%d")
# Returns the current local date 
#today = date.today() 
#print("Today date is: ", today)
# returns current date and time 


# In[60]:


# Import Relevent libraries
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.core.display import display, HTML
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[61]:


url = 'https://raw.githubusercontent.com/arka1985/covid19-monitoring-dashboard/main/covid-19-monitoring.csv'
df = pd.read_csv(url, index_col=0)


# In[76]:


df


# In[100]:


from ipywidgets import interact
import ipywidgets as widgets

#day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#month = [1,2,3,4,5,6,7,8,9,10,11,12]
#year = [2021,2021]
def DAY(day):
    return print(day)

interact(DAY, day=widgets.DatePicker(description='Pick a Date', disabled=False));


# In[90]:


day


# In[73]:


def foo(x):
    return x
interact(foo, x=widgets.DatePicker())


# In[ ]:





# ## <font color='red'> Total Number of Student: 50 </font>
# ## Number of submission and non-submission today till Now

# In[47]:


today_submission=df.loc[df['datetime']==today_str,'roll'].nunique()
#print("Total Number of students submitted online form today = ", today_submission) 
yet_to_submit = 50 - today_submission
#print("Total Number of students yet to submit online form today = ", yet_to_submit) 


# In[65]:


# displaying the total stats

display(HTML("<div style = 'background-color: #504e4e; padding: 30px '>" +
             "<span style='color: #fff; font-size:30px;'> Total Number of students submitted online form today: "  + str(today_submission) +"</span>" +
             "</div>")
       )
display(HTML("<div style = 'background-color: #504e4e; padding: 30px '>" +
             "<span style='color: red; font-size:30px;'> Total Number of students yet to submit online form today: " + str(yet_to_submit) + "</span>"+
             "</div>")
       )


# ## Find the roll number of the students yet to submit online from today

# In[23]:


df1 = df.loc[df['datetime']==today_str]
submission=df1.loc[df1['datetime'] == today_str, 'roll'].values.flatten().tolist()
submission_list = [int(i) for i in submission]
# No Response on specific date
def find_missing(lst): 
    return [x for x in range(1,51)  
                               if x not in lst] 
missing = find_missing(submission_list)
print("Roll number of the students yet to submit online form today = ", missing) 


# ## Number of Students suffering from different COVID Related Symptoms
# | Temperature | Symptoms | Co-morbidity |
# | --- | --- | --- |
# | Fever when temperature >=100 | Cough | Diabetes |
# | Warning when temperature >= 98.9 and < 100 | Fever | Hypertension
# | Normal when temperature < 98.8 | Difficulty in Breathing | Lung Disease
# | | Loss of sense of smell and taste | Heart Disease
# | | None of the Above | Kidney Disease
# | | | None of the Above

# In[24]:


df1['temperature'] = df1['temperature'].astype(str).str.extract('([-+]?\d*\.\d+|\d+)').astype(float)
filter_method = lambda x: 'Fever' if x >= 100 else 'Warning' if (x < 100 and x >= 98.9) else 'Normal'
df1['temperature'] = df1['temperature'].apply(filter_method)


# In[25]:


df1['temperature'].value_counts()


# In[26]:


sns.countplot(x='temperature',data=df1)


# In[ ]:




