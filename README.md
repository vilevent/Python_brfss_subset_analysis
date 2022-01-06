#  Descriptive Statistics with NumPy
> Programming assignment from Introduction to Data Analytics course

Calculating **measures of central tendency** (such as mean and median) and **measures of variability** (such as interquartile range and standard deviation) for the dataset are all part of ***descriptive statistics***.


### Libraries used
```python
import numpy as np
```

### Dataset at a glance
- Behavioral Risk Factor Surveillance System (**BRFSS**) involves U.S. residents completing health-related telephone surveys.
- The data within the CSV file `brfss-cdc.csv` is from a 2000 BRFSS survey, with a random sample of 20,000 people. Here, we are analyzing a subset of the attributes from the original dataset.


#### The CSV file has six attributes: surveyrespondent (ID), age, current_weight (lbs), weightyrago (lbs), height (inches), and gender (where 1 denotes male and 2 denotes female).

![FirstFiveRows](https://user-images.githubusercontent.com/96803412/148419538-2a1fba94-375c-470a-bf50-abc3b623f543.png)


### Importing BRFSS data into a NumPy array
```python
brfss_data = np.genfromtxt('brfss-cdc.csv', dtype=np.int32, delimiter=',', skip_header=1)
```
### Exploration of data
Descriptive statistics help us summarize large amounts of data in a meaningful manner.


## Alternatives
There are other ways to complete some of the tasks like loading the data, calculating the mean of an array, and calculating the interquartile range (IQR), and printing the output to the user. The end results remain the same.

#### Loading the dataset
```python
brfss_data = np.loadtxt("brfss-cdc.csv", dtype=int, delimiter=",", skiprows=1)
```
- There are no missing values in the CSV file, so we can use **np.loadtxt()**
- If there were missing values in the file, we should use **np.genfromtxt()**

#### Calculating the mean (and rounding it) for the data relevant to males
```python
male_mean_val = split_arr[0].mean().round(decimals=2)
```

#### Calculating the IQR for the data relevant to females
```python
from scipy.stats import iqr
female_iqr_val = iqr(split_arr[1])
```
- This code is an alternative to using the np.percentile() function.

#### Printing the output (first 5 rows)
```python
print("First Five Rows of the Data:", brfss_data[:5,], sep="\n")
```
