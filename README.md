# Telco-Customer-Churn-Project
This project analyzes internal customer churn data to identify key factors influencing churn at a telecommunications company. I used Python for data preprocessing, exploratory data analysis (EDA), and visualizations, to develop actionable strategies to reduce churn and improve customer retention.

The steps that I took in the python file attach are:
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
