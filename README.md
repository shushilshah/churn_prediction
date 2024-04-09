Project: Bank customer churn prediction

Problem Statement:
The dataset is given with the objective to find whether the customer within the bank will left or not.The leaving number of customer of any bank denotes the bad review of bank in most of the cases. The customer contains number of characteritics like credit score, country of residence, gender, balance in their account, member active or not.

Project's Workflow:

1. Data collection:
   Data for the project is collected from kaggle site for the learning purposes. It consists of 12 columns, and we have to determine whether a customer will left the bank or not on the basis of given data input.

2. Exploratory Data Analysis:
   In this phase, different visualizations are explored in order to understand the co-relation between different columns like barplot, countplot, piechart, boxplot etc.

3. Data/Model Training:
   The data is first split into train and test in the ratio 8:2, then the data is fitted with different models like random forest classifier, logistic regression.

4. Model Selection:
   The Random Forest Classifier model is selected among all because it has highest accuracy score which is 87%.

5. Deployment:
   The model's deployment is done locally using Streamlit framework. And when providing input to the model, the model gives accurate result.
