# Analyzing BRFSS Data Assignment

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file and create a NumPy array called brfss_data
# Set the resulting array's data type to int
brfss_data = np.genfromtxt('C:/Users/leven/Desktop/UNF/CAP4784/CAP4784/Lab 4/brfss-cdc.csv', dtype=np.int32, delimiter=',', skip_header=1)

# Display first 5 rows and shape of the NumPy array brfss_data
print()
print("First Five Rows of the Data:")
# Row indexing starts at 0
print(brfss_data[:5])
print("Shape of the data:", brfss_data.shape)
print()

# Weight change = difference between current weight and weight a year ago.
# Column 2 is current weight, Column 3 is weight a year ago.
weight_change = brfss_data[:, 2] - brfss_data[:, 3]
print("Descriptive Statistics for Weight Change Data:")

# Calculate & display mean for weight change
mean_val = np.mean(weight_change)
print("Mean:", mean_val.round(decimals=2))

# Calculate & display median for weight change
median_val = np.median(weight_change)
print("Median:", median_val)

# Calculate & display standard deviation for weight change
std_dev_val = np.std(weight_change)
print("Standard Deviation:", std_dev_val.round(decimals=2))

# Calculate & display IQR for weight change
quartile75, quartile25 = np.percentile(weight_change, [75, 25])
iqr_val = quartile75 - quartile25
print("Interquartile Range:", iqr_val)
print()

# Histogram showing distribution for weight change
sns.displot(data=weight_change, aspect=2, binwidth=4, color="purple")
plt.xlim(-115, 60)
plt.ylim(0, 7000)
plt.xlabel("Weight Change", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.show()

# Scatterplot to visually see outliers in weight change data
plt.figure(figsize=(12, 8))
sns.scatterplot(data=weight_change, color="red", alpha=0.4)
plt.ylabel("Weight Change", fontsize=12)

plt.show()

# Concatenate 1d weight_change array as column to the 2d brfss_data array
brfss_updated = np.column_stack((brfss_data, weight_change))

# Display first 5 rows and shape of concatenated array brfss_updated
print("First Five Rows of the Data with Weight Changes:")
print(brfss_updated[:5])
print("Shape of the data:", brfss_updated.shape)
print()

# Split the concatenated array based on the gender column (5th column)
# where gender 1 = male and gender 2 = female.
split_arr = [brfss_updated[brfss_updated[:, 5] == k] for k in np.unique(brfss_updated[:, 5])]

# Display first 5 rows of data related to males in split_arr array.
# Display shape of this array relevant to males data.
print("First Five Rows of the Data relevant to Males:")
print(split_arr[0][:5])
print("Shape of the data:", split_arr[0].shape)
print()

print("Descriptive Statistics for Data relevant to Males:")
# Calculate & display mean for males data
male_mean_val = np.mean(split_arr[0])
print("Mean:", male_mean_val.round(decimals=2))

# Calculate & display median for males data
male_median_val = np.median(split_arr[0])
print("Median:", male_median_val)

# Calculate & display standard deviation for males data
male_std_dev_val = np.std(split_arr[0])
print("Standard Deviation:", male_std_dev_val.round(decimals=2))

# Calculate & display IQR for males data
male_q75, male_q25 = np.percentile(split_arr[0], [75, 25])
male_iqr_val = male_q75 - male_q25
print("Interquartile Range:", male_iqr_val)
print()

# Display first 5 rows of data related to females in split_arr array.
# Display shape of this array relevant to females data.
print("First Five Rows of the Data relevant to Females:")
print(split_arr[1][:5])
print("Shape of the data:", split_arr[1].shape)
print()

print("Descriptive Statistics for Data relevant to Females:")
# Calculate & display mean for females data
female_mean_val = np.mean(split_arr[1])
print("Mean:", female_mean_val.round(decimals=2))

# Calculate & display median for females data
female_median_val = np.median(split_arr[1])
print("Median:", female_median_val)

# Calculate & display standard deviation for females data
female_std_dev_val = np.std(split_arr[1])
print("Standard Deviation:", female_std_dev_val.round(decimals=2))

# Calculate & display IQR for females data
female_q75, female_q25 = np.percentile(split_arr[1], [75, 25])
female_iqr_val = female_q75 - female_q25
print("Interquartile Range:", female_iqr_val)
print()
