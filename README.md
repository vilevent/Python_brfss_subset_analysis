#  Descriptive Statistics with NumPy
> Programming assignment from Introduction to Data Analytics course

Calculating **measures of central tendency** (such as mean and median) and **measures of variability** (such as interquartile range and standard deviation) for the dataset are all part of ***descriptive statistics***.


### Libraries used
```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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
##### Note: The CSV file named brfss-cdc should be located in the same folder as the Python file

### Adding a calculated column to 2D ndarray
- Weight change is defined as the difference between current weight and weight a year ago.
```python
weight_change = brfss_data[:, 2] - brfss_data[:, 3]
brfss_updated = np.column_stack((brfss_data, weight_change))
```

### Exploration of the dataset
Descriptive statistics help us summarize large amounts of data in a meaningful manner.


#### Descriptive statistics for the new `weight_change` attribute

      Mean: -7.38

      Median: -3.0

      Standard Deviation: 14.68

      Interquartile Range: 10.0
      
#### Interpretation
- A mean of -7.38 denotes that there is a average weight *loss* of 7.38 lbs among the group of 20,000 people.
- With a median of -3.0 lbs, **50% of the data points fall below that value**. -3.0 is the midpoint of the distribution.
- Since mean < median, the weight change data has a left-skewed distribution. This is supported by the histogram below. Most of the weight changes are **negative**. 
```python
sns.displot(data=weight_change, aspect=2, binwidth=4, color="purple")
plt.xlim(-115, 60)
plt.ylim(0, 7000)
plt.xlabel("Weight Change", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.show()
```
![Histogram](https://user-images.githubusercontent.com/96803412/148448968-51849b50-8c7b-4d67-a94f-039351f00442.png)
- Given that the mean and median differ, it indicates that there are outliers in the weight change data. The mean is sensitive to outliers. So, it is **more suitable to use the median as our measure of central tendency**. 

From the scatterplot below, we can visually recognize the data points that are substantially different from the other data points.
```python
plt.figure(figsize=(12, 8))
sns.scatterplot(data=weight_change, color="red", alpha=0.4)
plt.ylabel("Weight Change", fontsize=12)

plt.show()
```
![Scatterplot](https://user-images.githubusercontent.com/96803412/148458494-b410250e-9c3e-41cf-ab47-8011e67616a2.png)

### Analyzing the data, per gender
To do the analysis, we first split the NumPy array into subarrays based on the distinct values within the gender column.
```python
split_arr = [brfss_updated[brfss_updated[:, 5] == k] for k in np.unique(brfss_updated[:, 5])]
```
- `split_arr` is a list containing two ndarrays, from which we can index on.

**Data related to males: `split_arr[0]`**
```python
array([[    1,    77,   175, ...,    70,     1,     0],
       [    7,    31,   194, ...,    71,     1,    -9],
       [    8,    45,   170, ...,    67,     1,    -7],
       ...,
       [19995,    73,   224, ...,    69,     1,     0],
       [19997,    35,   200, ...,    73,     1,    -6],
       [20000,    83,   170, ...,    69,     1,    -4]])
```
**Data related to females: `split_arr[1]`**
```python
array([[    2,    33,   125, ...,    64,     2,    -7],
       [    3,    49,   105, ...,    60,     2,     0],
       [    4,    42,   132, ...,    66,     2,    -4],
       ...,
       [19996,    23,   215, ...,    66,     2,   -69],
       [19998,    57,   216, ...,    65,     2,   -22],
       [19999,    81,   165, ...,    67,     2,     0]])
```
---------------------

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

#### Printing the output (first 5 rows)
```python
print("First Five Rows of the Data:", brfss_data[:5,], sep="\n")
```
