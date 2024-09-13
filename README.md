# Telco-Customer-Churn-Project
This project analyzes internal customer data to identify key factors influencing churn at a telecommunications company. I used Python for data preprocessing, exploratory data analysis (EDA), and visualizations, to identify key variables that are driving churn, and developing strategies to alleviate the issue and improve customer retention.

- **Report**: https://docs.google.com/document/d/1lmg9bzFqzgwDnIv7HMhHRuL5lND4CtaJoRXlmtWmae4/edit?usp=sharing
- **Presentation**: https://docs.google.com/presentation/d/1LOeq93qVwTSpHW84qBq5JeKzkFNPlfEiixWXA6TTDc0/edit?usp=sharing

# Importance:
Customer churn is a significant issue in the highly competitive telecommunications industry. High churn rates not only affect revenue but also increase customer acquisition costs. Retaining existing customers is more cost-effective than acquiring new ones, making churn reduction an important factor in the companys business environment. This project is essential for Telco to maintain its competitive edge by improving customer loyalty and optimizing resource allocation.

# What Was Done in Python:
Data Preprocessing: Cleaned and prepared the dataset, including handling missing values, converting categorical variables to numerical ones, and creating a new feature, TenureYears, to better assess customer behavior over time.

Exploratory Data Analysis (EDA): Conducted a thorough analysis of the data to uncover key patterns and correlations, such as the impact of contract length, monthly charges, and internet service type on churn.

Visualization: Created visual representations of the data to highlight the relationships between variables and their impact on churn. Key visualizations include scatter plots for outlier detection, correlation matrices, and bar charts of top factors correlated with churn.

Clustering: Used K-means clustering to segment customers based on tenure and monthly charges, providing a deeper understanding of customer segments and their respective churn rates.

# Steps I took in Python:
- #1. Imported the necessary libraries such as pandas, numpy, matplotlib, seaborn, and sklearn.
- #2. Loaded the Telco Customer Churn dataset from a CSV file with the hopes of cleaning and visualizing
- #3. Displayed basic information about the dataset using df.info()
- #4. Displayed the summary of the dataset using df.describe()
- #5. Converted the 'TotalCharges' column to a numeric type as it was identified as an object.
- #6. Looked for missing values in the dataset using df.isnull().sum()
- #7. Since the dataset contains over 7000 entries, I decided to drop the customers with missing values since it was only 11 missing values, and would not affect the dataset significantly.
- #8. I then converted the 'SeniorCitizen' column to boolean values.
- #9. Standardized the values of 'No internet service' and 'No phone service' to 'No'.
- #10. I then removed the 'CustomerID' column as it is not needed for the analysis, improve anonimity, and make dataset cleaner.
- #11. I then created a new column 'TenureYears' to make it easier to track if customer is a long term customer or not.
- #12. I then created visualizations to check for outliers in the dataset.
- #13. Identified columns with non-numeric values and converted them to numeric values.
- #14. Converted the categorical variables into dummy variables so that they can be used in the analysis.
- #15. Created a correlation matrix to identify the correlation between the variables.
- #16. Created scatter plots to identify the relationship between the variables.
- #17. Created a box plot to identify the relationship between the 'Contract_Two year' and 'MonthlyCharges' columns.
- #18. Identified the top 10 factors correlated with churn.
- #19. Created a bar plot to identify the top 10 factors correlated with churn.
- #20. Performed K-means clustering to identify the segments in the dataset.
- #21. Visualized the segments.
- #22. Analyzed churn rate by segment.
- #23. Created a segment analysis DataFrame.
- #24. Provided recommendations based on segment analysis.

# Results: 
The analysis revealed that certain factors, such as contract length, monthly charges, internet service type, payment methods, and customer tenure, are significant predictors of customer churn. Key findings include:
- **Contract Length:** Customers with month-to-month contracts are more likely to churn compared to those with longer-term contracts.
- **Monthly Charges:** Higher monthly charges are strongly associated with an increased likelihood of churn.
- **Internet Service Type:** Customers using fiber optic internet services are more prone to churn compared to those using DSL or no internet service.
- **Payment Methods:** Customers using electronic checks as a payment method are more likely to leave.
- **Customer Tenure:** Longer tenure is associated with increased loyalty and lower churn rates.

# Strategies to Implement:
Incentives for Long-Term Contracts: 
- **Offer discounts or incentives:** Customers on month-to-month contracts were more likely to churn so offering discounts or complimentary service add-on's will to encourage them to switch to longer-term agreements.
- **Pricing Revision:** Consider revising the pricing structure, especially for customers with high monthly charges as these individuals are less likely to see the percieved value of Telco's services. We have also discovered from the dataset that our longer term customers tend to stay with us, due to the services that Telco offers.
- **Improve Fiber Optic Service Reliability:** Individuals with this type of internet service, value performance and reliability over anything else. Since these customers are more prone to churn, there are expectations that are not met. Telco can improve this by enhance the infrastructure and service quality for these customers to meet their high expectations.
- **Promote Automatic Payment Options:** There is a service gap with customers using automatic payments and electronic checks, so simplyfying or  promoting the use of these methods will be a convenience for the customer thus being less likely to churn
- **Strengthen Customer Loyalty Programs:** Our long term customers are more liekly to stay with the company so developing and implementing a loyalty program can foster increased retention, as well as engage our customers with shorter term contracts.

# Deliverables:
- **Report**: A detailed analysis report that includes findings, methodologies, strategic recommendations, etc...
- **Python Code/Visualizations:** The Python code used for the analysis, along with the generated visualizations. This code can be utilized in the future to create machine learning models such as Random Forests or a more advanced k-means clustering, which can improve the accuracy of churn predictions.
- **Presentation**: A presentation was designed to effectively communicate the findings and recommendations to Telco's key stakeholders and aid them in decision making.

# Attachments:
- **Report**: https://docs.google.com/document/d/1lmg9bzFqzgwDnIv7HMhHRuL5lND4CtaJoRXlmtWmae4/edit?usp=sharing
- **Presentation**: https://docs.google.com/presentation/d/1LOeq93qVwTSpHW84qBq5JeKzkFNPlfEiixWXA6TTDc0/edit?usp=sharing
