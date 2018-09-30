
# coding: utf-8

# In[1]:


# Mitchell Pudil
# Econ 213R: Applied Machine Learning
# Homework 1: Exploring Data

# First Dataset: Homeschooling Data

import pandas as pd
import numpy as np
import matplotlib as plt


# Import Data and look at head
df = pd.read_csv("/Users/mitchellpudil/Desktop/Personal_Research/Homeschool/homeschool2.csv")
df.head(10) #


# In[2]:


df.describe()


# In[7]:


df['lnhhinc'].hist(bins=15)      # Histogram of natural log of income


# In[8]:


# Create column called "income" to graph actual income 

df['income'] = np.exp(df['lnhhinc']) 
df['income'].hist(bins=15)


# In[9]:


# Boxplot of child's age (cage)
df.boxplot(column='cage')


# In[10]:


# boxplot of child's age by whether or not they are homeschooled
df.boxplot(column='cage', by='homeschool')


# In[14]:


# Now using matplotlib to chart probability of being homeschooled by gender

import matplotlib.pyplot as plt

temp1 = df['cmale'].value_counts(ascending=True)
temp2 = df.pivot_table(values='homeschool', index=['cmale'])
print("Frequency Table for Homeschooling:")
print(temp1)

print("\nProbbility of being homeschooled by Gender")
print(temp2){
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mitchell Pudil\n",
    "## Econ 213R: Applied Machine Learning\n",
    "## Homework 1: Exploring Data\n",
    "\n",
    "## First Dataset: Homeschooling Data\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The First dataset is homeschooling data. We will be looking at how the demographics of children who are homeschooled compare with the demographics of those who are not homeschooled"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We will begin by importing the appropriate packages that will be used later to analyze data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd # Allows to type pd to represent pandas \n",
    "import numpy as np # Allows for scientific computing\n",
    "import matplotlib.pyplot as plt  # visualization\n",
    "import seaborn as sns  # Allows for cleaner graphing capabilities"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### Import data and look at first few lines of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>year</th>\n",
       "      <th>homeschool</th>\n",
       "      <th>lnhhinc</th>\n",
       "      <th>momed</th>\n",
       "      <th>maritalmom</th>\n",
       "      <th>momage</th>\n",
       "      <th>cage</th>\n",
       "      <th>numsib</th>\n",
       "      <th>cmale</th>\n",
       "      <th>...</th>\n",
       "      <th>zip</th>\n",
       "      <th>religious</th>\n",
       "      <th>hhinc</th>\n",
       "      <th>meducation</th>\n",
       "      <th>evermarried</th>\n",
       "      <th>educ_evermarried</th>\n",
       "      <th>marriedmom</th>\n",
       "      <th>mothered</th>\n",
       "      <th>marrieded</th>\n",
       "      <th>hvalue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2003</td>\n",
       "      <td>0</td>\n",
       "      <td>10.9151</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>37</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>55000</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>15</td>\n",
       "      <td>Not Homeschooled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2003</td>\n",
       "      <td>0</td>\n",
       "      <td>10.5321</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>37500</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "      <td>Not Homeschooled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2003</td>\n",
       "      <td>0</td>\n",
       "      <td>10.5321</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>37500</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "      <td>Not Homeschooled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2003</td>\n",
       "      <td>0</td>\n",
       "      <td>11.3794</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>87500</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>Not Homeschooled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2003</td>\n",
       "      <td>0</td>\n",
       "      <td>11.3794</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>87500</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>Not Homeschooled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0  year  homeschool  lnhhinc  momed  maritalmom  momage  cage  \\\n",
       "0           1  2003           0  10.9151      3           1      37     8   \n",
       "1           2  2003           0  10.5321      2           1      36    16   \n",
       "2           3  2003           0  10.5321      2           1      36    10   \n",
       "3           4  2003           0  11.3794      5           1      39     8   \n",
       "4           5  2003           0  11.3794      5           1      39     6   \n",
       "\n",
       "   numsib  cmale        ...         zip  religious  hhinc  meducation  \\\n",
       "0       2      1        ...           3          1  55000          15   \n",
       "1       2      0        ...           1          1  37500          13   \n",
       "2       2      0        ...           1          1  37500          13   \n",
       "3       2      1        ...           2          0  87500          20   \n",
       "4       2      1        ...           2          0  87500          20   \n",
       "\n",
       "   evermarried  educ_evermarried  marriedmom  mothered  marrieded  \\\n",
       "0            1                15           1        15         15   \n",
       "1            1                13           1        13         13   \n",
       "2            1                13           1        13         13   \n",
       "3            1                20           1        20         20   \n",
       "4            1                20           1        20         20   \n",
       "\n",
       "             hvalue  \n",
       "0  Not Homeschooled  \n",
       "1  Not Homeschooled  \n",
       "2  Not Homeschooled  \n",
       "3  Not Homeschooled  \n",
       "4  Not Homeschooled  \n",
       "\n",
       "[5 rows x 24 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "homedf = pd.read_csv(\"/Users/mitchellpudil/Desktop/Personal_Research/Homeschool/homeschool2.csv\")  # Import dataset from csv\n",
    "homedf.head() # View first 5 rows of data\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's now describe the data by looking at the mean, std, and quartiles for each of the columns/features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>year</th>\n",
       "      <th>homeschool</th>\n",
       "      <th>lnhhinc</th>\n",
       "      <th>momed</th>\n",
       "      <th>maritalmom</th>\n",
       "      <th>momage</th>\n",
       "      <th>cage</th>\n",
       "      <th>numsib</th>\n",
       "      <th>cmale</th>\n",
       "      <th>...</th>\n",
       "      <th>region</th>\n",
       "      <th>zip</th>\n",
       "      <th>religious</th>\n",
       "      <th>hhinc</th>\n",
       "      <th>meducation</th>\n",
       "      <th>evermarried</th>\n",
       "      <th>educ_evermarried</th>\n",
       "      <th>marriedmom</th>\n",
       "      <th>mothered</th>\n",
       "      <th>marrieded</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.00000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "      <td>1496.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>8032.062834</td>\n",
       "      <td>2005.118316</td>\n",
       "      <td>0.498663</td>\n",
       "      <td>10.681364</td>\n",
       "      <td>3.012032</td>\n",
       "      <td>1.583556</td>\n",
       "      <td>40.210561</td>\n",
       "      <td>11.430481</td>\n",
       "      <td>1.473262</td>\n",
       "      <td>0.522059</td>\n",
       "      <td>...</td>\n",
       "      <td>2.606283</td>\n",
       "      <td>1.601604</td>\n",
       "      <td>0.605615</td>\n",
       "      <td>61133.02139</td>\n",
       "      <td>14.655080</td>\n",
       "      <td>0.935160</td>\n",
       "      <td>13.780749</td>\n",
       "      <td>0.780080</td>\n",
       "      <td>14.850267</td>\n",
       "      <td>11.743316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>10181.826004</td>\n",
       "      <td>3.316933</td>\n",
       "      <td>0.500165</td>\n",
       "      <td>0.962473</td>\n",
       "      <td>1.145526</td>\n",
       "      <td>1.260025</td>\n",
       "      <td>6.822385</td>\n",
       "      <td>3.917440</td>\n",
       "      <td>1.148776</td>\n",
       "      <td>0.499680</td>\n",
       "      <td>...</td>\n",
       "      <td>1.031640</td>\n",
       "      <td>0.804068</td>\n",
       "      <td>0.488882</td>\n",
       "      <td>44311.28131</td>\n",
       "      <td>3.542576</td>\n",
       "      <td>0.246325</td>\n",
       "      <td>4.964899</td>\n",
       "      <td>0.414331</td>\n",
       "      <td>3.085673</td>\n",
       "      <td>6.782203</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>2003.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.824050</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2500.00000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>374.750000</td>\n",
       "      <td>2003.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>10.221900</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27500.00000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>8.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>748.500000</td>\n",
       "      <td>2003.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>10.915100</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>55000.00000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>15.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>15256.750000</td>\n",
       "      <td>2007.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>11.379400</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>87500.00000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>17.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>34464.000000</td>\n",
       "      <td>2012.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>12.206100</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>74.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>200000.00000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Unnamed: 0         year   homeschool      lnhhinc        momed  \\\n",
       "count   1496.000000  1496.000000  1496.000000  1496.000000  1496.000000   \n",
       "mean    8032.062834  2005.118316     0.498663    10.681364     3.012032   \n",
       "std    10181.826004     3.316933     0.500165     0.962473     1.145526   \n",
       "min        1.000000  2003.000000     0.000000     7.824050     1.000000   \n",
       "25%      374.750000  2003.000000     0.000000    10.221900     2.000000   \n",
       "50%      748.500000  2003.000000     0.000000    10.915100     3.000000   \n",
       "75%    15256.750000  2007.000000     1.000000    11.379400     4.000000   \n",
       "max    34464.000000  2012.000000     1.000000    12.206100     5.000000   \n",
       "\n",
       "        maritalmom       momage         cage       numsib        cmale  \\\n",
       "count  1496.000000  1496.000000  1496.000000  1496.000000  1496.000000   \n",
       "mean      1.583556    40.210561    11.430481     1.473262     0.522059   \n",
       "std       1.260025     6.822385     3.917440     1.148776     0.499680   \n",
       "min       1.000000    22.000000     3.000000     0.000000     0.000000   \n",
       "25%       1.000000    36.000000     8.000000     1.000000     0.000000   \n",
       "50%       1.000000    40.000000    11.000000     1.000000     1.000000   \n",
       "75%       1.000000    45.000000    15.000000     2.000000     1.000000   \n",
       "max       7.000000    74.000000    20.000000     6.000000     1.000000   \n",
       "\n",
       "          ...            region          zip    religious         hhinc  \\\n",
       "count     ...       1496.000000  1496.000000  1496.000000    1496.00000   \n",
       "mean      ...          2.606283     1.601604     0.605615   61133.02139   \n",
       "std       ...          1.031640     0.804068     0.488882   44311.28131   \n",
       "min       ...          1.000000     1.000000     0.000000    2500.00000   \n",
       "25%       ...          2.000000     1.000000     0.000000   27500.00000   \n",
       "50%       ...          2.000000     1.000000     1.000000   55000.00000   \n",
       "75%       ...          4.000000     2.000000     1.000000   87500.00000   \n",
       "max       ...          4.000000     3.000000     1.000000  200000.00000   \n",
       "\n",
       "        meducation  evermarried  educ_evermarried   marriedmom     mothered  \\\n",
       "count  1496.000000  1496.000000       1496.000000  1496.000000  1496.000000   \n",
       "mean     14.655080     0.935160         13.780749     0.780080    14.850267   \n",
       "std       3.542576     0.246325          4.964899     0.414331     3.085673   \n",
       "min       6.000000     0.000000          0.000000     0.000000     8.000000   \n",
       "25%      13.000000     1.000000         13.000000     1.000000    13.000000   \n",
       "50%      15.000000     1.000000         15.000000     1.000000    15.000000   \n",
       "75%      17.000000     1.000000         17.000000     1.000000    17.000000   \n",
       "max      20.000000     1.000000         20.000000     1.000000    20.000000   \n",
       "\n",
       "         marrieded  \n",
       "count  1496.000000  \n",
       "mean     11.743316  \n",
       "std       6.782203  \n",
       "min       0.000000  \n",
       "25%       8.000000  \n",
       "50%      15.000000  \n",
       "75%      17.000000  \n",
       "max      20.000000  \n",
       "\n",
       "[8 rows x 23 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "homedf.describe()  # Describes the data: mean, std, quartiles, etc."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at how the household income for the homeschooled and those who aren't compares by graphing in Seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAbIAAAEKCAYAAAB36tAEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzs3Xd4VVX28PHvTiOBQEijJCEkQCjpJKF3kKIixUFH7KLjjIP6U2cc9R111FHHjlhHVBDbAIJSBKT3TmiaUEUQpKWHBNL3+8c5gRDTIPdykpv1eZ48SfY9Z+91I2bl7Kq01gghhBD1lZPVAQghhBC1IYlMCCFEvSaJTAghRL0miUwIIUS9JolMCCFEvSaJTAghRL0miUwIIUS9JolMCCFEvSaJTAghRL3mYnUA9Ymfn58OCQmxOgwhhKhXEhMTU7XW/vaqXxLZZQgJCWH79u1WhyGEEPWKUuqoPeuXrkUhhBD1miQyIYQQ9ZokMiGEEPWajJEJIWyisLCQ48ePk5eXZ3UowiLu7u4EBQXh6up6VduVRCaEsInjx4/TtGlTQkJCUEpZHY64yrTWpKWlcfz4cUJDQ69q29K1KISwiby8PHx9fSWJNVBKKXx9fS15IpdEJoSwGUliDZtV//0lkQnrlJSA1lZHIYSo5ySRiavvzBl48klo3hw8PCA0FF58Ec6fr/K2khLIzobMTMjNvUqxinpFKcXf/va3C9+/8cYbPPfcc1XeM3fuXJKTkyt87bnnnuONN964pCwkJITU1NRax2oLd999N7Nnz651PUeOHCEyMtKStm1BEpm4upKToUsXeP11iI+HMWOgRQt45hmjPDHxd7ccPgz//Ce0aQNeXuDtDc2awZAh8PHHcPasBe9D1EmNGjXi22+/vaxEU1UiE/WDJDJx9Zw4Addea3z9ySfwr3/BX/4Cr74Kb74J+flGdtq8GTB6HSdNgo4d4ZVXIDjYuHziRBg/Hg4cgPvvh4gIWLbMwvcl6gwXFxfuv/9+Jk2a9LvXjh49ypAhQ4iOjmbIkCH8+uuvbNy4kfnz5/P4448TGxvLzz//fFntvfXWW0RGRhIZGcnbb78NGE83nTt35r777iMyMpLbbruN5cuX06dPH8LCwti6dSsAubm5TJgwgW7dutG1a1fmzZsHQFJSEt27dyc2Npbo6GgOHjwIwOeff050dDQxMTHccccdF2JYu3YtvXv3pl27dheekLTWPP7440RGRhIVFcXMmTOrLC+ruLiYxx9/nG7duhEdHc1HH3104d4HH3yQ8PBwrr/+es6cOXNZPyt7kun34uooLobRoyE11chO5afnxsXB22/D3/4GQ4eSu2Q9974Tw8yZ0K8fPPQQ+JfbcvTee2HPHqO6YcPgr3+FyZPBRf5VW++RR2DXLtvWGRtr/BupxsSJE4mOjuYf//jHJeUPPvggd955J3fddRdTp07l4YcfZu7cuYwaNYqRI0cybty4CuubNGkSX3755YXvT5w4AUBiYiLTpk1jy5YtaK3p0aMHAwYMwNvbm0OHDvHNN98wZcoUunXrxtdff8369euZP38+L7/8MnPnzuWll15i8ODBTJ06lczMTLp3784111zDf//7X/7v//6P2267jYKCAoqLi0lKSuKll15iw4YN+Pn5kZ6efiGekydPsn79evbt28eoUaMYN24c3377Lbt27WL37t2kpqbSrVs3+vfvz8aNGyssL+vTTz/Fy8uLbdu2kZ+fT58+fRg2bBg7d+5k//79/Pjjj5w+fZrw8HAmTJhQ4/989iRPZOLqmD4dtm83ElXHjhVf07IlTJpEkUdTbhySxTffaO6/H55//vdJDEApiImBjz6Cm26CDz6AP/4RCgrs+1ZE3dasWTPuvPNO3nnnnUvKN23axK233grAHXfcwfr162tU36OPPsquXbsufAQEBACwfv16xo4dS5MmTfD09OTGG29k3bp1AISGhhIVFYWTkxMREREMGTIEpRRRUVEcOXIEgKVLl/LKK68QGxvLwIEDycvL49dff6VXr168/PLLvPrqqxw9ehQPDw9WrlzJuHHj8PPzA8DHx+dCfGPGjMHJyYnw8HBOnz59Ibbx48fj7OxMy5YtGTBgANu2bau0vKylS5fy+eefExsbS48ePUhLS+PgwYOsXbv2wr0BAQEMHjz4Mv/L2I/87SrsLzfXGAMLD4dBg6q+1t+fRyOWsHR1FJOD3yDm5kfQqup/po0aGU9jLVrA++/DjTfC7Nng7m7D9yAuTw2enOzpkUceIS4ujnvuuafSa2o7VVxXMeO2UaNGF752cnK68L2TkxNFRUUX7p8zZw6dOnW65N4uXbrQo0cPFi5cyPDhw/nkk0/QWlcab9m2SmOqLLaqYi57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8sknCQ8PJzo6mr///e8AnD59mrFjxxITE0NMTAwbN24EjCNS/vSnPxEREcGwYcM4bx4mu2vXLnr27El0dDRjx44lIyOjyvKyEhMTGTBgAPHx8QwfPpyTJ09eKI+JiaFXr168//779vmh1hGSyITtLVwIHTpAua1vSmkN780NpHNwLuFtz11REwdu/idngyPp8u/xNEveXKN7lDL2YPztN/jwwytqVtTQI4/AwIG2/XjkkerbPX/+PLGxsRc+nn322QuvlR7jsmfPHm677TYefvjhC69lZGSwcuVKJk2axA033MCjjz5KUlISP/74I7t27SI1NZUXX3yR5cuXs2PHDhISEnjrrbdIT0/nu+++IykpiT179vD008ZGQQ8//DADBgxg9+7d7Nixg4gIoyPo4MGDTJw4kaSkJJo3b86cOXMAuPPOO3n11VfZs2cPUVFRPP/881WWlyosLOShhx5i9uzZJCYmMmHCBP75z38CcM899/DOO++wadOmmv1Hq8ckkQnbOncONm0yTn+uxPJEb/b92oSxfa/8uPgSNw9+vO9tCpr5E/XEtTT7cUON7ouNhYQEePllOVnaEXl4eFxy5MoLL7xw4bWqjnG54YYbLhyz0rJly0uOYDly5AibN28mOTmZPn36EBsby/Tp0zl69CjNmjXD3d2d++67j2+//ZbGjY1t1FauXMkDDzwAgLOzM15eXoBxvEusuctNfHw8R44cISsri8zMzAt7F951112sXbu20vKy9u/fz08//cTQoUOJjY3lxRdf5Pjx47+7t+xBnI5IjnERtrVxo3EgWBX7Kr77bSDeTQsZ2DWzVk0Vevqw+4H/Ev3RX4n5+zXsffprUvuNrfa+e+81dvt46y3jkGphexaf4lIjZY8kKXvMSvkjWIqKinB2dmbo0KH8r4KV9Vu3bmXFihXMmDGD9957j5UrV1baZtm6nZ2dL3QtXimtNREREb976srMzKyzR67YgzyRCdtatcrYzaOSne6PnmrE95t9ub5nGm4utd83Ks8ngJ0PTSW3VXsin72RTq/di0tO1Qmyc2djedubb0IFQw7CQVV2jEtN9OzZkw0bNnDokLHs49y5cxw4cICcnByysrK47rrrePvtt9llnoo9ZMgQPjT7r4uLi8nOzq60bi8vL7y9vS8cyvnFF18wYMCASsvL6tSpEykpKRcSWWFh4YVuSy8vrwtPnV999VWN32t9JIlM2NbKlUamaFzxTvWfL22F1orre9pupUOhpw87H5rK0WvupdWS6fS8JYR2/32cxkf3VroLyF13GV2L775rszBEHVfZMS414e/vz2effcb48eOJjo6mZ8+e7Nu3j7NnzzJy5Eiio6MZMGAAkyZNAmDy5MmsWrWKqKgo4uPjSUpKqrL+6dOn8/jjjxMdHc2uXbsujO1VVl7Kzc2N2bNn88QTTxATE0NsbOyFiSXTpk1j4sSJ9OrVCw8Pj8v5UdU7dj3GxdHIMS7VyM4GHx+49VbjULBytIaw23vQrHERb02s+blPl8Pzt/0Er5iK/+4VqJJi8n0DONspnvOBYZwP7HDhI69FMP981pl9++DIkSqXu4kakmNcBFhzjIuMkQnbWbcOiosrHR/b8JMXP5/w4Mlbj9othJzATiTf+SqNMk/js3cDzQ9upcmRfXhvW4Zz4cU59yUubjzX/k8MS3+P/046z+PPOvZfrEI4MklkwnZWrQI3N2OX3gp89kMrPBoV0z86y+6h5DdvycleN3Ky141Ggda4ZafgkfIrHqnHaHL6ML33/cA1LOPN56J5sOQdPJ56BMoMxgsh6gdJZMJ21q83xsfc3H730rk8J2at8mdATCYejSzYI0opCrxaUODVgqwORg/Hz6Nh3KZ0ls9qyWfPH+GBhX1hzhxjc0ZxRbTWDWq2nLiUVUNVMtlD2EZeHuzYYWydUYHv1vlx9rwLw7vVre0sO/b0oXNwLm/7vkhJ8j5j/Zs580xcHnd3d9LS0iz7ZSaspbUmLS0Nd3f3q962PJEJ29ixAwoLK+1W/HpFS1p65xPdLvcqB1Y1pWDcgBRe/CKERY/OY+TXt8Lw4cZ4X8eOVodXrwQFBXH8+HHk3L6Gy93dnaCgoKveriQyYRulCzIreCLLOOvC0u3e/KF/aoUnQFttQEwmUxYUMGl1V0a+9hr83//B0KHGDsNyBl2Nubq6EhoaanUYogGqg79WRL20eTO0bm1Mvy/nu3V+FBU7MSi2bq4+dnGGsf1SWLnTm10F4fDKK8ahoHfffVmnUQshrCGJTNjGxo1QyRqiWatbEOCXT8c2tduOx55G9krHo1Exk74Jgk6d4C9/gUWL4DIWzQohrCGJTNTesWNw4kSF42OpWa4sT/RmYEwmdXkym6dHMSO6p/O/lS04meYGY8YY56n94x+wb5/V4QkhqiCJTNRe6fhYBYnsu3V+FJcoBtVyg+Cr4Q/9UygqVrw/N9CYBfK3v4G7O0ycKF2MQtRhkshE7W3ebCwkbtfudy/NXNWCIP882gfU3W7FUoF+BfSJzOLD+QGcy3MCb29jq/yVK8HcbFYIUfdIIhO1l5gI7duDq+slxWlZLqze1ZwBdbxbsaybBqSQnu3KF0tbGgUjRxqLvB97DMwTgYUQdYskMlE7JSWwc2eFa64WbvaluETRL8r+W1LZSlS7XDq1Ocfbc4IoKQGcneGhh4xZjObO5kKIukUSmaidQ4eM81DCwn730twNfvg3L6jTsxXLMxZIn2Hfr01Yss1cShAebhxg9tprIIt9hahzJJGJ2klMND6XeyI7l+fED1t96BOZVW+6FUsNiMnCz6uAd74NvFh4331w7hy89JJ1gQkhKiSJTNROYqKxSXBIyCXFyxO9OZ/vTN/I+tOtWMrVRTOqdxo/bPVl36/mAaHBwXDttfDhh/Dbb9YGKIS4hCQyUTs7dhizFV0u3e1s7no/PD2KiOlQPydIjOyVhqtLCe+WfSq7/XbjvLXXX7cuMCHE70giE1dOayORletWLCpWzN/oR8/wbFycLYqtlrybFjEkLoPpS1qRmWMm6VatjD0Yp0yB06etDVAIcYEkMnHlDh+GrKzfTfTY+FMz0rJd6VMPuxXLurFfKrl5zkxd1Opi4a23Qn6+zGAUog6RRCauXCUTPb7f5IuLcwndOp+1ICjbCQs6T3S7HN79LpDiYrOwTRsYOBDefx/S0qwMTwhhkkQmrtzOncbYWLmJHgs3+xLdLpcm7hacBG1jN/ZP4cgpDxZs8rtYePvtxuLod96xLjAhxAWSyMSV270b2rY1Zi2ajpxyJ/loE3qEZ1sYmO30jcyipXc+k+eUmfQRGmqsK5s82ehaFUJYShKZuHK7d/9uf8WFm4xFxD0dJJE5O8PoPmms3uXNnp+bXHzh9tuNJPb++9YFJ4QA7JzIlFIjlFL7lVKHlFJPVvB6I6XUTPP1LUqpkDKvPWWW71dKDa+uTqVUqFnHQbNOt6raUEq5KqWmK6V+VErtVUo9Zb+fhANKSzOObmnf/pLiRVt8CfTLo41/vkWB2d71PdNo5FrMO9+WOcK9Y0fo2RPeegtyc60LTghhv0SmlHIG3geuBcKB8Uqp8HKX3QtkaK07AJOAV817w4FbgAhgBPCBUsq5mjpfBSZprcOADLPuStsAbgIaaa2jgHjgz2UTqajGnj3G5zKJ7FyeEyt3NqdHl7P1bjePqjRrUsywhAy+XNaSMxllNka+7TYjoX/8sXXBCSHs+kTWHTiktT6stS4AZgCjy10zGphufj0bGKKUUmb5DK11vtb6F+CQWV+FdZr3DDbrwKxzTDVtaKCJUsoF8AAKAMfoD7sadu82PpfpWly1szl5Bc4O061Y1riBKeQXOhlnlZWKjITYWGOBdL7jPIEKUd/YM5EFAsfKfH/cLKvwGq11EZAF+FZxb2XlvkCmWUf5tiprYzaQC5wEfgXe0FqnX9lbbYD27AEfH+PDtHCzLx6Niuvtbh5VCW6RT5/ITN6fG2icVVbqttuMLtbPP7cuOCEaOHsmsoo6l8ofs1vZNbYqr6qN7kAxEACEAn9TSv3uZEil1P1Kqe1Kqe0psvP5ReUmemgNi7f60DUsBzcXxzxN+eaBKaRluzJ9SZkF0vHxxnllr7wCRUWV3yyEsBt7JrLjQJsy3wcBJyq7xuzi8wLSq7i3svJUoLlZR/m2KmvjVuAHrXWh1voMsAFIKP8mtNZTtNYJWusEf3//Gr95h1ZUBElJl4yPHfrNgyOnPOjWyfG6FUtFtculS3Aub80KurhAWinjqezwYZg1y9L4hGio7JnItgFh5mxCN4zJG/PLXTMfuMv8ehywUmutzfJbzBmHoUAYsLWyOs17Vpl1YNY5r5o2fgUGK0MToCewz4bv33EdOGCMCZV5Iis9u6u+7+ZRFaXg5kFnOHSiMd+tL/NHTe/extqyl182DhoVQlxVdktk5njUg8ASYC8wS2udpJR6QSk1yrzsU8BXKXUIeAx40rw3CZgFJAM/ABO11sWV1WnW9QTwmFmXr1l3pW1gzH70BH7CSJDTtNZ77PCjcDwVzFhcss2bQL88Av0KLArq6ugXnUWQfx4vfxmMLu1BdXKC8eONp9QFCyyNT4iGSGntmOMZ9pCQkKC3b99udRjWe/ppY0xo8WJwdaWgUOEzqi/XxKfzyDjHP6tr8RYfXpsRzML/7OG6nub8oOJiuPNOaN0atm3DodYfCFFLSqlErfXvhm5sRXb2EJcvORmCgsDVWFO14ScvcvOcHbpbsayhCem09M7n35+3vfhU5uxs7PaRmChPZUJcZZLIxOVLSjJOTDYt2eaDi3MJXR1w2n1FXJxh/JAzbN7rxaqdzS++MGyYkeCffVbGyoS4iiSRicuTnw8//3zJjvdLtnoTEZJLYwfY7b6mru2ejl+zAp77LOTSp7I77zSWJsyda2l8QjQkksjE5Tl40BgPatsWgDMZruz6uWmD6VYs5eaquXXoGdb92Jyl27wvvjB4sPG0+q9/yVOZEFeJJDJxeZKTjc9mIivtWovv2LASGcDInmm09snn/33S7mLOcnaGu+6Cn36C2bOrvF8IYRuSyMTlSU42ppu3Mdalr9zpjadHEWFB5y0O7OpzddHcNeIUOw42Zc7aMuvKBgww1pU99xwXV04LIexFEpm4PMnJxhTzRo0AWLGjOTHtc3FuoP+SronPILT1eZ6eGkpRsTnlvvSpbO9emDHD2gCFaAAa6K8fccWSki50K/56uhE/n2hM17CG161YytkJJlx7kgPHGjNlQeuLL/TrBx06GE9lhYWWxSdEQyCJTNRcUZEx2cOcsbhypzHJIS6sYUy7r0yfyGy6djjLs9NCyThrbvfp5AT33AOHDsH06VVXIISoFUlkouZ+/tl4ujCfyFbuaE5zz0JCWuVZHJi1lIKJY38j46wLz08PufhCr14QHg7PPy/nlQlhR5LIRM2VmbGoNazY4U3XsBzZjQloH5DH9T3TeH9uAHuPNjYKlYIJE+D4cfjoI2sDFMKBSSITNVeayIKDOXDMgxNpjYhrwONj5U247iTubiU8/G6Hi4uk4+Oha1d46SXIzbU0PiEclSQyUXPJydCqFXh4XBgf69rAx8fKau5ZzITrTrE80YdZq8pMx7/3XjhzBt5917rghHBgkshEzZWZsbhyR3NaehcQ4OvYx7ZcrlG9U+kYdI5H3u9Adq6zURgRAT17wmuvQWamtQEK4YAkkYmaKS6G/fuhbVtKSmDlLm+6hp2V8bFynJ3gkXHHOZ3hxr8+C7n4wr33QkYGTJ5sWWxCOCpJZKJmjhyBvDxo25YfDzchPdu1wex2f7m6tD3HDb3SeOfbIHYd8jQKO3SAPn2MRJadbW2AQjgYSWSiZkoneoSEsGKHjI9V577rT9KscREPTAq7uA/jHXcYT2UffmhpbEI4GklkombKzFhcudOb4BZ5+DeXHSsq07RxMX++4QSbk72Yutjc8aNTJ+jeHd58U2YwCmFDkshEzSQng78/he5NWbPbi1h5GqvW8G4ZRLfL4R8ftSM1yzhNm9tvh5QUmDbN2uCEcCCSyETNmDMWEw80Jee8C3EdZP1YdZQyJn5k5zrz5JR2RmFUlLHbx+TJcl6ZEDYiiUxUr6QE9u2Dtm1ZscM4fyxWJnrUSGjrPMYNSOHTRa3Z+FMzo/APfzD2YFy40NrghHAQkshE9Y4dM8Z02rZl5Q5vwgLP4eUp52zV1F3DT9OieQF/mdTROOqlf39o0QLeftvq0IRwCJLIRPX27gUgP7AdG5OaEdNensYuh0ejEiaO/Y0fD3vy3neB4OICY8bAypXw449WhydEvSeJTFR9yzfZAAAgAElEQVTPnLGYWBhFXoEz0e1lxt3l6heVRbfO2bwwvS2ZOS5w3XXg6goff2x1aELUe5LIRPWSk8HHh3WHAwGIaidPZJdLKbh/5Ekyclx5fUYb8PKCvn3hyy+NheZCiCsmiUxUz5yxuHZ3c9q2PE9zGR+7Ih0CzzO4awZvzw7iVLqb8VSWkQFz51odmhD1Wo0SmVJqjlLqeqWUJL6GRmtITqa4TQgbfvIiqp10K9bGPdeeJL/QiZe+DIa4OOM0gU8/tTosIeq1miamD4FbgYNKqVeUUp3tGJOoS06ehOxsfmzSk6xcF6IlkdVKkH8B1/ZI46MFARxL9YARI2D5cjh61OrQhKi3apTItNbLtda3AXHAEWCZUmqjUuoepZSrPQMUFjMneqzL6wZAtMxYrLXbrjlNSYninW8DYdgwo3DWLGuDEqIeq3FXoVLKF7gbuA/YCUzGSGzL7BKZqBtKE9mpMFp659PSW/ZXrK1WPoX0j8lkyoIAspsFQefOMHOm1WEJUW/VdIzsW2Ad0Bi4QWs9Sms9U2v9EOBZxX0jlFL7lVKHlFJPVvB6I6XUTPP1LUqpkDKvPWWW71dKDa+uTqVUqFnHQbNOtxq0Ea2U2qSUSlJK/aiUcq/Jz6NBSU5GN23Gmr0tpFvRhv448AzZ51z4ZGFrGDQIEhPh55+tDkuIeqmmT2SfaK3Dtdb/0VqfBCNBAGitEyq6QSnlDLwPXAuEA+OVUuHlLrsXyNBadwAmAa+a94YDtwARwAjgA6WUczV1vgpM0lqHARlm3VW14QJ8CfxFax0BDATkcaO8pCQOte7HmUw3mehhQ52CzxPT/iyT5wRR2HuAUfjNN9YGJUQ9VdNE9mIFZZuquac7cEhrfVhrXQDMAEaXu2Y0MN38ejYwRCmlzPIZWut8rfUvwCGzvgrrNO8ZbNaBWeeYatoYBuzRWu8G0Fqnaa1lXnlZWkNSEuvchwIyPmZrNw9M4dcz7szeb24kLN2LQlyRKhOZUqqVUioe8FBKdVVKxZkfAzG6GasSCBwr8/1xs6zCa7TWRUAW4FvFvZWV+wKZZh3l26qsjY6AVkotUUrtUEr9o5r30/CkpEBGBmsLetDcs5DgFvlWR+RQeoZnE+Cbz8ffm92Lu3YZmwkLIS5LdU9kw4E3gCDgLeBN8+Mx4P9Vc6+qoEzX8BpblVfVhgvQF7jN/DxWKTWk/IVKqfuVUtuVUttTUlIqqMqBmRM91p7pTFRoLqqin6S4Yk5OMKJ7Oqt2eXO4g/HUy/ffWxuUEPVQlYlMaz1daz0IuFtrPajMxyit9bfV1H0caFPm+yDgRGXXmGNWXkB6FfdWVp4KNDfrKN9WVW2s0Vqnaq3PAYswZmGW/xlM0VonaK0T/P39q3nLDiY5md8I4Jf05jI+ZifDu6WjlGb6zhho21aOdhHiClTXtXi7+WWIUuqx8h/V1L0NCDNnE7phTN6YX+6a+cBd5tfjgJVaa22W32LOOAwFwoCtldVp3rPKrAOzznnVtLEEiFZKNTYT3AAguZr31LDs3cu6RjI+Zk8tvAtJ6HiWz35oRUmPXrBmDZyVQ0uFuBzVdS02MT97Ak0r+KiUOR71IEbC2AvM0lonKaVeUEqNMi/7FPBVSh3C6K580rw3CZiFkVh+ACZqrYsrq9Os6wngMbMuX7PuqtrIwOgu3QbsAnZoreXP4bKSk1nXeDiNGxXTIeC81dE4rBHd0/n1jDsrfcZBYSEsk6WZQlwOZTyciJpISEjQ27dvtzqMq6dVK6JyN+Me6MPrfzlsdTQOq6BQMe5fEdzQK4WvtnWCceNg6lSrwxLCZpRSiZUt1bKFmi6Ifk0p1Uwp5aqUWqGUSi3T7SgcUXo66acL+CknhBg5f8yu3Fw1g7pm8t2GFuR27QuLFkFJidVhCVFv1HQd2TCtdTYwEmOSREfgcbtFJay3dy8b6API+WNXw8DYTM7nO/ODz61w+jTs3m11SELUGzVNZKUbA18H/E9rnW6neERdkZzMWvrj6lxMl+BzVkfj8KLb5dDcs5A5Kf2NghUrrA1IiHqkpolsgVJqH5AArFBK+QNyrK0jS05mg+pH5+DzuLnKOKq9OTtDn8hsvt8RQH5wmCQyIS5DTY9xeRLoBSRorQuBXH6/3ZRwIHk/HiRRxxERKuNjV0v/6EzOnndhWcBdsHYtFBRYHZIQ9cLlnPjcBfijUupOjPVYw+wTkqgLEne7UIAbESGSyK6WrmE5eHoUMTtvJJw7B1u2WB2SEPWCS/WXgFLqC6A9xnqr0o11NfC5neISVsrOZmNqGAARITI+drW4umh6RWQzf28XCpUbritWQL9+VoclRJ1Xo0SGMTYWrmXRWcOwdy8b6U1wswy8mxZVf72wmQExmSzb7sPqNrczdMUKeO45q0MSos6radfiT0ArewYi6g6dlMwG+hDZVrZKutriO57FzaWERY3/AJs3Q6507QpRnZomMj8g2TzyZH7phz0DE9b5eeNpUmhB507yAH61ubtpYjrksDitBxQVyTiZEDVQ067F5+wZhKhbNm4zlg1GtpP9Fa3QvXM2788N4hdCCV2/HgYPtjokIeq0mk6/XwMcAVzNr7cBO+wYl7DQhsOtaeacQ9uWslTQCj26GF26i/3vgHXrLI5GiLqvpnst/gmYDXxkFgUCc+0VlLBQbi4bc6Lo6n0Up8tZnCFsJsg/nwC/fBY7j4RNm4wuRiFEpWr6q2oi0AfIBtBaHwRa2CsoYZ3M7YdIIoLINplWh9JgKWV0L65MiyEvtwh27rQ6JCHqtJomsnyt9YVtBsyDKGUmgAPasjAVjRNdZKKHpbp3Psu5QjfW0U+6F4WoRk0T2Rql1P8DPJRSQ4FvgAX2C0tYZcNGhRPFtIvysDqUBq1rmDENf3GTm2D9eqvDEaJOq2kiexJIAX4E/gwsAp62V1DCOhv3+xLlsg+Pxs5Wh9KgubtpotrlsEwNNZ7IZC8CISpV01mLJRiTO/6qtR6ntf5YdvlwPEVFsCWtPfFeh6wORQBxYTn8lBPK6VQnOCwndAtRmSoTmTI8p5RKBfYB+5VSKUqpZ69OeOJq+nF7Pjnak5iAFKtDEUBcR2Ma/ioGycJoIapQ3RPZIxizFbtprX211j5AD6CPUupRu0cnrqqN84wE1iWs0OJIBEBY0Hk8PYpY6TxUEpkQVagukd0JjNda/1JaoLU+DNxuviYcyMY1hQTwG806yMqKusDZCWLa57LCeZixnkwIUaHqEpmr1jq1fKHWOgVwtU9Iwiobk7zoxWbyWgRbHYowdQ07y+GCNhzZlQn5+VaHI0SdVF0iq+qIWjm+1oGcOAFHsn3o1mw/2ln+Rqkr4sJyAFhZ2Bd27bI4GiHqpuoSWYxSKruCj7NA1NUIUFwdGzcan6Nbn7E2EHGJkFZ5+Hrms5LBMk4mRCWqTGRaa2etdbMKPppqreXPdgeycXU+7pwntJ3VkYiylIKYjudYoYaiN222Ohwh6iTZFlYAsGFVAd3ZSmGgZLK6Ji7sLKd0S/ata2DLIkpKYN48mDED8uQkBlE5SWSC8+dh5/7G9GYjua07WB2OKCe2vTFOtua39pDSQJLZmjUQHQ1jxsD48RAYCB99VP19okGSRCbYvh0Ki53p4ZJIXvNWVocjygnwK6ClZy6rGQhbt1odjv0dOQKjR0NmJjzzDLz5JrRtCw88AEuXWh2dqIMkkYkyEz1SkEPI6h6lILrDOVYz0PHHyQoL4dZbjf3SXn/dOB07Lg5eeglCQ43Xjh61OkpRx8hvLcGGDZqOTgdxD/S1OhRRiZhO5zlNK/avOmF1KPb12mvG4u/HHoPWrS+We3jACy8YY2V//at18Yk6SRJZA6c1bFyv6VOyTsbH6rDScbLVO5oZkyAcUU6O0Y3Yp4/xJFZeYCDccgssWiSHjYpL2DWRKaVGKKX2K6UOKaWerOD1RkqpmebrW5RSIWVee8os36+UGl5dnUqpULOOg2adbtW1Yb4erJTKUUr93fY/gbrv4EFIy3CSiR51XIBfAS0bZ7M6rwfs3291OPbxySeQkWF0H1ZmzBjw9ISXX756cYk6z26JTCnlDLwPXAuEA+OVUuHlLrsXyNBadwAmAa+a94YDtwARwAjgA6WUczV1vgpM0lqHARlm3ZW2UcYkYLFt3nX9Uzo+1ocN5LaSRFZXKQVdQzJZwwD0ZgdcGF1YCG+9BTExEF7+10QZnp5GMpszB/buvXrxiTrNnk9k3YFDWuvDWusCYAYwutw1o4Hp5tezgSFKKWWWz9Ba55sbFh8y66uwTvOewWYdmHWOqaYNlFJjgMNAkg3fd72yYQM0d80l1DOVwqY+VocjqhAZoTlFaw4sPWJ1KLY3YwYcO2Z0HVZn3Dhwc4NJk+wfl6gX7JnIAoFjZb4/bpZVeI3WugjIAnyruLeycl8g06yjfFsVtqGUagI8ATxf1ZtQSt2vlNqulNqe4oBreDZuhG5uuznfWhZC13UxYbkArF7vYnEkdvDppxAUBD16VH+tlxf07w+zZslCaQHYN5GpCsrKnypd2TW2Kq+qjecxuiJzKnj94oVaT9FaJ2itE/z9/au6tN5JS4PkZBiQv4TcVu2tDkdUI9CvgJaNMlj9WwdjFbujOHYM1q6Fa64x+lBrYuhQyMqC77+3b2yiXrBnIjsOtCnzfRBQfu7whWuUUi6AF5Bexb2VlacCzc06yrdVWRs9gNeUUkcwDhD9f0qpB6/srdZPpeNj/YpWkRsg42N1nVIQH3iK1XoAeocDzdqbMcOYPnvNNTW/Jy4OfH3hyy/tF5eoN+yZyLYBYeZsQjeMyRvzy10zH7jL/HocsFJrrc3yW8wZh6FAGLC1sjrNe1aZdWDWOa+qNrTW/bTWIVrrEOBt4GWt9Xu2/AHUdevXg6tzCd3YJhM96omo0nGyhQetDsV2vvrKmOARWH7koQrOzsYU/UWLjK4F0aDZLZGZ41EPAkuAvcAsrXWSUuoFpdQo87JPMcarDgGPAU+a9yYBs4Bk4Adgota6uLI6zbqeAB4z6/I16660DWEksijfE3iQJ12L9USkeXjS6uWF1gZiK0lJsHt3xevGqjNsmDHbcdYs28cl6hW7jhprrRcBi8qVPVvm6zzgpkrufQl4qSZ1muWHMWY1li+vtI0y1zxX1euOKC/P2GPxvlY7Oe8bSLF7E6tDEjUQ6FdAK9dUVu9tyZ+tDsYWZs0ytkUbNOjy723fHtq0gblzjX0YRYMlO3s0UNu3Q0EB9M9bSm5LeRqrL5SC7v5HWJ2TgE51gC61+fMhIgJ8rmDph1LQuzesWgXZ2baPTdQbksgaqPXrjc+D0maT21oSWX0S0/E8p2jNwe9+sjqU2jl+HHbtgl69rryO3r2N7sUlS2wXl6h3JJE1UOvXQ7uA87QoPkVOYCerwxGXoXN8YwBWz6/nTyGlU+drk8giIox1ZfPLzyMTDYkksgaopMTY0SPe71cAcgI7WxyRuBytA51p5XSa1YlNrQ6ldhYsgIAA46yxK+XsbCyiXrTIOPpFNEiSyBqg5GTjzMLerlspbtSY835tqr9J1BlKQc/m+1l9qjO6pPweA/VEbi6sWGE8jdV0EXRleveG9PSLCyNFgyOJrAEqHR8bmLOAnIAwOUyzHooLSeekbsXBVcetDuXKrFgB+fm161Ys1a0buLgYT2WiQZLfYA3Q+vXg56eJOLpYuhXrqfAYY+XM6hmnLI7kCi1dCu7uEB1d+7oaNzYWVC9fXvu6RL0kiawBWr8eYtrl4JqXw1mZ6FEv+Ya3pDUnWL3O2epQrsyyZcaRLa6utqkvPh527JBdPhooSWQNzLFjcPQodPM5BCAzFusrF1f6NNnN6sPB6Po2THbsGBw4YCQfW4mPN/ZrXLnSdnWKekMSWQOzYYPxuS8bKHF2kVOh67GEgN84WejHwb31bLZeaRegLRNZ587QpInxpCcaHElkDcz69caQQkLaYs61bId2cbM6JHGForoUA7BmxkmLI7lMy5eDtzeEhtquTmdniI2VRNZASSJrYNavh/BwjfehRHICOlodjqgF78gAY5xsSb7VodSc1kayiYur/bT78uLj4cgR+Pln29Yr6jxJZA1IVhbs2QOx7bJxyzjN2TbhVockaiHfL4h+zptY/ZNv/Rkn++knSEmBhATb113aVSmzFxscSWQNyKZNxh/EPRvvAeBscITFEYlaUYrufoc5cc6bg/XleLLSrr+4uN+9VFIC63/04q+Twuj7UFfG/7sLT38ayi8n3WtWd5s20KKFdC82QJLIGpD1642hhN7nllPi7CIzFh1AXAdjv8XlC/MsjqSGli+H4GAj4ZTx0y9NiL43gX4Pd2Xq4lZk5TqzdndzXvk6mMh7uvHut4GUlFRTt1JGgly5EoqL7fceRJ0jiawBWbMGwsKg5c8byW3dgRLXRlaHJGrJp3ML2vEzP8zOtTqU6hUUGP8IyzyNaQ3TFrei+wNxnExrxJO3HuW7fyfx7sOH+OrpvXz1dDKRobk8/G4Yo/4ZRWFRNeNqCQmQkWGsKRMNhiSyBuLcOdiyBWJjNU33b+dsG+lWdAQ5bSMYwQ+s3N6UggKro6nG5s3GP8Qy0+5f+LwtE17rTJfgc3z89/0M75aBR6OLj14tvQt55f7DPDT2OAs3+/LQO2FVjweWJkkZJ2tQJJE1EBs3Gsc2dW9zEtecTJno4SAKm/owqOk2cgvcLqwRrLOWLTP29YyNBeC1/7Xhuc9CGdE9jdf+8jM+zSpeD6cU3Ng/lVuHnOajBQFMnhNUeRve3tChgySyBkYSWQOxapUxPtYX47edTPRwHPEhGbhSwA8/WB1JNZYvNxYue3rywdwAnpjSnsFdM/j7H4/hXIPfRPded5L+0Zk89kF7Nv7UrPIL4+KMAeFz52wXu6jTJJE1EKtWQadO0OqXTRS7NiK3VTurQxI2Uhzann6sY/GCQqtDqVxWFmzdCvHxrEhszsPvhtE7IounbjtaoyQGxsPck7f+ir9XIX99uyNFxZWMl8XHG+Nx69bZLn5Rp0kiawBycmDbNqNHp+n+beQEdkI722izVmG5s8GRjOAHftzryokTVkdTidWroaSEX9oO5OYXImjTIo9/3n4Ul8vc89ijUQl/Hf0bu382nuoqFBVlbEa8YkWtwxb1gySyBmDDBuPw3LjoImOiR3Ck1SEJGzob1IXhylg7tWSJxcFUZvlychv5MPqrmygsVLw44Rcau1c3n75i/WOy6NYpm2emhnIyrYIt1jw8ICJCxskaEElkDcCqVca5gz3cd+NckEdWaKzVIQkbKmnkQUjrPFq7ptbZsyX10mVMaDKTpCOePH3HUQL9r3yKpVLw8B+Oc77AiWemVrJfY1wc7NwJqalX3I6oPySRNQCrVkGXLtDyoHE0dFZojMURCVs72y6WUSVzWbxY1705DseO8dqB0cxKv4b7rj9J9y5na11lkH8BI3ulMX1Jy4p3/iid4i/HujQIksgcXFYWJCYa42NeP20gzyeAAq8W1d8o6pWs0BhuKv4fubmqznUvLp60j6f4D0M7/8otg8/YrN7xg8+gFLzydfDvX+zUyTjWRcbJGgRJZA5u1Spjt574OI3XTxvICrHB0fKizskK7coA1uDtfp45c6yO5qL9+2H8e72Jckri0bsybLrhvX/zQq7rkca0H1rx6+lyu9SUHusi42QNgiQyB7d0qXH+WFf/YzRKO0F2iHQrOqJ871YUefszovkmFiyA/DpwsktmJoy6QeNWdJ5Pu7yJh7vtt+gfP+QMWlfyVBYfD4cPGx/CoUkic3BLlhh/mPrtMxZCy0QPx5UVGsstuVPJzrb+QaS4GMaPh19+0czRY/GMsuEhmmW09C5kRPd0Pl3UmtPp5ZaUlG5XJd2LDk8SmQP7+Wfjj9GEBGiWtJHiRo3Jbd3B6rCEnWSFxjLi7Cw8G5dY3r345JPwww/wbJ+V9GM9GR172K2tmwakUFDkxJTvy60rCw4Gf3/rs7qwO0lkDmzpUuNzt27gtWc92cGRaGcXa4MSdpMVGosbhQxqd5R587BsE+HPP4c33oAxY+CBvEmcaxlKvncru7UX3DKfbp2z+WBeAAWFZQbhlIKuXY2Zi9WeASPqM7smMqXUCKXUfqXUIaXUkxW83kgpNdN8fYtSKqTMa0+Z5fuVUsOrq1MpFWrWcdCs062qNpRSQ5VSiUqpH83Pg+33k7DG0qXQujW0bZqO5+HdZHaIr/4mUW/ltu5AkbsnN3l8T3o6zJ9/9WPYuBHuv9/IHw/eX0Dz3WvICOtu93b/0D+FU+mNmLPW/9IX4uONtWR79tg9BmEduyUypZQz8D5wLRAOjFdKld9y/V4gQ2vdAZgEvGreGw7cAkQAI4APlFLO1dT5KjBJax0GZJh1V9oGkArcoLWOAu4CvrDl+7daYaExNBAfD9571qC0JqOD/X+hCAs5OZPVritjTnxAy5bw0UdXt/mkJBg50ujN+9e/wOfgFpzzcu3arViqW6ezBPnn/X5nfDnWpUGw5xNZd+CQ1vqw1roAmAGMLnfNaGC6+fVsYIhSSpnlM7TW+VrrX4BDZn0V1mneM9isA7POMVW1obXeqbUu3ZkuCXBXSjnMSZNbtsDZs8b4WPOdKyl285Ad7xuAjLBuNP1tHzcMyGb5cjh06Oq0++uvMHy4Mev99dfBywu8ty9DKycyOiTYvX0nJxjbN5Ute5uxdW/Tiy/4+UFIiCQyB2fPRBYIHCvz/XGzrMJrtNZFQBbgW8W9lZX7AplmHeXbqqyNsv4A7NRa14FJy7axeLHxSyUuDrx3riIrNBbtIhsFO7rMDt0AuL3lMpyd4eOP7d/mb7/BkCHG4vtXXoFW5nCYd+JysttGUuzRtOoKbGR493Qauxfz7nflfs107Qpr19aNNQnCLuyZyCpa+lh+IUll19iqvNo4lFIRGN2Nf67gOpRS9yultiultqekpFR0SZ00b56xCbhP4WmaHEkiI6yb1SGJqyAnoCOFjb3oeGgRvXvDtGn2nfRx8iQMGmR8fuUVaN/eKHfOyaLZvq1XZXysVBP3EkZ0S2fmqhacSi+zmXBCApw/b5xRJhySPRPZcaBNme+DgPKHTFy4RinlAngB6VXcW1l5KtDcrKN8W5W1gVIqCPgOuFNr/XNFb0JrPUVrnaC1TvD396/okjrn8GFjvKJPH2i+azVw8S914eCcnMhsH0fznasYORJSUmD27OpvuxK//WYksePH4T//MTacL+WTuAxVUkxGp172abwSY/ulUFjkxEcLWl8s7NrVONZl8eKrGou4euyZyLYBYeZsQjeMyRvl51HNx5hoATAOWKm11mb5LeaMw1AgDNhaWZ3mPavMOjDrnFdVG0qp5sBC4CmtdV0/JP6ylM5W690bvHeupMi9CTlBna0NSlw1mR0S8Dj1C32DjhAaCs89Z0z+saVDh4w/lI4fN57EoqIufd1n80IKGzcj+ypviRbkX0CPLll8MC/w4lR8Dw+IiZFE5sDslsjM8agHgSXAXmCW1jpJKfWCUmqUedmngK9S6hDwGPCkeW8SMAtIBn4AJmqtiyur06zrCeAxsy5fs+5K2zDr6QA8o5TaZX44xG668+ZBu3YQ0Frjs20Jme3jZf1YA1L69O2zexX33QcHD8Knn1Zz02XYvRv69jW2oHrzTYgun6tKSvDdvIj0Tr0s+Xd3Y/9UzmS48c3qMj0oPXpAcjIcOXLV4xH2Z9d1ZFrrRVrrjlrr9lrrl8yyZ7XW882v87TWN2mtO2itu2utD5e59yXzvk5a68VV1WmWHzbr6GDWmV9VG1rrF7XWTbTWsWU+bLc1t0XS040T3nv1gsZH9+J++ihp4f2sDktcRbmt2lPQ1Bfv7Uvp1ctINM89Z5wUXluLFxtJTGuYPNnYZL68pgcSccs8Q7pF/+4SOp4luEUeb5edit/dHKuTpzKHJDt7OJhFi4x97vr0Ad8tximL6V36WhyVuKqcnEjr0gefrUtwKini/vvh9GmYNOnKq9QaPvwQbrjBWGT/3nvQtm3F1/puXohWivTOva+8wVpwcoIx/VLZvr8ZW5LNGZNt2kBAAHX25FFRK5LIHMz8+cbSmU6djHGKnIAwu24PJOqm9M59cM3JoGnyFiIioH9/eOkl2Lr18us6fx7uvRf++ldju7O33zYWPVfGZ9NCsttGUejpfeVvoJaGJ6TTxL2Yd78zn8qUMroXV6yAvDzL4hL2IYnMgeTmwsKFRrei67ksvH5cT5o8jTVIGZ16op2c8d1qdKU99hj4+Bj7H54oP3e4Cvv2GU/306bBHXfAiy8axwJVxi3tJM0ObLe8O7uxewnDu6Uza7X/xan4PXsaWVkWRzscSWQOZMECOHcOBg82pj87FRdJt2IDVdS4GVkh0fhsNrrSvLyMJJSZCWPHGru+VHl/kTEbMTbWOEXh5ZdhwgRjkX1V/NZ9B0Bq1CBbvI1aGdM3lcIiJ6aUTsXv2hU8PeHbb60NTNicJDIH8vXXRpdPdDT4bvqeQo+rP/1Z1B3pXfrQ9NBO3NJOAsZM1qeegu3bITLy4ukIZRUWwmefGdPpn3rK6I2bNs14yq8J/zWzyW3ZjnOt2tvujVyhNi3y6dEliw/nm7viu7oaT2Xz5xuZWjgMSWQOIj3dOP9p0CBwLi7Ad8M80iL6y7T7Bqy0W7n0qQygXz945x1jyGj4cGOt4QMPwLPPwujREBQE99xj/J7/97/h+eeNLsmacM04Q/M9a0iJrjsHSdzYL5VT6Y2YucpcWdOvH6SlGVN7hcOQ33IOYs4c46/pIUOMzVpdczI5EzvM6rCEhXIDOnLeJxD/tXM4df29F8ojImDKFJg5E7Ztgy+/NMZXg4ONp/khQ4wnMVXR5m5V8Fs/F1VSQkrMNTZ+J1euW+ezhLY+z+sz2nD70NOobt2gUSOje3GQ9d2fwjYkkTmIr782fhGFhRGyUZkAABMCSURBVEGLObMo8mhKRqeeVoclrKQUKTHXELT2K1zOZlDU9OIsQjc3Y/LGHXcYU+sLC42y2vBfO4fzfm3IDehYy8BtRym4eWAKr/4vmKXbvBneHWNN2XffGQvhnKRTyhHIf0UHcPw4rFljTPJwKszHb/1cUqIGyW73gpTYoTgVF+G3fm6l1yhV+yTmmnGG5jtXkhI95PIf5exsSFwGfl4FvD4z2Cjo39/YKFI2EXYYksgcwNSpxl/V11wDPtuX4nIumxTpVhTA2TbhRvfi6m/s2k7LFV/jVFzEqYSRdm3nSri6aG7sl8qKHd7sOOBprCfw8IAvHOos3QZNElk9V1honATcrRsEBkLLZV9S2MSLjI5yGrTgQveid+IyXLLT7dOG1rRaPI3s4AjOtbZ+tmJFbuidRhP3Yv7zdbCRxPr1g2++kcXRDkISWT23YIGxwHX0aHDNTMFv/Xecjr8e7SzdisJQ2r3ov8Y+57l4HtqF5+E9nOo2qvqLLeLpUcyN/VOYvaYFuw55wrBhxkmgCxZYHZqwAUlk9dyHH0LLlsbymJZLP8epqJATPW+0OixRh5xtE05O6w4EfD/FLvW3+uEzSlxcORM3wi7128rNA1No6lHEs1NDjJXefn7SveggJJHVY/v3G7vtjBwJzk6agAVTyAqNqbPdO8IiSnGy5400PZCI5/5Em1btlHeOlsu+JDVyEEWNm9m0blvz9Cjm5kFnWLDJjy37mxuDyosWGRM/RL0miawe++ADcHGB664Dr91raXz8ACflaUxU4HS3kRS7utv8qazV0s9xPZvOb31vtmm99vKH/qk09yzk6amh6JE3QEkJ/Pe/VoclakkSWT116pSxqHXIEGPnhaBvJ1Po0YwzsUOtDk3UQUUeTTnTdRgtVnyN87lqNlqsqZISgr6ZRHabCLLaxdmmTjvzaFTCbdecYXmiD/N+iTb23poyBfLzrQ5N1IIksnrqtdeMGYt33AGNjyTjv+47fut7MyVuHlaHJuqoE73H4XI+h9YLP7FJfb6bvqfx8QMcG3RHnVs7VpUxfVNoF3CehyZ3IOe6m+HMGZg1y+qwRC1IIquHTp0yJnkMHWpMuQ/+36sUu3nwW/9brQ5N1GFn20aREdad/9/emYdHVWQL/HeSCGEJyGYAAVljjCAgm7g9cUYj+hjAEYkDI44L7oAKo4g+FfVTeIqO6MCgoyKPTzY3fKNiRnyfMw47hoBsSUjEsMgSQWAgIUm9P6riNEw6hCa3u29zft/XX9+uW/dUna7bfW7VPfec1nMmE1d8+NSEGUObOZM50rgley74Rc10MEwkxMOYXxdSuCeRp7IH2wyhf/iDfRhT8SVqyHxIxWxs+HBI3FlA8l9ns/2i6yOayFDxBwXpI6ldtJOWH//plOQ0+cfHNFz3NVv7jfBlYOou7Q9xbZ+9vLSgNVmXj4JVq8KePbqsDEpK7Lva0FNDDZnPyM8/djbW9u0nMXFxFPb7baS7pviA/R168GPHXrR+dxJxR/4ZkgwpPUqH6eM4lNyOHX3961w0csB2GiUdZcgXd7Ev+VybAsBDi7J5M0yZYp/5TEmBxEQbvzghAZKSbKDm22+3AcAPHfKsGzGJGjIfYYxNNx8XZ5McJm1cQfNFMym8fBjFZyZHunuKTyjofze1i3bS9p2JIR3fcuF06hZuJm/AA76cjVXQsF4ZT4wooOCHRG6u/z7lq7+BD4PHpAyF/fvh1Vdt/rdzz4WHHoKsLGjRAm68EW67zabNSU+3qXPmz4cbbrB5BYcPh9Wra7Q7MYt/z8LTkPnzbc6xe++FZk0NHZ8YRUlSE7676vZId03xEfvbd2dHn0G0nvsCu/5jCAfP7VHtY+tsy6XdGxMoSulDUZr/s493bvdP7v7VdqZ+kMZTDabw1IQJcN11pxxFeds2ePFF6xB56BCkpsKoUdZJsnnz4MeVlUF2tg0C/uGHMHs2XHEFTJpkg/YrlaMzMp+wbx+MHm2v6gYPhuafvEnDDUvZct39lCXWi3T3FJ+RN/BBSpKakDr5VuJKqhdvUEqKSXtqKEaETRlP+MpTsSoGX7aH9F5FTPxpDOM3/Bbz3y+ELGvzZrjjDmjXziYwvfhi+5jatGnud1uFEQOIj4fu3WHMGJgzxyY9zc62y47DhsHWrSF3LaZRQ+YDjLFr57t2wQMPQP0dOXR6dTQ/duzFzl4DIt09xYeU1kli85AJ1N+SzXlP/wYpK636gPJyOr1yP0k5q9mY8STFjVqEp6NhQATGZWxlQN89PM947vyvZI6syz0pGatX26XC1FQb9eraa23C0kcftRefoVC/vpU5a5ZdZnzvPSvr8cfh4MHQZMYqash8wHPP2ZP4zjshtX0J5z39G8rjE9g47GlNDKiEzN7zLydn8Dia/f0DUl4YiZQerbSelJWSOvlWWv7ldb775a3s7RJ7mZXj4+CBIYXcfNkWXi+/jfN71mHh+6VV+n4cOWJ/l+np0KOHdXq86Sab5HbMmBPPvqpL3br2XtrMmTYDzTPPWGeR2bPV27ECMfpNVJuePXualStXhrXNTz6xsRSvvBImPGo4b9ItNP/8Hdb97gXfPb+jRCdtP51G289ncKBjdzaNe4ODKf+K0tFg/VLaTxvHmev+Tn7/u/nuqjtiZkkxGHn/u4EXv+jKBtJITYX+/W1Q7sREazjWr7fe+pmZ8NNPNvbw9dfDgAF2FuU169fD1KmwcaPNRjN1KnTt6n27p4KIrDLG9PRMvhqy6hNuQ5aZCYMGWTf7V16BtJkP02bOZPKvuYvv0u8MWz+U2Kdp9hekLHiOWgf2crh5Ow636kTiznzqFuZQktSELf85ip29ozdNS03T5v2XyPxbIrPaPs6K7a0oKTl2/9lnQ5cuNu5wt2723lY4KS+HTz+FN96wxvSee2DiRGgUpY+SqiGLIsJpyD74ADIyoHVrmPx8Gb3m/Z7W86ew7ZIh5Px6fMxfFSvhJ+HQPpJXf8aZOStI/HEHRxq35Ke2F7D94hsoq1030t0LK1JWSpcZ99MoZxlZo9/imy4jOHrUzshatQrPzKs6HDgAb70FH30EDRvC+PFw3302d2g0oYYsigiHITt6FJ59Fp5+2t44fuGxffR67Raafv0RhZdlkDtoLMSF+fJPUU5D4koO0/nNh2i8aQl5Iyfx/dCxUXtPOi8PXn8dli2zs8WxY633ZL0ocWhWQxZFeG3I1qyxN3VXrYKrfml4ps/HdJ12J7X27SZ34IMaS1FRwoyUlnDe/zzGWWsyKep5NZt+/2eKm7WKdLeCkpUFb79t/0saN4aRI63Hc4cIpyj02pB5enkhIteIyCYRyRWRRyrZX1tE5rr9y0SkbcC+8a58k4ikn0imiLRzMnKczFqhthFOjLFXUYMG2bX23FzDlKHLWPB9b3o/O5CjdRqyaswsNWKKEgFMQi3Wj5jEpiGP0XDNV/Qe3okO08ZSa3d0JuPs1g1eftk6gKSl2bisHTtCv342f+GOHZHuoTd4NiMTkXhgM3AVUAisAG4yxqwPqHMPcIEx5i4RyQAGG2OGikga8C7QG2gJ/BVIcYdVKlNE5gHvG2PmiMh0YI0xZtrJtmGMKQumU03NyPbvh+XLYfFimD+3nLz8OBokFjPy7E8Yt/NBzjpUwOEmrdh65S3s7PMrTPwZp9ymoiinRuLebbRd9CeSV/4FMOzr1o+iPv3Z3/kSDqT0wJxxatFAvGD3buv5vHjxvx6m7tzZGra+fa3hS0nx3lnFt0uLItIXeNIYk+4+jwcwxjwXUGeRq7NERBKAnUAz4JHAuhX13GH/JhN4HtgNNDfGlAa2fbJtGGOWBNMpVEOWl2evjLZ8mM2WPUnkl5+DIY54SrmSxQxhPkOZS516cexNvZRd3dP5MbWvr+PYKUqskrjne5JXfkLyN59Rd1cBAJtHv8b2QfdEtmMnoKAAvv7aLjuuXWufgwMbjatNG2jf3sZ4bNDAOo40aGCDGRtjQ2d16mSjd4WC14bMy3/Ks4HvAz4XAn2C1XEGaD/QxJUvPe7Ys912ZTKbAPuMMaWV1A+ljRrl8GH74GTrWslc0DSPGxOX0KNhDl2bFFK3WT2Km6Wy9Zx3KW7R7mdvxChxilIU5XiadqQodRRFw0eRsG839bdt5sil6SQlRbpjVdOli32BDVCcn29DauXlwfbtUFhon1E7dMhGDjl63PPxN94YuiHzGi8NWWX+4cdP/4LVCVZe2T29quqH0saxHRQZCYx0Hw+KyKZKjqsWe4GsUA/2nqbAnkh3wkNiWb9Y1g1Uv6hg3ryQE2k3Bc6p2d4ci5eGrBBoHfC5FbA9SJ1Ct+zXECg6wbGVle8BzhSRBDcrC6wfShs/Y4yZAcyohr6+RkRWejn1jzSxrF8s6waqn99x+rX1sg0vvRZXAJ2cN2EtIANYeFydhcAIt30DsNjYm3YLgQzncdgO6AQsDybTHfOlk4GT+VGIbSiKoig+wrMZmbsfdR+wCIgH3jTGfCsiE4GVxpiFwJ+BWSKSi50lZbhjv3VeiOuBUuDeCm/CymS6Jh8G5ojIM8A3TjahtKEoiqL4B30gWgHsvUC3jBqTxLJ+sawbqH5+Jxz6qSFTFEVRfE10Bg5TFEVRlGqihuw050RhxKINESkQkbUikiUiK11ZYxHJdOHJMkWkkSsXEXnF6ZYtIhcGyBnh6ueIyIiA8h5Ofq471tM0AyLypojsEpF1AWWe6xOsjTDo9qSIbHPjlyUi1wbs8zwsXQ3r11pEvhSRDSLyrYiMduWxMn7B9Iu+MTTG6Os0fWEdZvKA9kAtYA2QFul+naDPBUDT48omA4+47UeASW77WuBT7DODFwHLXHljYIt7b+S2G7l9y4G+7phPgf4e63M5cCGwLpz6BGsjDLo9CYytpG6aO/9qA+3ceRlf1TkKzAMy3PZ04G63fQ8w3W1nAHM9GrsWwIVuOwkbPi8thsYvmH5RN4Y6Izu96Q3kGmO2GGNKgDnAwAj3KRQGAjPd9kxgUED5O8ayFPusYQsgHcg0xhQZY34EMoFr3L4Gxpglxv6C3gmQ5QnGmK+w3rTh1idYG17rFoyBwBxjTLExJh/IxZ6flZ6jbmZyJbDAHX/891Sh2wLgF17MrI0xO4wxq932AWADNjpQrIxfMP2CEbExVEN2elNZGDFPwnTVIAb4XERWiY26ApBsjNkB9scHnOXKg+lXVXlhJeXhJhz6BGsjHNznltbeDFgSO1ndqh2WDqgIS+cZbumrO7CMGBy/4/SDKBtDNWSnN9UK0xVlXGKMuRDoD9wrIpdXUfdkw5NF+/cRC/pMAzoA3YAdwIuuvCZ1C6veIlIfeA8YY4z5qaqqlZRF/fhVol/UjaEastObaoXpiiaMMdvd+y7gA+yyxQ9uGQb3vstVD6ZfVeWtKikPN+HQJ1gbnmKM+cEYU2aMKQdex44fnLxuP4elO678GFlybFi6GkdEzsD+yc82xrzvimNm/CrTLxrHUA3Z6U11wohFDSJST0SSKraBq4F1HBuG7PjwZDc7b7GLgP1uGWYRcLWINHLLIlcDi9y+AyJykVuPvzlAVjgJhz7B2vCUij9fx2Ds+FX0x+uwdDWti2AjB20wxkwJ2BUT4xdMv6gcw5r2dNGXv15YT6rNWK+iCZHuzwn62h7r8bQG+Laiv9i18y+AHPfe2JUL8JrTbS3QM0DWrdib0bnA7wLKe7ofZh7wKi5ogIc6vYtdnjmKvQq9LRz6BGsjDLrNcn3Pdn9WLQLqT3D93ESAt2iwc9SdD8udzvOB2q480X3OdfvbezR2l2KXu7KxiS2yXF9jZfyC6Rd1Y6iRPRRFURRfo0uLiqIoiq9RQ6YoiqL4GjVkiqIoiq9RQ6YoiqL4GjVkiqIoiq9RQ6YoEUZEDka6D4riZ9SQKYqiKL5GDZmiRAkicoWI/J+ILBCRjSIyuyLit4j0EpF/iMgaEVkuIkkikigib4nNV/WNiPRzdW8RkQ9F5GMRyReR+0TkQVdnqYg0dvU6iMhnLgDz30QkNZL6K0qoJJy4iqIoYaQ7cD425tzXwCUishyYCww1xqwQkQbAYWA0gDGmizNCn4tIipPT2clKxEZHeNgY011EXsKGOnoZmAHcZYzJEZE+wB+xaTUUxVeoIVOU6GK5MaYQQESygLbYFBY7jDErAIyLsC4ilwJTXdlGEfkOqDBkXxqbQ+qAiOwHPnbla4ELXETzi4H5AWmeanusm6J4ghoyRYkuigO2y7C/UaHyFBZVJYsMlFMe8LncyYzD5oLqFnpXFSU60HtkihL9bARaikgvAHd/LAH4ChjmylKANthgrSfEzeryRWSIO15EpKsXnVcUr1FDpihRjrHp4YcCU0VkDZCJvff1RyBeRNZi76HdYowpDi7p3xgG3OZkfotNL68ovkOj3yuKoii+RmdkiqIoiq9RQ6YoiqL4GjVkiqIoiq9RQ6YoiqL4GjVkiqIoiq9RQ6YoiqL4GjVkiqIoiq9RQ6YoiqL4mv8HQ8zxM8Wh64MAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "homedf['income'] = np.exp(homedf['lnhhinc'])   # Creates income variable based off of the natural log\n",
    "\n",
    "\n",
    "income_data = pd.DataFrame(homedf, columns=['homeschool', 'income'])   # Subsets homedf dataframe to \n",
    "            # only homeschool and income\n",
    "\n",
    "not_homeschooled = income_data.loc[(income_data['homeschool']==0)]\n",
    "no_hs_income = pd.DataFrame(not_homeschooled, columns=['income'])\n",
    "no_hs_income.columns = ['Not Homeschooled']\n",
    "# Above 3 lines subsets the income data to only homeschoolers, takes only the income column, and \n",
    "# finally renames that column so that it fits for the graph legend\n",
    "\n",
    "homeschooled = income_data.loc[(income_data['homeschool']==1)]\n",
    "hs_income = pd.DataFrame(homeschooled, columns=['income'])\n",
    "hs_income.columns = ['Homeschooled']\n",
    "\n",
    "# plot of 2 variables\n",
    "p1=sns.kdeplot(no_hs_income['Not Homeschooled'], shade=True, color=\"r\")\n",
    "p1=sns.kdeplot(hs_income['Homeschooled'], shade=True, color=\"b\")\n",
    "p1.set(xlabel='Income', ylabel='Density')\n",
    "\n",
    "\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Quartile Ranges of Child's Age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.25     8.0\n",
       "0.50    11.0\n",
       "0.75    15.0\n",
       "Name: cage, dtype: float64"
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "homedf.quantile([.25,0.5,.75])['cage']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We will now be determining the frequency of homeschoolers by gender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Frequency Table for Homeschooling:\n",
      "0    715\n",
      "1    781\n",
      "Name: cmale, dtype: int64\n",
      "\n",
      "Probbility of being homeschooled by Gender\n",
      "       homeschool\n",
      "cmale            \n",
      "0        0.534266\n",
      "1        0.466069\n"
     ]
    }
   ],
   "source": [
    "# Now using matplotlib to chart probability of being homeschooled by gender\n",
    "\n",
    "import matplotlib.pyplot as plt   # imports matplotlib\n",
    "\n",
    "\n",
    "homeschool1 = homedf['cmale'].value_counts(ascending=True) \n",
    "homeschool2 = homedf.pivot_table(values='homeschool', index=['cmale'])  # Creates frequency (pivot) table to look at the\n",
    "                # number of people for each gender that has been homeschooled \n",
    "print(\"Frequency Table for Homeschooling:\")\n",
    "print(homeschool1)    # Prints frequency table for homeschooling\n",
    "\n",
    "print(\"\\nProbbility of being homeschooled by Gender\")  \n",
    "print(homeschool2)  # Prints frequency table for homeschooling by gender\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's graph our findings from  earlier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([<matplotlib.axis.XTick at 0x111a26278>,\n",
       "  <matplotlib.axis.XTick at 0x1a2372cbe0>],\n",
       " <a list of 2 Text xticklabel objects>)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "fig=plt.figure(figsize=(8,4))   # Define chart and set the size of the chart\n",
    "ax1=fig.add_subplot(121)  # Allows for labeled axis, and adjusts the size of the bars\n",
    "ax1.set_xlabel('homeschool') # Let x label be homeschool\n",
    "ax1.set_ylabel('Count of Students') # Let y label be count of students\n",
    "ax1.set_title('Homeschool by Gender') # Let axis title be homeschool by gender\n",
    "temp1.plot(kind='bar')  # Define graph as a bar chart\n",
    "\n",
    "# Rename cmale: 0 is female and 1 is male\n",
    "\n",
    "plt.xticks([0, 1], ['Female','Male'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at how many homeschoolers/non-homeschoolers are religious (since it's BYU, afterall)- just for fun"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([<matplotlib.axis.XTick at 0x11198f588>,\n",
       "  <matplotlib.axis.XTick at 0x11199c898>],\n",
       " <a list of 2 Text xticklabel objects>)"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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nHHGGRx//PEceeSRtLS0rM6PZ9ZleZPFSOA9EbFmX7lkltP662d3348IDjjgAK699tpcx+VZD6yzOn379mXZsmUA77pQ8KyzzuITn/gEU6ZMYdSoUUybNo3hw4fnismsO+Tthnoc2LQnAzFrRKNGjeKee+5h5syZACxcuJAnn+y493XPPffk1ltvZdGiRSxYsIBf/3rlZeqHDx/Os88+u/w9J0+ezN577w1kYxYPPPAAADfeeOPyY55++ml22mknzjzzTFpbW3niiSe67Wc0yyNvsrgauFHSkZI+XP7owdjMCjdw4ECuvvpqjjvuOHbeeWdGjRrV6Qf17rvvzqGHHsouu+zCkUceSWtrKxtvvPG76vTv35+rrrqKo48+mp122om11lqLL37xiwCcffbZnHbaaXzkIx+hT58+y4+59NJL2XHHHdlll11Yd911Oeigg3rmBzbrgPI0myUt62BXRESfDvbVVWtra1QbTGw4vniqe63mMvCPP/44I0aM6KZgMgsWLGCDDTZg4cKF7LXXXkyYMIHdduv5xR5X+2fx32b3Ws2/zXqR9EBEtNaql2vMIiLytkDMmt748eN57LHHWLRoEePGjatLojDrabnvDWVm+fziF78oOgSzbpf33lBTqbL4EEBEHNitEZmZWcPJ27K4u2J7C+CTZAPfZmbWy+Uds/huZZmkycBXuj0iMzNrOKszcH0P8PHuCsTMzBrXKiWLtJ72F4FXuzccMwO4/fbb2X777dl222254IILig7HLPcA91LePcDdB1iAlzu13q67rz3IMff+nXfe4dRTT2Xq1Km0tLQsv9Bvhx126N5YzLog7wD3/hXbC4AZEbHyvZrNbLXcd999bLvttmyzzTYAHHvssdx8881OFlaoXN1QEXFXxeOBriQKSVdKekXSX8vKBkiaKump9LxpKpekH0uaKekRSb6iyZrK888/z1ZbbbV8u6Wlheeff77AiMxqtCwknVDrDSLimhznuRq4DCivexYwPSIukHRW2j4TOAgYlh4fAq5Iz2ZNodoteLzGthWtVjfUv3ZQHsBAYCPenQCqV474vaQhFcWHAfuk15OAO8mSxWHANZH9j7lX0iaSBkfEi7XOY9YbtLS0MGvWrOXb7e3tbLHFFgVGZFajGyoihlU+yL7lTwHWIfuQX1WblxJAeh6UyrcEZpXVa09lK5E0XlKb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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "temp3 = pd.crosstab(homedf['homeschool'], homedf['religious'])  # Define the plot as the number of religious people \n",
    "        # and non-religious people that are and aren't homeschooled \n",
    "temp3.plot(kind='bar', stacked=True, color=['red', 'blue'], grid=False)   # Create stacked bar chart\n",
    "\n",
    "plt.ylabel('Number of Homeschoolers', fontsize=13)\n",
    "plt.xlabel('Homeschool Status', fontsize=16)\n",
    "plt.xticks([0, 1], ['Not Homeschooled','Homeschooled'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Personal subsetting exercise (just for fun/practice): Subsetting people who are male, whose family makes more than 100k, and are homeschooled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>year</th>\n",
       "      <th>homeschool</th>\n",
       "      <th>lnhhinc</th>\n",
       "      <th>momed</th>\n",
       "      <th>maritalmom</th>\n",
       "      <th>momage</th>\n",
       "      <th>cage</th>\n",
       "      <th>numsib</th>\n",
       "      <th>cmale</th>\n",
       "      <th>...</th>\n",
       "      <th>hhinc</th>\n",
       "      <th>meducation</th>\n",
       "      <th>evermarried</th>\n",
       "      <th>educ_evermarried</th>\n",
       "      <th>marriedmom</th>\n",
       "      <th>mothered</th>\n",
       "      <th>marrieded</th>\n",
       "      <th>hvalue</th>\n",
       "      <th>income</th>\n",
       "      <th>homeincome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>760</th>\n",
       "      <td>416</td>\n",
       "      <td>2003</td>\n",
       "      <td>1</td>\n",
       "      <td>11.9184</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>48</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>150000</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "      <td>Homeschooled</td>\n",
       "      <td>150001.414045</td>\n",
       "      <td>150001.414045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>776</th>\n",
       "      <td>759</td>\n",
       "      <td>2003</td>\n",
       "      <td>1</td>\n",
       "      <td>11.9184</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>150000</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "      <td>Homeschooled</td>\n",
       "      <td>150001.414045</td>\n",
       "      <td>150001.414045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>777</th>\n",
       "      <td>778</td>\n",
       "      <td>2003</td>\n",
       "      <td>1</td>\n",
       "      <td>11.9184</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>150000</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>17</td>\n",
       "      <td>Homeschooled</td>\n",
       "      <td>150001.414045</td>\n",
       "      <td>150001.414045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>796</th>\n",
       "      <td>1576</td>\n",
       "      <td>2003</td>\n",
       "      <td>1</td>\n",
       "      <td>11.9184</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>41</td>\n",
       "      <td>11</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>150000</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>17</td>\n",
       "      <td>Homeschooled</td>\n",
       "      <td>150001.414045</td>\n",
       "      <td>150001.414045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>803</th>\n",
       "      <td>1840</td>\n",
       "      <td>2003</td>\n",
       "      <td>1</td>\n",
       "      <td>11.9184</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>12</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>150000</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>Homeschooled</td>\n",
       "      <td>150001.414045</td>\n",
       "      <td>150001.414045</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Unnamed: 0  year  homeschool  lnhhinc  momed  maritalmom  momage  cage  \\\n",
       "760         416  2003           1  11.9184      2           1      48    18   \n",
       "776         759  2003           1  11.9184      2           1      39    11   \n",
       "777         778  2003           1  11.9184      4           1      50    10   \n",
       "796        1576  2003           1  11.9184      4           1      41    11   \n",
       "803        1840  2003           1  11.9184      5           1      50    12   \n",
       "\n",
       "     numsib  cmale      ...         hhinc  meducation  evermarried  \\\n",
       "760       1      1      ...        150000          13            1   \n",
       "776       2      1      ...        150000          13            1   \n",
       "777       3      1      ...        150000          17            1   \n",
       "796       3      1      ...        150000          17            1   \n",
       "803       2      1      ...        150000          20            1   \n",
       "\n",
       "     educ_evermarried  marriedmom  mothered  marrieded        hvalue  \\\n",
       "760                13           1        13         13  Homeschooled   \n",
       "776                13           1        13         13  Homeschooled   \n",
       "777                17           1        17         17  Homeschooled   \n",
       "796                17           1        17         17  Homeschooled   \n",
       "803                20           1        20         20  Homeschooled   \n",
       "\n",
       "            income     homeincome  \n",
       "760  150001.414045  150001.414045  \n",
       "776  150001.414045  150001.414045  \n",
       "777  150001.414045  150001.414045  \n",
       "796  150001.414045  150001.414045  \n",
       "803  150001.414045  150001.414045  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 270,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "richmalehs = homedf.loc[(homedf['cmale']==1) & (homedf['hhinc'] > 100000) & (homedf['homeschool']==1)]   # Subset as defined above\n",
    "richmalehs.head() # Looking at the first 5 entries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Second Data Set: Crime Rates and Precipitation\n",
    "\n",
    "### Our next data set will be crime rates and precipitation. Our goal here is to fix missing data (or at least a couple of the rows) and then determine if there is any correlation between precipitation and certain crime rates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>murd</th>\n",
       "      <th>rape</th>\n",
       "      <th>rob</th>\n",
       "      <th>assl</th>\n",
       "      <th>burg</th>\n",
       "      <th>larc</th>\n",
       "      <th>veht</th>\n",
       "      <th>pop</th>\n",
       "      <th>year</th>\n",
       "      <th>city</th>\n",
       "      <th>Tmean</th>\n",
       "      <th>Prcp</th>\n",
       "      <th>Snow</th>\n",
       "      <th>Snwd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2.439098</td>\n",
       "      <td>3.949016</td>\n",
       "      <td>91.29195</td>\n",
       "      <td>212.4338</td>\n",
       "      <td>149.9465</td>\n",
       "      <td>287.8136</td>\n",
       "      <td>63.18425</td>\n",
       "      <td>860974.0</td>\n",
       "      <td>76</td>\n",
       "      <td>Baltimore, MD</td>\n",
       "      <td>31.12903</td>\n",
       "      <td>0.132258</td>\n",
       "      <td>0.054839</td>\n",
       "      <td>0.032258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2.322951</td>\n",
       "      <td>2.322951</td>\n",
       "      <td>71.54688</td>\n",
       "      <td>223.0033</td>\n",
       "      <td>124.5101</td>\n",
       "      <td>288.1620</td>\n",
       "      <td>46.80745</td>\n",
       "      <td>860974.0</td>\n",
       "      <td>76</td>\n",
       "      <td>Baltimore, MD</td>\n",
       "      <td>44.24138</td>\n",
       "      <td>0.074483</td>\n",
       "      <td>0.044828</td>\n",
       "      <td>0.034483</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2.090656</td>\n",
       "      <td>4.645901</td>\n",
       "      <td>71.77917</td>\n",
       "      <td>233.9211</td>\n",
       "      <td>145.5329</td>\n",
       "      <td>315.2244</td>\n",
       "      <td>48.20122</td>\n",
       "      <td>860974.0</td>\n",
       "      <td>76</td>\n",
       "      <td>Baltimore, MD</td>\n",
       "      <td>48.29032</td>\n",
       "      <td>0.071935</td>\n",
       "      <td>0.251613</td>\n",
       "      <td>0.290323</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1.626065</td>\n",
       "      <td>3.832868</td>\n",
       "      <td>63.99729</td>\n",
       "      <td>238.9155</td>\n",
       "      <td>125.9039</td>\n",
       "      <td>290.1365</td>\n",
       "      <td>46.92360</td>\n",
       "      <td>860974.0</td>\n",
       "      <td>76</td>\n",
       "      <td>Baltimore, MD</td>\n",
       "      <td>57.16667</td>\n",
       "      <td>0.042333</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1.393770</td>\n",
       "      <td>4.645901</td>\n",
       "      <td>57.95761</td>\n",
       "      <td>262.1450</td>\n",
       "      <td>147.9720</td>\n",
       "      <td>326.0261</td>\n",
       "      <td>64.22958</td>\n",
       "      <td>860974.0</td>\n",
       "      <td>76</td>\n",
       "      <td>Baltimore, MD</td>\n",
       "      <td>62.35484</td>\n",
       "      <td>0.162258</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   month      murd      rape       rob      assl      burg      larc  \\\n",
       "0      1  2.439098  3.949016  91.29195  212.4338  149.9465  287.8136   \n",
       "1      2  2.322951  2.322951  71.54688  223.0033  124.5101  288.1620   \n",
       "2      3  2.090656  4.645901  71.77917  233.9211  145.5329  315.2244   \n",
       "3      4  1.626065  3.832868  63.99729  238.9155  125.9039  290.1365   \n",
       "4      5  1.393770  4.645901  57.95761  262.1450  147.9720  326.0261   \n",
       "\n",
       "       veht       pop  year           city     Tmean      Prcp      Snow  \\\n",
       "0  63.18425  860974.0    76  Baltimore, MD  31.12903  0.132258  0.054839   \n",
       "1  46.80745  860974.0    76  Baltimore, MD  44.24138  0.074483  0.044828   \n",
       "2  48.20122  860974.0    76  Baltimore, MD  48.29032  0.071935  0.251613   \n",
       "3  46.92360  860974.0    76  Baltimore, MD  57.16667  0.042333  0.000000   \n",
       "4  64.22958  860974.0    76  Baltimore, MD  62.35484  0.162258  0.000000   \n",
       "\n",
       "       Snwd  \n",
       "0  0.032258  \n",
       "1  0.034483  \n",
       "2  0.290323  \n",
       "3  0.000000  \n",
       "4  0.000000  "
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crimedf = pd.read_csv(\"/Users/mitchellpudil/Desktop/Crime_Rate/crime.csv\")  # Import data set\n",
    "crimedf.head() # at first 10 lines of the data set\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Describe Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>murd</th>\n",
       "      <th>rape</th>\n",
       "      <th>rob</th>\n",
       "      <th>assl</th>\n",
       "      <th>burg</th>\n",
       "      <th>larc</th>\n",
       "      <th>veht</th>\n",
       "      <th>pop</th>\n",
       "      <th>year</th>\n",
       "      <th>Tmean</th>\n",
       "      <th>Prcp</th>\n",
       "      <th>Snow</th>\n",
       "      <th>Snwd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4042.000000</td>\n",
       "      <td>3956.000000</td>\n",
       "      <td>3795.000000</td>\n",
       "      <td>3956.000000</td>\n",
       "      <td>3956.000000</td>\n",
       "      <td>3956.000000</td>\n",
       "      <td>3956.000000</td>\n",
       "      <td>3944.000000</td>\n",
       "      <td>4.028000e+03</td>\n",
       "      <td>4042.000000</td>\n",
       "      <td>4027.000000</td>\n",
       "      <td>4028.000000</td>\n",
       "      <td>4017.000000</td>\n",
       "      <td>4025.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>6.438149</td>\n",
       "      <td>1.862793</td>\n",
       "      <td>5.753337</td>\n",
       "      <td>55.746172</td>\n",
       "      <td>131.370748</td>\n",
       "      <td>166.721715</td>\n",
       "      <td>346.220161</td>\n",
       "      <td>103.820335</td>\n",
       "      <td>1.671597e+06</td>\n",
       "      <td>86.738743</td>\n",
       "      <td>60.679279</td>\n",
       "      <td>0.087357</td>\n",
       "      <td>0.030596</td>\n",
       "      <td>0.128988</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.452260</td>\n",
       "      <td>1.103834</td>\n",
       "      <td>2.579570</td>\n",
       "      <td>32.660631</td>\n",
       "      <td>84.258944</td>\n",
       "      <td>63.824224</td>\n",
       "      <td>105.802099</td>\n",
       "      <td>54.181254</td>\n",
       "      <td>1.698434e+06</td>\n",
       "      <td>6.490206</td>\n",
       "      <td>15.394288</td>\n",
       "      <td>0.084348</td>\n",
       "      <td>0.109333</td>\n",
       "      <td>0.715811</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.491336</td>\n",
       "      <td>6.424526</td>\n",
       "      <td>16.170800</td>\n",
       "      <td>34.977970</td>\n",
       "      <td>81.314780</td>\n",
       "      <td>11.801300</td>\n",
       "      <td>3.739730e+05</td>\n",
       "      <td>76.000000</td>\n",
       "      <td>10.451610</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.062223</td>\n",
       "      <td>3.814394</td>\n",
       "      <td>28.029532</td>\n",
       "      <td>74.036127</td>\n",
       "      <td>122.150550</td>\n",
       "      <td>278.477000</td>\n",
       "      <td>61.790042</td>\n",
       "      <td>7.451270e+05</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>52.129030</td>\n",
       "      <td>0.025161</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>1.702295</td>\n",
       "      <td>5.205219</td>\n",
       "      <td>48.450275</td>\n",
       "      <td>107.656000</td>\n",
       "      <td>158.949800</td>\n",
       "      <td>334.042450</td>\n",
       "      <td>95.786640</td>\n",
       "      <td>9.999000e+05</td>\n",
       "      <td>87.000000</td>\n",
       "      <td>61.964290</td>\n",
       "      <td>0.070000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>9.000000</td>\n",
       "      <td>2.429504</td>\n",
       "      <td>7.218239</td>\n",
       "      <td>79.370783</td>\n",
       "      <td>159.869475</td>\n",
       "      <td>207.468175</td>\n",
       "      <td>397.954400</td>\n",
       "      <td>134.350650</td>\n",
       "      <td>1.695239e+06</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>71.245695</td>\n",
       "      <td>0.126774</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>12.000000</td>\n",
       "      <td>7.237594</td>\n",
       "      <td>18.385680</td>\n",
       "      <td>179.862000</td>\n",
       "      <td>544.122500</td>\n",
       "      <td>425.512800</td>\n",
       "      <td>780.833100</td>\n",
       "      <td>356.107300</td>\n",
       "      <td>7.530493e+06</td>\n",
       "      <td>98.000000</td>\n",
       "      <td>97.677420</td>\n",
       "      <td>1.830000</td>\n",
       "      <td>1.182143</td>\n",
       "      <td>17.838710</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             month         murd         rape          rob         assl  \\\n",
       "count  4042.000000  3956.000000  3795.000000  3956.000000  3956.000000   \n",
       "mean      6.438149     1.862793     5.753337    55.746172   131.370748   \n",
       "std       3.452260     1.103834     2.579570    32.660631    84.258944   \n",
       "min       1.000000     0.000000     0.491336     6.424526    16.170800   \n",
       "25%       3.000000     1.062223     3.814394    28.029532    74.036127   \n",
       "50%       6.000000     1.702295     5.205219    48.450275   107.656000   \n",
       "75%       9.000000     2.429504     7.218239    79.370783   159.869475   \n",
       "max      12.000000     7.237594    18.385680   179.862000   544.122500   \n",
       "\n",
       "              burg         larc         veht           pop         year  \\\n",
       "count  3956.000000  3956.000000  3944.000000  4.028000e+03  4042.000000   \n",
       "mean    166.721715   346.220161   103.820335  1.671597e+06    86.738743   \n",
       "std      63.824224   105.802099    54.181254  1.698434e+06     6.490206   \n",
       "min      34.977970    81.314780    11.801300  3.739730e+05    76.000000   \n",
       "25%     122.150550   278.477000    61.790042  7.451270e+05    81.000000   \n",
       "50%     158.949800   334.042450    95.786640  9.999000e+05    87.000000   \n",
       "75%     207.468175   397.954400   134.350650  1.695239e+06    92.000000   \n",
       "max     425.512800   780.833100   356.107300  7.530493e+06    98.000000   \n",
       "\n",
       "             Tmean         Prcp         Snow         Snwd  \n",
       "count  4027.000000  4028.000000  4017.000000  4025.000000  \n",
       "mean     60.679279     0.087357     0.030596     0.128988  \n",
       "std      15.394288     0.084348     0.109333     0.715811  \n",
       "min      10.451610     0.000000     0.000000     0.000000  \n",
       "25%      52.129030     0.025161     0.000000     0.000000  \n",
       "50%      61.964290     0.070000     0.000000     0.000000  \n",
       "75%      71.245695     0.126774     0.000000     0.000000  \n",
       "max      97.677420     1.830000     1.182143    17.838710  "
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crimedf.describe() # Note that crime rates are in crime per 100,000"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at the correlations of different crime rates and precipitation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py:6462: UserWarning: The 'normed' kwarg is deprecated, and has been replaced by the 'density' kwarg.\n",
      "  warnings.warn(\"The 'normed' kwarg is deprecated, and has been \"\n",
      "/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py:6462: UserWarning: The 'normed' kwarg is deprecated, and has been replaced by the 'density' kwarg.\n",
      "  warnings.warn(\"The 'normed' kwarg is deprecated, and has been \"\n"
     ]
    },
    {
     "data": {
      "image/png": "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vSVp6fOfDXxsTcfK47Py2OIl74Hc2Bv+eF7rDqQVaVUj5Xa7UVNTY77Wdb1BA9UaDP18aJtevyU502dL5M/O4XASg1ZN+xgyZAg++eQTAMDXX3+N888/vzUvz+FwOJx2BqGUttpauZHd9+OPP4JSisWLF6NXr16tdXkOh8PhtDNa1UhxOBwOh9MY2neVF4fD4XASGm6kOBwOh2NZLCmL1JbKFPUxduxYeDwshbVr1664+eab8cQTT0AURQwfPhx33313q4/pm2++wTPPPIPXX38dR44cwSOPPAJCCHr37o358+dDEASsWLEC27ZtgyRJmDt3LgYMGNAm4/v+++8xffp09OjRAwAwYcIEXH311a0+PkVRMHfuXBQUFCAQCODOO+/EeeedZ4m5izW2zp07W2LeAEDTNDz66KP4+eefIYoilixZAkqpJeYu1tiqqqosM3cAUFpainHjxuHll1+GJEmWmLd2AbUgH3zwAZ09ezallNKvvvqKTp8+vU3H4/P56HXXXRf23pgxY+iRI0eorut06tSpdO/eva06pjVr1tBrr72W3njjjZRSSu+44w66c+dOSiml8+bNox9++CHdu3cvnThxItV1nRYUFNBx48a12fg2bNhAX3rppbB92mJ8f/vb3+iiRYsopZSWlZXRkSNHWmbuYo3NKvNGKaUfffQRfeSRRyillO7cuZNOnz7dMnMXa2xWmrtAIEBnzJhBR48eTQ8ePGiZeWsPWDLcZzVligMHDsDr9WLKlCmYNGkSvvjiCwQCAeTk5IAQguHDh2PHjh2tOqacnBwsX77cfP3999/joosuAgCMGDEC27dvx+7duzF8+HAQQpCdnQ1N01BWVtYm49u7dy+2bduGW265BXPnzkV1dXWbjO+qq67Cvffea74WRdEycxdrbFaZNwC44oorsHDhQgDAiRMnkJ6ebpm5izU2K83dU089hfHjx6NTp04ArPf3amUsaaTqU6ZoKxwOB26//Xa89NJLWLBgAebMmYOkpLreLC6XC1VVVa06pvz8/LBCaEqpKYVijCdyHltznJHjGzBgAB5++GGsW7cO3bp1w8qVK9tkfC6XC263G9XV1Zg5cyZmzZplmbmLNTarzJuBJEmYPXs2Fi5ciPz8fMvMXayxWWXuNm7ciLS0NPPBG7De36uVsaSRspoyRc+ePTFmzBgQQtCzZ094PB5UVFSY22tqapCc3LZad4JQ919pjCdyHmtqasx1tdbmyiuvxIUXXmj+vm/fvjYbX2FhISZNmoTrrrsOv/3tby01d5Fjs9K8GTz11FP44IMPMG/ePPj9dT3K2nruIsc2fPhwS8zd22+/je3bt2PixInYv38/Zs+eHeYhWWHerIwljZTVlCn+9re/4cknnwQAFBUVwev1wul04ujRo6CU4rPPPsOwYcPadIz9+vXDrl27AACffPIJhg0bhiFDhuCzzz6Drus4ceIEdF1HWlpam4zv9ttvx7fffgsA2LFjBy644II2GV9JSQmmTJmChx56CDfccAMA68xdrLFZZd4A4J133sELL7wAAEhKSgIhBBdeeKEl5i7W2O6++25LzN26devwl7/8Ba+//jr69u2Lp556CiNGjLDEvLUHLJndd+WVV+Lf//43xo8fbypTtCU33HAD5syZgwkTJoAQgsWLF0MQBDz44IPQNA3Dhw/HwIFnLwh7NsyePRvz5s3Dn/70J+Tm5iI/Px+iKGLYsGG4+eaboes6/vu//7vNxvfYY49h4cKFkGUZ6enpWLhwIdxud6uP7/nnn0dlZSVWrVqFVatWAQD++Mc/YtGiRW0+d7HG9sgjj2Dx4sVtPm8AMHr0aMyZMwe33HILVFXF3Llz0atXL0t872KNLSsryxLfuVhY/e/VSnDFCQ6Hw+FYFkuG+zgcDofDAbiR4nA4HI6F4UaKw+FwOJaFGykOh8PhWBZupDicJsJzjjiclocbqQRj8uTJGDVqVL030B9++AF5eXl499134zrf8uXLMXjw4Ab3eeSRR3DttdfGdb7jx48jLy8P77//flz7x2LixInIy8tr8N/GjRuxa9cu5OXl4bvvvmvytQxeeuklXHzxxRg0aBA2bdqELVu2YP78+Wd93pbi7rvvxuOPPx71fmFhIe666y4MHToUv/rVr7B06VIEAoGwfX788UdMnjwZgwcPxqWXXoo1a9aEfZ8mTpyIO+64o8U/A4cDWLROitN0rr/+esyePRtfffUVhgwZErX9vffeg8vlwpVXXtls15wxYwZqa2ub7XxnYv78+aiurjZf33bbbbj66qtx4403mu/l5OTgP//5T7Ncr6qqCk8//TSuueYaTJgwAbm5ubj33nvhdDqb5fzNCaUUTz/9ND766CPccsstYdsCgQCmTJkCh8OBpUuXorCw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\n",
      "text/plain": [
       "<Figure size 432x432 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(style=\"darkgrid\")\n",
    "\n",
    "figure = (sns.jointplot(\"veht\", \"murd\", data=crimedf, kind=\"reg\",\n",
    "                  xlim=(0, 400), ylim=(0, 8), color=\"m\").set_axis_labels(\"Vehicle Theft per 100k\", \"Murder Rate per 100k\", fontsize=16))\n",
    "\n",
    "sns.despine()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>murd</th>\n",
       "      <th>rape</th>\n",
       "      <th>rob</th>\n",
       "      <th>assl</th>\n",
       "      <th>burg</th>\n",
       "      <th>larc</th>\n",
       "      <th>veht</th>\n",
       "      <th>pop</th>\n",
       "      <th>year</th>\n",
       "      <th>Tmean</th>\n",
       "      <th>Prcp</th>\n",
       "      <th>Snow</th>\n",
       "      <th>Snwd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>month</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.085144</td>\n",
       "      <td>0.069587</td>\n",
       "      <td>0.075421</td>\n",
       "      <td>0.035151</td>\n",
       "      <td>0.074690</td>\n",
       "      <td>0.080782</td>\n",
       "      <td>0.056324</td>\n",
       "      <td>-0.001620</td>\n",
       "      <td>-0.031613</td>\n",
       "      <td>0.218534</td>\n",
       "      <td>-0.042036</td>\n",
       "      <td>-0.201959</td>\n",
       "      <td>-0.184727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>murd</th>\n",
       "      <td>0.085144</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.510430</td>\n",
       "      <td>0.663215</td>\n",
       "      <td>0.271522</td>\n",
       "      <td>0.416488</td>\n",
       "      <td>0.165411</td>\n",
       "      <td>0.637625</td>\n",
       "      <td>0.085204</td>\n",
       "      <td>0.054104</td>\n",
       "      <td>-0.094339</td>\n",
       "      <td>0.154368</td>\n",
       "      <td>0.126864</td>\n",
       "      <td>0.080371</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rape</th>\n",
       "      <td>0.069587</td>\n",
       "      <td>0.510430</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.330163</td>\n",
       "      <td>0.265272</td>\n",
       "      <td>0.554782</td>\n",
       "      <td>0.336400</td>\n",
       "      <td>0.356277</td>\n",
       "      <td>-0.268532</td>\n",
       "      <td>-0.036534</td>\n",
       "      <td>0.115492</td>\n",
       "      <td>0.135979</td>\n",
       "      <td>-0.010600</td>\n",
       "      <td>-0.025125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rob</th>\n",
       "      <td>0.075421</td>\n",
       "      <td>0.663215</td>\n",
       "      <td>0.330163</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.344461</td>\n",
       "      <td>0.253620</td>\n",
       "      <td>0.075326</td>\n",
       "      <td>0.586601</td>\n",
       "      <td>0.385985</td>\n",
       "      <td>0.106852</td>\n",
       "      <td>-0.285665</td>\n",
       "      <td>0.120505</td>\n",
       "      <td>0.177447</td>\n",
       "      <td>0.086225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>assl</th>\n",
       "      <td>0.035151</td>\n",
       "      <td>0.271522</td>\n",
       "      <td>0.265272</td>\n",
       "      <td>0.344461</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.054552</td>\n",
       "      <td>0.273201</td>\n",
       "      <td>0.234213</td>\n",
       "      <td>-0.133944</td>\n",
       "      <td>0.477755</td>\n",
       "      <td>0.098201</td>\n",
       "      <td>0.067068</td>\n",
       "      <td>-0.054543</td>\n",
       "      <td>-0.061037</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>burg</th>\n",
       "      <td>0.074690</td>\n",
       "      <td>0.416488</td>\n",
       "      <td>0.554782</td>\n",
       "      <td>0.253620</td>\n",
       "      <td>-0.054552</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.615597</td>\n",
       "      <td>0.327131</td>\n",
       "      <td>-0.154091</td>\n",
       "      <td>-0.406034</td>\n",
       "      <td>0.139666</td>\n",
       "      <td>0.037554</td>\n",
       "      <td>-0.022915</td>\n",
       "      <td>-0.034833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>larc</th>\n",
       "      <td>0.080782</td>\n",
       "      <td>0.165411</td>\n",
       "      <td>0.336400</td>\n",
       "      <td>0.075326</td>\n",
       "      <td>0.273201</td>\n",
       "      <td>0.615597</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.179805</td>\n",
       "      <td>-0.287498</td>\n",
       "      <td>0.026075</td>\n",
       "      <td>0.298832</td>\n",
       "      <td>-0.032286</td>\n",
       "      <td>-0.196741</td>\n",
       "      <td>-0.148765</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>veht</th>\n",
       "      <td>0.056324</td>\n",
       "      <td>0.637625</td>\n",
       "      <td>0.356277</td>\n",
       "      <td>0.586601</td>\n",
       "      <td>0.234213</td>\n",
       "      <td>0.327131</td>\n",
       "      <td>0.179805</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.146577</td>\n",
       "      <td>0.325005</td>\n",
       "      <td>-0.080304</td>\n",
       "      <td>0.023789</td>\n",
       "      <td>0.074196</td>\n",
       "      <td>0.041046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pop</th>\n",
       "      <td>-0.001620</td>\n",
       "      <td>0.085204</td>\n",
       "      <td>-0.268532</td>\n",
       "      <td>0.385985</td>\n",
       "      <td>-0.133944</td>\n",
       "      <td>-0.154091</td>\n",
       "      <td>-0.287498</td>\n",
       "      <td>0.146577</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.024120</td>\n",
       "      <td>-0.141098</td>\n",
       "      <td>0.063618</td>\n",
       "      <td>0.098629</td>\n",
       "      <td>0.057290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>-0.031613</td>\n",
       "      <td>0.054104</td>\n",
       "      <td>-0.036534</td>\n",
       "      <td>0.106852</td>\n",
       "      <td>0.477755</td>\n",
       "      <td>-0.406034</td>\n",
       "      <td>0.026075</td>\n",
       "      <td>0.325005</td>\n",
       "      <td>0.024120</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011753</td>\n",
       "      <td>0.038521</td>\n",
       "      <td>-0.052873</td>\n",
       "      <td>-0.054547</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tmean</th>\n",
       "      <td>0.218534</td>\n",
       "      <td>-0.094339</td>\n",
       "      <td>0.115492</td>\n",
       "      <td>-0.285665</td>\n",
       "      <td>0.098201</td>\n",
       "      <td>0.139666</td>\n",
       "      <td>0.298832</td>\n",
       "      <td>-0.080304</td>\n",
       "      <td>-0.141098</td>\n",
       "      <td>0.011753</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.015819</td>\n",
       "      <td>-0.553337</td>\n",
       "      <td>-0.410845</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Prcp</th>\n",
       "      <td>-0.042036</td>\n",
       "      <td>0.154368</td>\n",
       "      <td>0.135979</td>\n",
       "      <td>0.120505</td>\n",
       "      <td>0.067068</td>\n",
       "      <td>0.037554</td>\n",
       "      <td>-0.032286</td>\n",
       "      <td>0.023789</td>\n",
       "      <td>0.063618</td>\n",
       "      <td>0.038521</td>\n",
       "      <td>-0.015819</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.039990</td>\n",
       "      <td>-0.000379</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Snow</th>\n",
       "      <td>-0.201959</td>\n",
       "      <td>0.126864</td>\n",
       "      <td>-0.010600</td>\n",
       "      <td>0.177447</td>\n",
       "      <td>-0.054543</td>\n",
       "      <td>-0.022915</td>\n",
       "      <td>-0.196741</td>\n",
       "      <td>0.074196</td>\n",
       "      <td>0.098629</td>\n",
       "      <td>-0.052873</td>\n",
       "      <td>-0.553337</td>\n",
       "      <td>0.039990</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.730452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Snwd</th>\n",
       "      <td>-0.184727</td>\n",
       "      <td>0.080371</td>\n",
       "      <td>-0.025125</td>\n",
       "      <td>0.086225</td>\n",
       "      <td>-0.061037</td>\n",
       "      <td>-0.034833</td>\n",
       "      <td>-0.148765</td>\n",
       "      <td>0.041046</td>\n",
       "      <td>0.057290</td>\n",
       "      <td>-0.054547</td>\n",
       "      <td>-0.410845</td>\n",
       "      <td>-0.000379</td>\n",
       "      <td>0.730452</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          month      murd      rape       rob      assl      burg      larc  \\\n",
       "month  1.000000  0.085144  0.069587  0.075421  0.035151  0.074690  0.080782   \n",
       "murd   0.085144  1.000000  0.510430  0.663215  0.271522  0.416488  0.165411   \n",
       "rape   0.069587  0.510430  1.000000  0.330163  0.265272  0.554782  0.336400   \n",
       "rob    0.075421  0.663215  0.330163  1.000000  0.344461  0.253620  0.075326   \n",
       "assl   0.035151  0.271522  0.265272  0.344461  1.000000 -0.054552  0.273201   \n",
       "burg   0.074690  0.416488  0.554782  0.253620 -0.054552  1.000000  0.615597   \n",
       "larc   0.080782  0.165411  0.336400  0.075326  0.273201  0.615597  1.000000   \n",
       "veht   0.056324  0.637625  0.356277  0.586601  0.234213  0.327131  0.179805   \n",
       "pop   -0.001620  0.085204 -0.268532  0.385985 -0.133944 -0.154091 -0.287498   \n",
       "year  -0.031613  0.054104 -0.036534  0.106852  0.477755 -0.406034  0.026075   \n",
       "Tmean  0.218534 -0.094339  0.115492 -0.285665  0.098201  0.139666  0.298832   \n",
       "Prcp  -0.042036  0.154368  0.135979  0.120505  0.067068  0.037554 -0.032286   \n",
       "Snow  -0.201959  0.126864 -0.010600  0.177447 -0.054543 -0.022915 -0.196741   \n",
       "Snwd  -0.184727  0.080371 -0.025125  0.086225 -0.061037 -0.034833 -0.148765   \n",
       "\n",
       "           veht       pop      year     Tmean      Prcp      Snow      Snwd  \n",
       "month  0.056324 -0.001620 -0.031613  0.218534 -0.042036 -0.201959 -0.184727  \n",
       "murd   0.637625  0.085204  0.054104 -0.094339  0.154368  0.126864  0.080371  \n",
       "rape   0.356277 -0.268532 -0.036534  0.115492  0.135979 -0.010600 -0.025125  \n",
       "rob    0.586601  0.385985  0.106852 -0.285665  0.120505  0.177447  0.086225  \n",
       "assl   0.234213 -0.133944  0.477755  0.098201  0.067068 -0.054543 -0.061037  \n",
       "burg   0.327131 -0.154091 -0.406034  0.139666  0.037554 -0.022915 -0.034833  \n",
       "larc   0.179805 -0.287498  0.026075  0.298832 -0.032286 -0.196741 -0.148765  \n",
       "veht   1.000000  0.146577  0.325005 -0.080304  0.023789  0.074196  0.041046  \n",
       "pop    0.146577  1.000000  0.024120 -0.141098  0.063618  0.098629  0.057290  \n",
       "year   0.325005  0.024120  1.000000  0.011753  0.038521 -0.052873 -0.054547  \n",
       "Tmean -0.080304 -0.141098  0.011753  1.000000 -0.015819 -0.553337 -0.410845  \n",
       "Prcp   0.023789  0.063618  0.038521 -0.015819  1.000000  0.039990 -0.000379  \n",
       "Snow   0.074196  0.098629 -0.052873 -0.553337  0.039990  1.000000  0.730452  \n",
       "Snwd   0.041046  0.057290 -0.054547 -0.410845 -0.000379  0.730452  1.000000  "
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crimedf.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at how many rows are missing per column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month      0\n",
       "murd      86\n",
       "rape     247\n",
       "rob       86\n",
       "assl      86\n",
       "burg      86\n",
       "larc      86\n",
       "veht      98\n",
       "pop       14\n",
       "year       0\n",
       "city       0\n",
       "Tmean     15\n",
       "Prcp      14\n",
       "Snow      25\n",
       "Snwd      17\n",
       "dtype: int64"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crimedf.apply(lambda x: sum(x.isnull()), axis=0)  # lambda function to determine number of missing observations per feature"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at how the different types of crime compare with each other to see which crime rate is most prevelant on average. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 297,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rape</th>\n",
       "      <th>rob</th>\n",
       "      <th>assl</th>\n",
       "      <th>burg</th>\n",
       "      <th>larc</th>\n",
       "      <th>veht</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.949016</td>\n",
       "      <td>91.29195</td>\n",
       "      <td>212.4338</td>\n",
       "      <td>149.9465</td>\n",
       "      <td>287.8136</td>\n",
       "      <td>63.18425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.322951</td>\n",
       "      <td>71.54688</td>\n",
       "      <td>223.0033</td>\n",
       "      <td>124.5101</td>\n",
       "      <td>288.1620</td>\n",
       "      <td>46.80745</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.645901</td>\n",
       "      <td>71.77917</td>\n",
       "      <td>233.9211</td>\n",
       "      <td>145.5329</td>\n",
       "      <td>315.2244</td>\n",
       "      <td>48.20122</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.832868</td>\n",
       "      <td>63.99729</td>\n",
       "      <td>238.9155</td>\n",
       "      <td>125.9039</td>\n",
       "      <td>290.1365</td>\n",
       "      <td>46.92360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.645901</td>\n",
       "      <td>57.95761</td>\n",
       "      <td>262.1450</td>\n",
       "      <td>147.9720</td>\n",
       "      <td>326.0261</td>\n",
       "      <td>64.22958</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       rape       rob      assl      burg      larc      veht\n",
       "0  3.949016  91.29195  212.4338  149.9465  287.8136  63.18425\n",
       "1  2.322951  71.54688  223.0033  124.5101  288.1620  46.80745\n",
       "2  4.645901  71.77917  233.9211  145.5329  315.2244  48.20122\n",
       "3  3.832868  63.99729  238.9155  125.9039  290.1365  46.92360\n",
       "4  4.645901  57.95761  262.1450  147.9720  326.0261  64.22958"
      ]
     },
     "execution_count": 297,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "murders = crimedf.loc[:,'rape':'veht']\n",
    "murders.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's drop the missing observations for population, Tmean, Prcp, and Snow because there are not many missing observations and replace larceny with the mean. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:3: UserWarning: Boolean Series key will be reindexed to match DataFrame index.\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n",
      "/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:4: UserWarning: Boolean Series key will be reindexed to match DataFrame index.\n",
      "  after removing the cwd from sys.path.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "month      0\n",
       "murd      72\n",
       "rape     226\n",
       "rob       72\n",
       "assl      72\n",
       "burg      72\n",
       "larc       0\n",
       "veht      84\n",
       "pop        0\n",
       "year       0\n",
       "city       0\n",
       "Tmean      0\n",
       "Prcp       0\n",
       "Snow       0\n",
       "Snwd       1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crimedf['larc'].fillna(crimedf['larc'].mean(), inplace=True)  # \n",
    "crimedf2 = crimedf[np.isfinite(crimedf['pop'])]   # Ask how to combine these commands into one\n",
    "crimedf3 = crimedf2[np.isfinite(crimedf['Tmean'])]\n",
    "crimedf4 = crimedf3[np.isfinite(crimedf['Snow'])]\n",
    "\n",
    "# Let's run that lambda function again to make sure that there are no missing values for the robbery rate\n",
    "crimedf4.apply(lambda x: sum(x.isnull()), axis=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### It appears that there is a negative correlation between larceny rate and snowfall. Let's now do a regression to see if this is the case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intercept    80.692743\n",
      "Tmean         1.672750\n",
      "rape         -1.122872\n",
      "burg          1.007691\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import statsmodels.formula.api as sm   # Statsmodels is a library that will allow us to perform regressions\n",
    "result = sm.ols(formula=\"larc ~ Tmean + rape + burg\", data=crimedf4).fit()  # Define reg. formula and fit\n",
    "print(result.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Third Data Set: Loan Payments\n",
    "\n",
    "### The last data set we will use will come from a .txt file that looks at loan payments. The goal here will be to estimate the effect of Price Change on Loan Payments Overdue and the difference in overdue loan payments between men and women, on average."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  MetroArea  PriceChange  LoanPaymentsOverdue  Male\n",
      "0   Atlanta          1.2                 4.55   0.0\n",
      "1    Boston         -3.4                 3.31   0.0\n",
      "2   Chicago         -0.9                 2.99   1.0\n",
      "3    Dallas          0.8                 4.26   1.0\n",
      "4    Denver         -0.7                 3.56   0.0\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PriceChange</th>\n",
       "      <th>LoanPaymentsOverdue</th>\n",
       "      <th>Male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>17.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>-3.427778</td>\n",
       "      <td>3.532222</td>\n",
       "      <td>0.529412</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.518043</td>\n",
       "      <td>1.061633</td>\n",
       "      <td>0.514496</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-9.700000</td>\n",
       "      <td>1.650000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-7.000000</td>\n",
       "      <td>3.020000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>-3.950000</td>\n",
       "      <td>3.300000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>-0.750000</td>\n",
       "      <td>4.477500</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6.900000</td>\n",
       "      <td>5.630000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PriceChange  LoanPaymentsOverdue       Male\n",
       "count    18.000000            18.000000  17.000000\n",
       "mean     -3.427778             3.532222   0.529412\n",
       "std       4.518043             1.061633   0.514496\n",
       "min      -9.700000             1.650000   0.000000\n",
       "25%      -7.000000             3.020000   0.000000\n",
       "50%      -3.950000             3.300000   1.000000\n",
       "75%      -0.750000             4.477500   1.000000\n",
       "max       6.900000             5.630000   1.000000"
      ]
     },
     "execution_count": 236,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "paymentsdf = pd.read_table('/Users/mitchellpudil/Desktop/indicators.txt', delim_whitespace=True)  # Import table\n",
    "print(paymentsdf.head())  # Top 5 results\n",
    "paymentsdf.describe()  # Mean, max, min, and other summary statistics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's take a look at price changes. This should help us determine the quality of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Frequency')"
      ]
     },
     "execution_count": 209,
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
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "indicators['PriceChange'].hist()   # Quick plot of the price change\n",
    "plt.xlabel('Price Change', fontsize=13)\n",
    "plt.ylabel('Frequency', fontsize=13)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's look at the distribution of the average number of Loan Payments Overdue by Gender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Loan Payments Overdue')"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZAAAAEcCAYAAADpzeJvAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzt3XmcHFW5//HPlySQgCHINmyRKKBsyuIoIngdwMuVRXBBgSsqiEa8gqh4le0CIii4K3jFILJqRFG4YQugMCAqS4JBAkHlh9FEQAlLYCACgef3xzkNlaanp7oyPT3DfN+vV7+muupU1VPdNfV01Tl1ShGBmZlZq1bodABmZjYyOYGYmVklTiBmZlaJE4iZmVXiBGJmZpU4gZiZWSVOIDbiSDpH0kmdjqPTmn0Okg6UdONQx9SMpJC0cafjsMHjBGKVSZovaYmkPkmPSLpc0uROx1Xkg9byk9SbP8et6sZfksf3dCg06zAnEFte74iIlwHrAv8ATutwPG2jZLT+z/wJ+GDtjaQ1gDcBD3YsIuu40frPYIMsIv4FXARsXhsnaZKk8yQ9KOmvko6tHYAlfU/SRYWyp0r6VT5I90haKOloSYvymc77+1u3pI9KukfSw5JmSFovj78hF7k9nyXt22DeMZK+ntfzF0mH5l/VY/P0XkknS/oN8CTwKknr5fU8nNf70cLylrmsVNuWwvv5ko6SdFc+aztb0vjC9D0lzZH0qKTfSnpdYdo2km6T9LikC4Hn5+v/o9FpkhZLulvSLnnkeyXNrit4hKRLmizrR8C+ksbk9/sDFwNPF5bxRkm/y7HfL+l0SSv2E9hKkr4m6W+S/iHpDEkTBtgeG2acQGxQSFoZ2Be4qTD6NGAS8CrgraRfsAflaUcAr8vX6t8CHAx8KF7oW2cdYE1gfeBDwDRJr2mw3p2BLwPvI50F/RX4CUBE/FsutlVEvCwiLmwQ+keB3YCtgW2BdzYo8wFgKjAxL386sBBYD9gH+FLt4FzS+4H/ADYCXg0cm7dlW+CHwMeANYDvAzPywXZF4BLgfGB14GfAewZYz3bAvaTP8XjgF5JWB2YAr5S0WaHsAXnZ/bkPuAvYNb//IHBeXZlngU/n9W0P7AL8Vz/LO5W07VsDG5O+5+MG2B4bbiLCL78qvYD5QB/wKLCUdJB5bZ42BngK2LxQ/mNAb+H9G4GHSQfl/Qvje/LyVimM+ynwP3n4HOCkPHwW8JVCuZcBzwBT8vsANm6yDdcCHyu8f1ueZ2x+3wucWJg+mXSgnFgY92XgnPrYCtuysO4zO6Twfnfg/+Xh7wFfrIvvj6Tk+2/581Vh2m+L66qb78AG5W8BPlBY18l5eAvgEWClfpbVC3yElGSmA68B/pSnLQR6+pnvU8DFhfdBShYCngA2KkzbHvhLp/dpv1p7+QzEltc7I2I1YCXgUOB6SbWzhxVJyaHmr6RfmgBExC2kX8giJYiiRyLiibp512uw/vWK64iIPuCh4noGsB6woPB+QYMyxXHrAQ9HxON1sZVdX/3yitu1IXBEvgT0qKRHSQlrvfz6e+SjbWHeZhqVr63rXOA/JYl0hvXTiHhqgOX9AtgZOIwGZyuSXi3pMkkPSHoM+BJpP6i3FrAyMLuwnTPzeBtBnEBsUETEsxHxC9Kv8x2BRaQzgQ0LxV4B/L32RtInSInnPuBzdYt8uaRV6ua9r8Gq7yuuI8+zRnE9A7gf2KDwvlErsuJB+D5gdUkT62Krre8J0sGxZp0Gyyuuo7hdC0hnBasVXitHxPQc5/r5gI+kA4E9mm5ZoXz9uiLiJlL9xVuA/6Sfy1d5PdvkeZ4ErgQ+3k/57wF3A5tExKrA0aQfB/UWAUuALQrbOSlSY4xBU1//ZIPPCWQEyhWxb+twDEE6IF0q6e+SviHpXcDLgXkR8SzprOJkSRMlbQh8Brggz/9q4CTSZZEPAJ+TtHXdar4gacVcR7In6bp/vR8DB0naWtJKpF+9N0fE/Dz9H6Q6mPr4T5B0QY7xcEnrS1oN+Hyz7Y6IBaRLR2fkX9uPA0cCW0t6MzAH2F3S6vlM7FMNFvMJSRvk+oijgVrdzJnAIZK2U7KKpD1ysvod6bLeJ3MF/+tJl+uaWTuXHyfpvcBmwBWF6ecBpwNLI6LsPSNHA28tfL5FE4HHgD5Jm5ISTb0dgF8BY4F7Jc2V9HlJr5L0HyVjsGHCCcSWR+2X82qkA+XppIrwO/P4w0i/yO8FbiQd7H+YD4AXAKdGxO0R8WfSgen8nAQAHiBdl7+P1ALokIi4uz6AiPgV8D/Az0m/0jcC9isUOQE4N18qeV+DbTgTuBr4A/B70gF2KelMqj9HAu8lVRIvIlUc/zAv50/A7aS6jqt5ITkU/ThPuze/TsrbMotUqX963vZ7SHUZK0TE08C78/tHSPVHDzWJEeBmYJMc48nAPhFRnOd8YEuaV54vIyLua5JsPks6m3mc9Lk22vbTSdu/IfB1UiOLL5I+jxc1kuiUvI/aQDpdCeNX6y/Swelt/Uz7KOnA8zCptc16hWnfJl0meQyYDbylMO0E0q/x80gHgDuB7iYxLFM5TTo7OD0PHwn8v7ycu4B35fEr5bheW5hvbdLljLXIFc7AGaQD+P2kVlG7kw7MDwNHF+ZdobCuh3L8q+dpU3KMHwL+RjqIHpOnvZ10+eYZUiOA2/P4A/M6nwP+Ary/n20/H7iiwfjvATfk4ZnAoXXTbwf+Saqo3xS4Jm/TH4H3Fcqdk5d1BSkBv410WW5G/u5uIR10b6zb1rGFZfQCHym8/zAwj5R8riIdwCfk72iTJt/zgcBvSC3qFpMuUe2Sp70XmF1X/gjgkgbLEWnfO2KAfbvSd5qnT8if3SOk/e6/WbYBw3qkHxoP5u/3k3X7/0WkHzaPFT87v5p8X50OwK8KX1o/CYRUwbmI1Bx1pfxPf0Nh+gH5QDQ2/6M/AIzP004A/kU6WI8htSy6qUkMzycQ0r0fDwAH5/fvzf+sK5Ca9j4BrJun/S/pzKO2nMOBS/NwD+nX/w9JieSj+Z/9x6TLI1vkGF+Vy3+K1Gx4g7y93wem52m1g82Z+cCyFalV2GaF7b0gT9sdWJV0MJ0DfIvUJHiLfrb9AeCgBuN3IiW+lUnNXH9TmLY5qbXafNLluAWkJs1j8/e1qLa+fBBcTLrcswLpfo+fkA6mq5DOGv5OyQRCSsL3kC5hjSU1G/4t6ZLitQPsawfm7+TTwLj8fS4mNSWu/SDYrFD+98B7Gixn0xzjlAHWtzzf6SnAr3Nsk4G55ASSP8fZpKbCK5Iua94L/Edhf3gmf1YrABM6/X8+El4dD8CvCl9a/wmkaZPWBuUfId0jUfsH+mVh2ubAkiYxBOmX2iOkX4snkS61NCo7B9g7D2+XD54r5PezyL++SQlkCSkRLiQljQC2KyxrNqnlF6Rf1LsUpq2bt3ds4WCzQWH6LcB+he29gHSwv5WUPJ4jNetde4DPfynw9gbjawfJ9XPsTwAb5mknkxLjfNLZw6/r5v0+cHwePgc4rzBtTN6uTQvjvkT5BHIlObnn9yvkbV0IbDPAth7IIDQHJjWsCPIPljzuJ6Sk+mRhecvznd5b/F5I9+7UEsh2wN/qYjoKOLuwP9zQ7LPw68Uv14G8tDRt0prvNp6X70x+lHT9udjM8oHC8JPA+AGuBW8bES+PiI0i4tiIeC6v54OFu6kfJf1iXjPHdDPpwPrWXNG6MenSTM1DEXFtRGxASiaQKsJrlvBC5fGGwMWF9cwjnQF0NdmmZSqeI+LJiHhDREwk3VD4LPAnpX69Nu1nuxeRDmz11iUdmB+J1Mz3cl6oj9kP+FFETCElq+3qmuu+n2VbbBWb+q5FOoDWN/8ta0Pg24V1PUz65f6+iPh9ifkHozlwre7l+c8tIvaL1AT8NlKSrMVa9Tutb5Jd/Iw2BNar+8yPrltuoybc1oQTyEtLv01ac0umz5Pu2H55/sddTONmlpXl1lZnku4JWSOvZ27des7lhdZXF0XqBqWKBcBusWyz1/ERUaYJb7xoRMRVEfHvpIPc3Xk7Gvkl6TJdvfcBv4vU3BXSTXf7S9qedMnlukLc19fF/bKIKLZaKsb3IOmsp775b03tfpn+mg8vIN0sWVzfhIj4bT/bV2+5mwOTPs+/kxoCNLM83+n99P8ZLSDdqFhc7sSI2L1Q5kX7hDXnBDJyjZM0vvAaS/MmrRNJB6EHgbGSjiNd9x9sq5D+ER8EkHQQ6Qyk6HzgXaQkUt8dRivOIDUT3jCvay1Je5ec9x/AFL3QN1eXpL1y0n2KVLneX0usLwBvVuoja/XcTPkwUr1HsRnwFaSEfiJwYe0MDbgMeLWkD+QmtuMkvUHLdi3yvEhNon8BnCBpZUmbkyqSa9MfJB2cD1Dq2+vDpNZoxc/pKElb5G2dlJv1kt/3SjqhyWe13M2B8xnMEcDxSn2XvTw3Vd6EZc8Cluc7/WnezpdL2oDUCrDmFuCx3GR4Qv6ctpT0hpLLtgacQEauK0iXc2qvE6J5k9arSNfC/0Q6tf8XbThlj4i7SM0zf0c6SL+W1IqnWGYh6bJFkCo9q/o26fLX1fl+jJtI17rLqN1T8pCk20j/C0eQflk/TOo+pGE/TpGaHe9IqsSdT/qs30OqkP1NodxTpAP/20jJvTb+cVKfUvvl9T1A6huq1oS5kUNJl2oeINWRnF03/aOkVkcPkeoinj+7iIiL8/J/onSH+FzS5bqaydR9R3UGpTlwpL7I3kf64bAgL++nwDRe+D6W5zv9Amnf/gupWfDz8eQk/A5S31t/yev+AekyrlWkZS9tmg0NST8E7ouIYzsdy2iWf6n/LCK2X45lTCA1T942J1cbJZxAbMhJmkJqmbVNRPyls9HY8pL0GWDPiNi507HY0PLdljakJH2RdE/Bl508Rj5J80kNJBp1g28vcT4DMTOzSlyJbmZmlTiBmJlZJSOuDmTNNdeMKVOmdDqMl6QnnniCVVZZZeCCZsOA99f2mT179qKIGPABXyMugUyZMoVZs2Z1OoyXpN7eXnp6ejodhlkp3l/bR1KprnJ8CcvMzCpxAjEzs0qcQMzMrBInEDMzq8QJxMzMKnECMaZPn86WW27JLrvswpZbbsn06dM7HZKZjQAjrhmvDa7p06dzzDHHcNZZZ/Hss88yZswYDj74YAD233//DkdnZsOZz0BGuZNPPpmzzjqLnXbaibFjx7LTTjtx1llncfLJJ3c6NDMb5pxARrl58+ax4447LjNuxx13ZN68eR2KyMxGCieQUW6zzTbjxhuXfQrpjTfeyGabNXy6qpnZ89qaQCTNl3SHpDmSXtT/iKQeSYvz9Dn5Od02hI455hgOPvhgrrvuOpYuXcp1113HwQcfzDHHHNPp0MxsmBuKSvSdImJRk+m/jog9hyAOa6BWUX7YYYcxb948NttsM04++WRXoJvZgNwKy9h///3Zf//93TmdmbWk3XUgAVwtabakqf2U2V7S7ZKulLRFm+MxM7NB0u4zkB0i4j5JawPXSLo7Im4oTL8N2DAi+iTtDlwCbFK/kJx8pgJ0dXXR29vb5rBHp76+Pn+2NmJ4f+28IXsmuqQTgL6I+FqTMvOB7mZ1Jt3d3eHngbSHL2HZSOL9tX0kzY6I7oHKte0SlqRVJE2sDQO7AnPryqwjSXn4jTmeh9oVk5mZDZ52XsLqAi7O+WEs8OOImCnpEICIOAPYB/i4pKXAEmC/GKpTIjMzWy5tSyARcS+wVYPxZxSGTwdOb1cMZmbWPr4T3czMKnECMTOzSpxAzMysEicQMzOrxAnEzMwqcQIxM7NKnEDMzKwSJxAzM6vECcTMzCpxAjEzs0qcQMzMrBInEDMzq8QJxMzMKnECMTOzSpxAzMysEicQMzOrpK0JRNJ8SXdImiPpRQ8yV/IdSfdI+oOkbdsZj5mZDZ52PtK2ZqeIWNTPtN2ATfJrO+B7+a+ZmQ1znb6EtTdwXiQ3AatJWrfDMZmZWQntTiABXC1ptqSpDaavDywovF+Yx5mZ2TDX7ktYO0TEfZLWBq6RdHdE3FCYrgbzRP2InHymAnR1ddHb29uWYEe7vr4+f7Y2Ynh/7by2JpCIuC///aeki4E3AsUEshCYXHi/AXBfg+VMA6YBdHd3R09PT7tCHtV6e3vxZ2sjhffXzmvbJSxJq0iaWBsGdgXm1hWbAXwwt8Z6E7A4Iu5vV0xmZjZ42nkG0gVcLKm2nh9HxExJhwBExBnAFcDuwD3Ak8BBbYzHzMwGUdsSSETcC2zVYPwZheEAPtGuGMzMrH2G4j4QM7PK8lWMlqXfp9ZOnb4PxMysqYho+Nrw85f1O83JY2gMmEAkrSzpfySdmd9vImnP9odmZmbDWZkzkLOBp4Dt8/uFwElti8jMzEaEMglko4j4CvAMQEQsofENgGZmNoqUSSBPS5pAvkNc0kakMxIzMxvFyrTCOh6YCUyW9CNgB+DAdgZlZmbD34AJJCKukXQb8CbSpavDm3TPbmZmo8SACUTSv+XBx/PfzSVR1ymimZmNMmUuYf13YXg8qUPE2cDObYnIzMxGhDKXsN5RfC9pMvCVtkVkZmYjQpU70RcCWw52IGZmNrKUqQM5jRce8rQCsDVwezuDMjOz4a9MHciswvBSYHpE/KZN8ZiZ2QhRpg7k3KEIxMxGr62+cDWLlzzT8nxTjry8pfKTJozj9uN3bXk91li/CUTSHTR4PnlNRLyuLRGZ2aizeMkzzD9lj5bmqfJI21YTjjXX7Ayk1uNu7YFP5+e/7yc9PbAUSWNIl8H+HhF71k07EPgq8Pc86vSI+EHZZZuZWef0m0Ai4q8AknaIiB0Kk46U9BvgxJLrOByYB6zaz/QLI+LQksuy5eSH85jZYCnTjHcVSTvW3kh6M7BKmYVL2gDYA/BZxTDR7AE8zR7QY2ZWr0wrrA8DZ0uaRKoTWZzHlfEt4HPAxCZl3pO7S/kT8OmIWFBfQNJUYCpAV1cXvb29JVdvrfJna53S6r7X19dXaX/1Pj54miYQSSsAG0fEVpJWBRQRi8ssOD+18J8RMVtSTz/FLiU1C35K0iHAuTToIiUipgHTALq7u6PVijMraeblLVdKmg2KCvtelUp07+ODq+klrIh4Djg0Dz9WNnlkOwB7SZoP/ATYWdIFdct/KCJqzxY5E3h9C8s3M7MOKlMHco2kz0qaLGn12mugmSLiqIjYICKmAPsB10bEAcUyktYtvN2LVNluZmYjQNk6EHihOS+kupBXVVmhpBOBWRExA/ikpL1Id7g/jB9UZWY2YpS5E/2Vy7uSiOgFevPwcYXxRwFHLe/yzcxs6A14CUvSypKOlTQtv98kV5CbmdkoVqYO5GzgaeDN+f1C4KS2RWRmZiNCmQSyUUR8BXgGICKWkJ6NbmZmo1iZBPK0pAnkjhUlbQQ81XwWMzN7qSvTCusEYCYwWdKPSPd3HNjGmMzMbAQo0wrrakmzgTeRLl0dHhGL2h6ZmZkNa2UeaTsDmA7MiIgn2h+SmZmNBGXqQL4OvAW4S9LPJO0jaXyb4zIzs2GuzCWs64Hr84OhdgY+CvyQ/p/vYWZmo0CZSnRyK6x3APsC25J6zTUzs1GsTB3IhaQK9CuB7wK9uZdeMzMbxcqcgZwN/GdEPNvuYMzMbOQY6IFSa5O6MPmIpADuAv43Iv4xFMGZmdnw1W8rLEk7ALeS7kA/D6g9DOrmPM3MzEaxZmcgXwfeGRG/L4z7P0kXA98HtmtrZGZmNqw1uw9k1brkAUBEzAEmll2BpDGSfi/psgbTVpJ0oaR7JN0saUrZ5ZqZWWc1SyCS9PIGI1cfYL56h9P/o2oPBh6JiI2BbwKntrBcMzProGaJ4JvA1ZLeKmlifvWQmvN+s8zCJW0A7AH8oJ8ie/PCPSUXAbtIclfxZmYjQL91IBExTdJ9wBeBLUiV6XcBJ0XEpSWX/y3gc/R/yWt9YEFe31JJi4E1AHfWaGY2zDVtxhsRlwEvqrsoIz/29p8RMTufuTQs1mi1DZY1FZgK0NXVRW9vb5WQrAR/ttYpre57fX19lfZX7+ODp1RXJhXtAOwlaXdgPLCqpAsi4oBCmYXAZGChpLHAJODh+gVFxDRgGkB3d3f09PS0MexRbObl+LO1jqiw7/X29ra+v3ofH1StVIa3JCKOiogNImIKsB9wbV3yAJgBfCgP75PLvOgMxMzMhp92noE0JOlEYFZEzADOAs6XdA/pzGO/oY7HzMyqKdOZ4uGk/rAeJ7Wm2gY4MiKuLruSiOgFevPwcYXx/wLe21LEZmY2LJS5hPXhiHgM2BVYCzgIOKWtUZmZ2bBXJoHUWkrtDpwdEbfTuPWUmZmNImUSyGxJV5MSyFWSJgJ+HoiZ2ShXphL9YGBr4N6IeFLSGqTLWGZmNoqVOQO5JiJui4hHASLiIUp2ZWJmZi9d/Z6BSBoPrAysmTtVrNV7rAqsNwSx2XLY6gtXs3jJMy3PN+XIy1sqP2nCOG4/fteW12NmI1+zS1gfAz5FShazeSGBPEZ6NroNY4uXPMP8U/ZoaZ4qd/a2mnDM7KWjWWeK3wa+LemwiDhtCGMyM7MRYMBK9Ig4TdKbgSnF8hFxXhvjMjOzYa7MnejnAxsBc4Bn8+jac9LNzGyUKtOMtxvY3J0cmplZUZlmvHOBddodiJmZjSxlzkDWBO6SdAvwVG1kROzVtqjMzGzYK5NATmh3EGZmNvKUaYV1vaQNgU0i4peSVgbGtD80MzMbzgasA5H0UeAi4Pt51PrAJe0MyszMhr8yleifID3f/DGAiPgzsPZAM0kaL+kWSbdLulPSFxqUOVDSg5Lm5NdHWt0AMzPrjDJ1IE9FxNNS6slE0ljSfSADzgfsHBF9ksYBN0q6MiJuqit3YUQc2lLUZmbWcWXOQK6XdDQwQdK/Az8DLh1opkj68ttx+eV7SczMXiLKJJAjgQeBO0gdLF4BHFtm4ZLGSJoD/JPULfzNDYq9R9IfJF0kaXLJuM3MrMPKtMJ6Djgzv1oSEc8CW0taDbhY0pYRMbdQ5FJgekQ8JekQ4Fxg5/rlSJoKTAXo6uqit7e31VBGpVY/p76+vkqfrb8PGwzeX0eeMn1h7Ql8EdgwlxfpCtWqZVcSEY9K6gXeTrqzvTb+oUKxM4FT+5l/GjANoLu7O1rtcnxUmnl5y12zV+nOvcp6zF7E++uIVOYS1reADwFrRMSqETGxTPKQtFY+80DSBOBtwN11ZdYtvN0LmFc6cjMz66gyrbAWAHMrdKa4LnCupDGkRPXTiLhM0onArIiYAXxS0l7AUuBh4MAW12FmZh1SJoF8DrhC0vUs2xfWN5rNFBF/ALZpMP64wvBRwFGlozUzs2GjTAI5GegDxgMrtjccMzMbKcokkNUjYte2R2KDauJmR/Lac49sfcZzW10PQGvPXjezl4YyCeSXknaNiKvbHo0NmsfnncL8U1o7sFdp1TLlyMtbKm9mLx1l+8KaKWmJpMckPS7psXYHZmZmw1uZGwknDkUgZmY2spTpzv0iSbtLKnO2YmZmo0SZpHAG8H7gz5JOkbRpm2MyM7MRoMwlrF+SKtInAfsD10haQOp65IKIeKbNMVpFlSq4Z7Y2z6QJ41pfh1kdtxocmcq0wkLSGsABwAeA3wM/AnYkdXHS067grLpWW2BBSjhV5jNbXm41ODKV6UzxF8CmwPnAOyLi/jzpQkmz2hmcmZkNX2XOQE6PiGsbTYiI7kGOx8zMRogydSDXStoS2JzUnUlt/HntDMzMzIa3MpewjifVc2xOehrhbsCNgBOImdkoVqYZ7z7ALsADEXEQsBWwUlujMjOzYa9MAlmSH2u7VNKqpOebv6q9YZmZ2XBXphJ9Vn6y4JnAbFLX7re0NSozMxv2ylSi/1cePEPSTGDV/LCopiSNB24gXe4aC1wUEcfXlVmJVJfyeuAhYN+ImN/SFpiZWUf0m0AkrQ0cDWwM3AF8ucWD+1PAzhHRJ2kccKOkKyPipkKZg4FHImJjSfsBpwL7troRVp6k5tNPbTy+9Scam9lLXbM6kPOAJ4DTgJcB32llwZH05bfj8qv+KLQ3L3RGcBGwiwY6wtlyiYh+X9ddd12/08zM6jW7hLVORByTh6+SdFurC5c0hlRvsjHw3Yi4ua7I+sACgIhYKmkxsAawqG45U4GpAF1dXfT29rYaipXQ19fnz9Y6ptV9r+r+6n188DRLIJL0cqB2RjCm+D4iHh5o4RHxLLB1roS/WNKWETG3uI5GszVYzjRgGkB3d3e02v+NlVOlbyGzQTHz8pb3vUr7a4X1WP+aJZBJpLOH4kG+dhYStNCUNyIeldQLvB0oJpCFwGRgoaSxeZ0DJiYzM+u8fhNIRExZngVLWgt4JiePCcDbSJXkRTNIPfr+jnTD4rXhC+5mZiNCqe7cK1oXODfXg6wA/DQiLpN0IjArImYAZwHnS7qHdOaxXxvjMTOzQdS2BJLvFdmmwfjjCsP/At7brhjMzKx9/JxzMzOrpOwTCccAXcXyEfG3dgVlZmbDX5nu3A8Djgf+ATyXRwfwujbGZWZmw1yZM5DDgddExEPtDsbMzEaOMnUgC4DF7Q7EzMxGljJnIPcCvZIuJ3WQCEBEfKNtUZmZ2bBXJoH8Lb9WzC8zM7NSzwP5wlAEYmZmI0uZVlhrAZ8DtgDG18ZHxM5tjMvMzIa5MpXoPwLuBl4JfAGYD9zaxpjMzGwEKJNA1oiIs0gdI14fER8G3tTmuMzMbJgrU4n+TP57v6Q9gPuADdoXkpmZjQRlEshJkiYBR5Aeb7sq8Om2RmVmZsNemVZYl+XBxcBO7Q3HzMxGigHrQCRtIOliSQ9K+oekn0vyJSwzs1GuTCX62aQnB64LrA9cmsc1JWmypOskzZN0p6TDG5TpkbRY0pz8Oq7RsszMbPgpUweyVkQUE8Y5kj5VYr6lwBERcZukicBsSddExF115X4dEXuWDdjMzIaHMmcgiyQdIGlMfh0ADNgzb0TcHxG35eHHgXmkMxgzM3sJKJNAPgy8D3gAuB/YBziolZVImkJ6vO3NDSZvL+l2SVdK2qKV5ZqZWeeUaYX1N2Cv4rh8CetbZVYg6WXAz4FPRcRjdZNvAzaMiD5JuwOXAJuueiVqAAALQUlEQVQ0WMZUYCpAV1cXvb29ZVZtLerr6/Nnax3T6r5XdX/1Pj54FBGtzyT9LSJeUaLcOOAy4Koy3b9Lmg90R8Si/sp0d3fHrFmzWgnXSurt7aWnp6fTYdgoNOXIy5l/yh4tzVNlf62yntFI0uyI6B6oXJlLWA2XXyIAAWcB8/pLHpLWyeWQ9MYcj598aGY2ApRphdVImdOWHYAPAHdImpPHHQ28AiAiziDVp3xc0lJgCbBfVDklMjOzIddvApH0OI0ThYAJAy04Im5kgDOViDgdOH2gZZmZ2fDTbwKJiIlDGYiZmY0sVetAzMxslHMCMTOzSpxAzMysEicQMzOrpGozXjOzQTXlyMtbn2lma/NMmjCu9XVYv5xAzKzjqtwd7rvKO8+XsMzMrBInEDMzq8QJxMzMKnECMTOzSpxAzMysEicQMzOrxAnEzMwqcQIxM7NKnEDMzKyStiUQSZMlXSdpnqQ7JR3eoIwkfUfSPZL+IGnbdsVjZmaDq51dmSwFjoiI2yRNBGZLuiYi7iqU2Q3YJL+2A76X/5qZ2TDXtjOQiLg/Im7Lw48D84D164rtDZwXyU3AapLWbVdMZmY2eIakDkTSFGAb4Oa6SesDCwrvF/LiJGNmZsNQ23vjlfQy4OfApyLisfrJDWaJBsuYCkwF6Orqore3d7DDNKCvr8+frY0o3l87q60JRNI4UvL4UUT8okGRhcDkwvsNgPvqC0XENGAaQHd3d/T09Ax+sEZvby/+bG3EmHm599cOa2crLAFnAfMi4hv9FJsBfDC3xnoTsDgi7m9XTGZmNnjaeQayA/AB4A5Jc/K4o4FXAETEGcAVwO7APcCTwEFtjMfMzAZR2xJIRNxI4zqOYpkAPtGuGMzMrH18J7qZmVXiBGJmZpU4gZiZWSVOIGZmVokTiJmZVeIEYmZmlTiBmJlZJU4gZmZWiROImZlV4gRiZmaVOIGYmVklTiBmZlZJ2x8oZWa2PNKTIfqZdmr/86W+Wq2dfAZiZsNaRDR8XXfddf1Oc/IYGk4gZmZWiROImZlV0s5H2v5Q0j8lze1neo+kxZLm5Ndx7YrFzMwGXzsr0c8BTgfOa1Lm1xGxZxtjMDOzNmnbGUhE3AA83K7lm5lZZ3W6Ge/2km4H7gM+GxF3NiokaSowFaCrq4ve3t6hi3AU6evr82drI4b3185TO5u7SZoCXBYRWzaYtirwXET0Sdod+HZEbDLQMru7u2PWrFmDHqtBb28vPT09nQ7DrBTvr+0jaXZEdA9UrmOtsCLisYjoy8NXAOMkrdmpeMzMrDUdu4QlaR3gHxERkt5ISmYPDTTf7NmzF0n6a9sDHJ3WBBZ1Ogizkry/ts+GZQq1LYFImg70AGtKWggcD4wDiIgzgH2Aj0taCiwB9osS19MiYq12xTzaSZpV5rTVbDjw/tp5ba0DsZHF/5A2knh/7TzfiW5mZpU4gVjRtE4HYNYC768d5ktYZmZWic9AzMysEieQUUbS2yX9UdI9ko5sMH0lSRfm6Tfnm0HNOqZEx6yS9J28z/5B0rZDHeNo5QQyikgaA3wX2A3YHNhf0uZ1xQ4GHomIjYFvAk2e+WY2JM4B3t5k+m7AJvk1FfjeEMRkOIGMNm8E7omIeyPiaeAnwN51ZfYGzs3DFwG7qNkzRc3arETHrHsD50VyE7CapHWHJrrRzQlkdFkfWFB4vzCPa1gmIpYCi4E1hiQ6s2rK7NfWBk4go0ujM4n6ZnhlypgNJ95nO8QJZHRZCEwuvN+A1JV+wzKSxgKT8HNdbHgrs19bGziBjC63AptIeqWkFYH9gBl1ZWYAH8rD+wDXlumjzKyDZgAfzK2x3gQsjoj7Ox3UaNDpB0rZEIqIpZIOBa4CxgA/jIg7JZ0IzIqIGcBZwPmS7iGdeezXuYjNSnXMegWwO3AP8CRwUGciHX18J7qZmVXiS1hmZlaJE4iZmVXiBGJmZpU4gZiZWSVOIGZmVokTiFUmqUvSjyXdK2m2pN9JetcgLbtH0mWDsay8vFfm3oX/nHsbXrFBmb0a9VDcZJlflXSnpK8OVpwN1nGOpH0qzrtp/k6ekvTZJuWukLRa9Shbimm+pDWHYl3Wfk4gVknuYPES4IaIeFVEvJ50z8gGHYpnoHuaTgW+GRGbAI+Qeh1eRkTMiIhTWljtx4BtI+K/W5hnKD0MfBL4WrNCEbF7RDw6NCHZS4kTiFW1M/B0vpELgIj4a0ScBqnr+PwL/db8jIaP5fE9knolXSTpbkk/qvX2m59VcrekG4F315YraZX8TIhbJf1e0t55/IGSfibpUuDq/gLNy9+Z1LswpN6G39mg3IGSTs/D75U0V9Ltkm5oUHYGsApws6R9Ja0l6ec5xlsl7ZDLnSDpXElX51/f75b0FUl3SJopaVwud1yeb66kaY16QJb0eknX57O9qwbqcTYi/hkRtwLPNCtXOyvIn/PleZvnStq3QdleSd+UdIOkeZLeIOkX+czupEK5S3Kcd0qa2s96D5B0i6Q5kr6v9LgBG0kiwi+/Wn6Rftl+s8n0qcCxeXglYBbwStIdxYtJZyorAL8DdgTGk3pU3YTUOd5Pgcvy/F8CDsjDqwF/Ih28DyT1g7R6Yb1zGsSyJqkb+9r7ycDcBuUOBE7Pw3cA69fW2c829hWGfwzsmIdfAczLwycAN5LunN6KdKf0bnnaxcA783BxG84H3pGHzyF1KTMO+C2wVh6/L6kngTLf1QnAZ5tMn58/o/cAZxbGT2pQthc4NQ8fTupzat38HS8E1ihuDzABmFsYX1vXZsClwLg8/n+BD3Z6v/artZe7MrFBIem7pETwdES8AdgVeF3h+v0kUnJ4GrglIhbm+eYAU4A+4C8R8ec8/gJSEiIva6/CdfzxpIM0wDUR8XxnjxGxdaPwGowbqAuG3wDnSPop8IsBygK8Ddi8cOKwqqSJefjKiHhG0h2kLmRm5vF3kLYdYCdJnwNWBlYH7iQdYGteA2wJXJPXMQYY7P6e7gC+JulUUvL+dT/lZhTK3xm53ylJ95KS80PAJwv1YZNJ3/1DhWXsArweuDVvzwTgn4O4LTYEnECsqjtJv1gBiIhP5MrRWXmUgMMi4qriTJJ6gKcKo57lhf2wv4O6gPdExB/rlrUd8ESJWBeRHjI0NtIzTgbsrTUiDsnL3wOYI2nriHioySwrANtHxJK6GCFvb0Q8J+mZyD+5geeAsZLGk36Bd0fEAkknkJLkMosiHay3L7G9lUTEnyS9ntSv1JclXR0RJzYoWvv+nmPZ77K2PT2khLp9RDwpqZfG23NuRBw1mNtgQ8t1IFbVtcB4SR8vjFu5MHwV8PHCNf5XS1qlyfLuBl4paaP8fv+6ZR1WqCvZppVA8wH7OtKlIEi9Df9fs3kkbRQRN0fEcaQENLlZeVIdzKGF+RudCfWndnBdJOllhTiL/gisJWn7vPxxkrbIw4cqdZK5XCStBzwZEReQKt6rPlt8EumxyE9K2hR4U4MyvwL2kbR2XvfqkjasuD7rECcQqyQflN8JvFXSXyTdQqqc/nwu8gPgLuA2SXOB79PkjDci/kW6ZHV5rkT/a2HyF0l1AH/Iy/pif8vJl8Qa+TzwGaVehtcg9TrczFdzRfdc4Abg9gHKfxLoVmowcBdwyADlnxepBdSZpEtCl5C63a8v8zQpsZwq6XZgDvDmPHlTlr08BICkdZR6r/0McKykhZJWbRLKa4Fb8md4DHBSk7LNzCSdifyB9F3d1GB77gKOBa7O5a4h1aXYCOLeeM1GOKX7Zd6dk4zZkHECMTOzSnwJy8zMKnECMTOzSpxAzMysEicQMzOrxAnEzMwqcQIxM7NKnEDMzKyS/w8NYIrflbKmRQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "indicators.boxplot(column='LoanPaymentsOverdue', by='Male')\n",
    "plt.title('Loan Payments Overdue, by Gender')\n",
    "plt.xlabel('Gender: 0 is female, 1 is male')\n",
    "plt.ylabel('Loan Payments Overdue')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Let's do a simple linear regression to estimate the effect of Price Change on Loan Payments Overdue (note that there aren't too many observations, so the results will probably be biased."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We expect that for a 100% increase in price change, that the number of overdue loan payments changes by -0.12.\n",
      "We also find that the average difference in overdue loan payments between a male and a female (male-female) is -0.19.\n"
     ]
    }
   ],
   "source": [
    "import statsmodels.formula.api as sm   # Statsmodels is a library that will allow us to perform regressions\n",
    "result = sm.ols(formula=\"LoanPaymentsOverdue ~ PriceChange + Male\", data=indicators).fit()  # Define reg. formula and fit\n",
    "price_change_coef = round(result.params[1], 2)  # Determine coefficient for price change and round\n",
    "male_coef = round(result.params[2], 2) # Determine coefficient for males\n",
    "\n",
    "print(\"We expect that for a 100% increase in price change, that the number of overdue loan payments changes by {}.\".format(price_change_coef))\n",
    "print(\"We also find that the average difference in overdue loan payments between a male and a female (male-female) is {}.\".format(male_coef))\n",
    "\n"
   ]
  }
 ],
 "metadata": {
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}


fig=plt.figure(figsize=(8,4))
ax1=fig.add_subplot(121)
ax1.set_xlabel('homeschool')
ax1.set_ylabel('Count of Students')
ax1.set_title('Homeschool by Gender')
temp1.plot(kind='bar')

ax2=fig.add_subplot(122)
temp2.plot(kind='bar')
ax2.set_xlabel('homeschool')
ax2.set_ylabel('Probability of Getting Homeschooled')
ax2.set_title('Probability of Getting Homeschooled by Gender')





# In[16]:


# Let's look at how many homeschoolers/non-homeschoolers are religious (since it's BYU, afterall)

#stacked
temp3 = pd.crosstab(df['homeschool'], df['religious'])
temp3.plot(kind='bar', stacked=True, color=['red', 'blue'], grid=False)




# In[19]:


# Subsetting df to look at people who are male, not homeschooled, and religious

malenr = df.loc[(df["cmale"]==1) & (df["homeschool"]==0) & (df["religious"]==1), ["cmale","homeschool","religious"]]
malenr.head(10)


# In[21]:


# Let's look at people who are male, whose family makes more than $100k, and are homeschooled

richmalehs = df.loc[(df['cmale']==1) & (df['hhinc'] > 100000) & (df['homeschool']==1)]
richmalehs.head(10)


# In[22]:


# Dataframe 2: Crime Rates

df2 = pd.read_csv("/Users/mitchellpudil/Desktop/Crime_Rate/crime.csv")

# Let's look at how many rows are missing per column
df2.apply(lambda x: sum(x.isnull()), axis=0)


# In[24]:


# Let's replace robbery rates with the mean of robbery rates

df2['rob'].fillna(df2['rob'].mean(), inplace=True)


# In[29]:


# Let's for the same for larceny and Snowfall
df2['larc'].fillna(df2['larc'].mean(), inplace=True)
df2['Snow'].fillna(df2['Snow'].mean(), inplace=True)

# Let's run that lambda function again to make sure that there are no missing values for the robbery rate
df2.apply(lambda x: sum(x.isnull()), axis=0)


# In[32]:


# Let's see if there's any correlation between snowfall and robbery

corr = np.corrcoef(df2['Snow'], df2['rob'])
corr[0][1]

# So there is a little bit of correlation between snowfall and robbery


# In[104]:


# The last data set we will use will come from a .txt file
indicators = pd.read_table('/Users/mitchellpudil/Desktop/indicators.txt', delim_whitespace=True)
indicators.head()
indicators.describe()


# In[98]:


indicators['PriceChange'].hist()


# In[161]:


# Let's look at the distribution of the average number of Loan Payments Overdue by Gender

indicators.boxplot(column='LoanPaymentsOverdue', by='Male')


# In[158]:


# Let's do a simple linear regression to estimate the effect of Price Change on Loan Payments Overdue
import statsmodels.formula.api as sm
result = sm.ols(formula="LoanPaymentsOverdue ~ PriceChange + Male", data=indicators).fit()
price_change_coef = round(result.params[1], 2)
male_coef = round(result.params[2], 2)

print("We expect that for a 100% increase in price change, that the number of overdue loan payments changes by {}.".format(price_change_coef))
print("We also find that the average difference in overdue loan payments between a male and a female (male-female) is {}.".format(male_coef))



# In[188]:


# For our next dataset, we will import data from an html file. The file we will be looking at is NFL statisticst)
r = requests.get("http://www.espn.com/mlb/standings/_/%20season/2017")
print(r.text[0:500])
# Parse html stored in our text into soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')


# In[272]:


import json

climate_data_json = json.load(open("/Users/mitchellpudil/Desktop/climate.json", 'r'))


# In[273]:


# Convert the data to a dataframe using pandas

climate_data_rough = pd.DataFrame(climate_data_json)
climate_data_rough.head(5)


# In[274]:


# Clean Data
df = climate_data_rough['data']  # Drops last column of NaN's
df.drop(df.tail(4).index,inplace=True)    # Drops last few rows of dataframe which are not data
df.head(5), df.tail(5)


# In[250]:


climate_clean = pd.DataFrame(df)
climate_clean.head(5)


# In[285]:


plt.plot(climate_clean)


# In[283]:




