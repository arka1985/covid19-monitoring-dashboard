{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <font color='violet'> On-line Dashboard For Monitoring of the Health Status of the Students for Prevention of Spread of COVID-19</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### <font color='turquoise'> Designed and Developed By: Dr. Arkaprabha Sau, MBBS, MD (Gold Medalist), Dip. Public Health, Dip. Geriatric Medicine, Ph.D. (Research Fellow-Health Informatics)</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color='blue'> Institute Name: ABC</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color='blue'> Department: XYZ</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python program to get \n",
    "# current date \n",
    "# Import date class from datetime module \n",
    "from datetime import date \n",
    "from datetime import datetime\n",
    "from datetime import date \n",
    "from datetime import timedelta\n",
    "today = date.today()\n",
    "today_str = today.strftime(\"%Y-%m-%d\")\n",
    "yesterday = today - timedelta(days = 1)\n",
    "yesterday_str = yesterday.strftime(\"%Y-%m-%d\")\n",
    "daybeforeyesterday = today - timedelta(days = 2)\n",
    "daybeforeyesterday_str = daybeforeyesterday.strftime(\"%Y-%m-%d\")\n",
    "# Returns the current local date \n",
    "#today = date.today() \n",
    "#print(\"Today date is: \", today)\n",
    "# returns current date and time "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Relevent libraries\n",
    "from __future__ import print_function\n",
    "from ipywidgets import interact, interactive, fixed, interact_manual\n",
    "from IPython.core.display import display, HTML\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://raw.githubusercontent.com/arka1985/covid19-monitoring-dashboard/main/covid-19-monitoring.csv'\n",
    "df = pd.read_csv(url, index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8e90f5c7f4d545e3a90d7b35d4f64aed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(DatePicker(value=None, description='Pick a Date'), Output()), _dom_classes=('widget-inte…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from ipywidgets import interact\n",
    "import ipywidgets as widgets\n",
    "\n",
    "#day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]\n",
    "#month = [1,2,3,4,5,6,7,8,9,10,11,12]\n",
    "#year = [2021,2021]\n",
    "\n",
    "def DAY(day):\n",
    "    \"\"\"\n",
    "    Do your computations here\n",
    "    \"\"\"\n",
    "    return day\n",
    "\n",
    "interact(DAY, day=widgets.DatePicker(description='Pick a Date',disabled=False));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color='red'> Total Number of Student: 50 </font>\n",
    "## Number of submission and non-submission today till Now"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "today_submission=df.loc[df['datetime']==today_str,'roll'].nunique()\n",
    "#print(\"Total Number of students submitted online form today = \", today_submission) \n",
    "yet_to_submit = 50 - today_submission\n",
    "#print(\"Total Number of students yet to submit online form today = \", yet_to_submit) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div style = 'background-color: #504e4e; padding: 30px '><span style='color: #fff; font-size:30px;margin-left:30px;'> Total Number of students submitted online form today: 1</span></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div style = 'background-color: #504e4e; padding: 30px '><span style='color: red; font-size:30px;margin-left:30px;'> Total Number of students yet to submit online form today: 49</span></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# displaying the total stats\n",
    "\n",
    "display(HTML(\"<div style = 'background-color: #504e4e; padding: 30px '>\" +\n",
    "             \"<span style='color: #fff; font-size:30px;margin-left:30px;'> Total Number of students submitted online form today: \"  + str(today_submission) +\"</span>\" +\n",
    "             \"</div>\")\n",
    "       )\n",
    "display(HTML(\"<div style = 'background-color: #504e4e; padding: 30px '>\" +\n",
    "             \"<span style='color: red; font-size:30px;margin-left:30px;'> Total Number of students yet to submit online form today: \" + str(yet_to_submit) + \"</span>\"+\n",
    "             \"</div>\")\n",
    "       )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Find the roll number of the students yet to submit online from today"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Roll number of the students yet to submit online form today =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]\n"
     ]
    }
   ],
   "source": [
    "df1 = df.loc[df['datetime']==today_str]\n",
    "submission=df1.loc[df1['datetime'] == today_str, 'roll'].values.flatten().tolist()\n",
    "submission_list = [int(i) for i in submission]\n",
    "# No Response on specific date\n",
    "def find_missing(lst): \n",
    "    return [x for x in range(1,51)  \n",
    "                               if x not in lst] \n",
    "missing = find_missing(submission_list)\n",
    "print(\"Roll number of the students yet to submit online form today = \", missing) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Number of Students suffering from different COVID Related Symptoms\n",
    "| Temperature | Symptoms | Co-morbidity |\n",
    "| --- | --- | --- |\n",
    "| Fever when temperature >=100 | Cough | Diabetes |\n",
    "| Warning when temperature >= 98.9 and < 100 | Fever | Hypertension\n",
    "| Normal when temperature < 98.8 | Difficulty in Breathing | Lung Disease\n",
    "| | Loss of sense of smell and taste | Heart Disease\n",
    "| | None of the Above | Kidney Disease\n",
    "| | | None of the Above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n",
      "/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "df1['temperature'] = df1['temperature'].astype(str).str.extract('([-+]?\\d*\\.\\d+|\\d+)').astype(float)\n",
    "filter_method = lambda x: 'Fever' if x >= 100 else 'Warning' if (x < 100 and x >= 98.9) else 'Normal'\n",
    "df1['temperature'] = df1['temperature'].apply(filter_method)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Normal    1\n",
       "Name: temperature, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['temperature'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1a28801860>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='temperature',data=df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

