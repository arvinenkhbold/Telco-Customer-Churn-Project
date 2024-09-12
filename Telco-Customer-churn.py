import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

#Read me
#This code is used to clean, prepare, and visualize the Telco Customer Churn dataset.
#The steps that we took in this python file are:
#1. Imported the necessary libraries such as pandas, numpy, matplotlib, seaborn, and sklearn.
#2. Loaded the Telco Customer Churn dataset from a CSV file with the hopes of cleaning and visualizing
#3. Displayed basic information about the dataset using df.info()
#4. Displayed the summary of the dataset using df.describe()
#5. Converted the 'TotalCharges' column to a numeric type as it was identified as an object.
#6. Looked for missing values in the dataset using df.isnull().sum()
#7. Since the dataset contains over 7000 entries, I decided to drop the customers with missing values since it was only 11 missing values, and would not affect the dataset significantly.
#8. I then converted the 'SeniorCitizen' column to boolean values.
#9. Standardized the values of 'No internet service' and 'No phone service' to 'No'.
#9. I then removed the 'CustomerID' column as it is not needed for the analysis, improve anonimity, and make dataset cleaner.
#10. I then created a new column 'TenureYears' to make it easier to track if customer is a long term customer or not.
#11. Created visualizations to check for outliers in the dataset.
#12. Identified columns with non-numeric values and converted them to numeric values.
#13. Converted the categorical variables into dummy variables so that they can be used in the analysis.
#14. Created a correlation matrix to identify the correlation between the variables.
#15. Created scatter plots to identify the relationship between the variables..
#17. Identified the top 10 factors correlated with churn.
#18. Created a bar plot to identify the top 10 factors correlated with churn.
#19. Performed K-means clustering to identify the segments in the dataset.
#20. Visualized the segments.
#21. Analyzed churn rate by segment.
#22. Created a segment analysis DataFrame.
#23. Provided recommendations based on segment analysis.


df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Display basic information about the dataset
print(df.info())

#Basic information revealed that total charges is identified as object but not numeric.
#Code will convert the total charges to numeric.
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#Look for missing values in the dataset
print("Missing values:")
print(df.isnull().sum())

#Missing values revealed that there are 11 missing values in the 'TotalCharges' column.
#The code below will drop the missing values in the 'TotalCharges' column.
df = df.dropna(subset=['TotalCharges'])

#And now we will look for missing values in the dataset again to confirm that the missing values have actually been dropped.
print("Missing values:")
print(df.isnull().sum())

#The missing values have been dropped successfully.
#We will now convert the 'SeniorCitizen' column to boolean values.
df['SeniorCitizen'] = df['SeniorCitizen'].astype(bool)

#We will now check the datatypes of the columns to confirm that the 'SeniorCitizen' column has been converted to boolean values.
print(df.dtypes)

#The 'SeniorCitizen' column has successfully been converted to boolean values.

#From first inspection, there are inconsistencies in the values entered. We will change, "No internet service" and "No phone service" to just "No" for the following columns:
#'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'.
df['MultipleLines'] = df['MultipleLines'].replace({'No phone service': 'No'})
df['OnlineSecurity'] = df['OnlineSecurity'].replace({'No internet service': 'No'})
df['OnlineBackup'] = df['OnlineBackup'].replace({'No internet service': 'No'})
df['DeviceProtection'] = df['DeviceProtection'].replace({'No internet service': 'No'})
df['TechSupport'] = df['TechSupport'].replace({'No internet service': 'No'})
df['StreamingTV'] = df['StreamingTV'].replace({'No internet service': 'No'})
df['StreamingMovies'] = df['StreamingMovies'].replace({'No internet service': 'No'})

#I now want to remove the 'CustomerID' column as it is not needed for the analysis, improve anonimity, and make dataset cleaner.
df = df.drop(columns=['customerID'])

#Now lets do some feature engineering. The tenure section can be confusing. This column is in the number of months, and it is hard to track if customer is a long term customer or not.
#I will create a new column 'TenureYears' to make it easier to track if customer is a long term customer or not.
df['TenureYears'] = df['tenure'] / 12

#Lets now do a starter visualization to see if there are any inconsistencies in the dataset visually.
sns.pairplot(df[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']])
plt.show()
#This plot shows that there are no inconsistencies and outliers in the dataset.

print(df.describe())
#From this numerical summary, we can infer a couple of things:
#1. The average tenure is 32 months, with a standard deviation of 24 months.
#2. The average monthly charges is $64.80, with a standard deviation of $30.09.
#3. The average total charges is $2283.30, with a standard deviation of $2266.77.

#Now we will check if there are any non-numeric values in the dataset.
for column in df.columns:
    try:
        df[column].astype(float)
    except ValueError:
        print(f"Column '{column}' contains non-numeric values: {df[column].unique()}")

binary_columns = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
                  'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                  'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Churn']

for col in binary_columns:
    df[col] = df[col].map({'Yes': 1, 'No': 0, 'Male': 1, 'Female': 0})

#We will now convert the categorical variables into dummy variables.
df = pd.get_dummies(df, columns=['InternetService', 'Contract', 'PaymentMethod'], drop_first=True)
print("Columns after dummy variable creation:")
print(df.columns)

# Now try to create the correlation matrix
correlation_matrix = df.corr()

# Visualize the correlation matrix
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Scatter plots for key relationships
fig, axs = plt.subplots(2, 2, figsize=(20, 20))
sns.scatterplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', ax=axs[0, 0])
sns.scatterplot(data=df, x='TotalCharges', y='MonthlyCharges', hue='Churn', ax=axs[0, 1])
sns.scatterplot(data=df, x='tenure', y='TotalCharges', hue='Churn', ax=axs[1, 0])

sns.boxplot(data=df, x='Contract_Two year', y='MonthlyCharges', hue='Churn', ax=axs[1, 1])

plt.tight_layout()
plt.show()

# Identify top factors correlated with churn
churn_correlations = correlation_matrix['Churn'].sort_values(ascending=False)
print("Top factors correlated with churn:")
print(churn_correlations)

# Visualize top 10 correlations with churn
plt.figure(figsize=(12, 8))
sns.barplot(x=churn_correlations.index[:10], y=churn_correlations.values[:10])
plt.title('Top 10 Factors Correlated with Churn')
plt.xticks(rotation=45, ha='right')
plt.show()

# Select features for segmentation (you can adjust these based on correlation results)
segmentation_features = ['tenure', 'MonthlyCharges', 'TotalCharges']

# Normalize the features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[segmentation_features])

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Segment'] = kmeans.fit_predict(scaled_features)

# Visualize segments
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='tenure', y='MonthlyCharges', hue='Segment', style='Churn')
plt.title('Customer Segments')
plt.show()

# Analyze churn rate by segment
segment_churn = df.groupby('Segment')['Churn'].mean()
print("Churn rate by segment:")
print(segment_churn)

# Create segment analysis DataFrame
segment_analysis = df.groupby('Segment').agg({
    'tenure': 'mean',
    'MonthlyCharges': 'mean',
    'InternetService_Fiber optic': 'mean',
    'Contract_Two year': 'mean'
})

print("\nRecommendations based on Segment Analysis:")
for segment, churn_rate in segment_churn.items():
    print(f"Segment {segment}:")
    segment_data = segment_analysis.loc[segment]
    print(f"  - Churn Rate: {churn_rate:.2%}")
    print(f"  - Avg. Tenure: {segment_data['tenure']:.1f} months")
    print(f"  - Avg. Monthly Charges: ${segment_data['MonthlyCharges']:.2f}")
    print(f"  - % on Fiber Optic: {segment_data['InternetService_Fiber optic']:.2%}")
    print(f"  - % on Two-Year Contract: {segment_data['Contract_Two year']:.2%}")
    
    if churn_rate > 0.3:
        print("  - High churn risk. Focus on retention strategies.")
    elif segment_data['tenure'] < 12:
        print("  - New customers. Implement onboarding and early engagement programs.")
    elif segment_data['MonthlyCharges'] > 70:
        print("  - High-value customers. Offer loyalty rewards and premium services.")
    else:
        print("  - Stable segment. Maintain satisfaction and gradually increase engagement.")
    print()