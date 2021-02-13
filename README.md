# Predicting-House-Prices-in-Bengaluru
This project predicts price of new houses in Bengaluru.\
Data is taken from kaggle : https://www.kaggle.com/architsingh15/bengaluru-house-prices

## Varible Details :
The dataset consists of 13320 records with 8 input and 1 output variables. There are missing values in few variables. The missing values are imputed by understanding the visualization and detailed analysis which is present in attached **.ipynb** file. \
Also the input variables with **high corelation** are removed to avoid the overfitting.\
The dataset contains input variables like area_type, availability, society, location, no. of bedrooms, bath, total sqft, balcony and price as output variable. Particularly the location variable contains improper names with 1305 unique names. These names are replaced with proper names. After replacing with proper names the unique values in location varible is reduced to 925.\
The **no. of bedroom variable** contain only one record for no. of bedrooms greater than 11 BHK. To remove the outliers, the no. of bedroom variable is restricted to 11 BHK.\
The **total sqft variable** contains values with different units. These values are converted to common unit i.e., sqft.\
The continuous variable which are **total sqft and price** doesnot follow normal distribution. Hence **log transformation** is done before splitting and fitting the data to model. 


## Algirithm Used for Prediction :
Following are the algorithms used for predicting new house prices and performance metrics used are RMSE and R square value.
|Sl.No.|      Algorithm      |RMSE|R2 (%)|
|:----:|:-------------------:|:----------:|:---------:|
|1.    | Linear Regression   |    0.439   |    64.60  |
|2.    | Ridge               |    0.44    |    64.56  |
|3.    | Lasso               |    0.44    |    64.56  | 
|4.    | KNN                 |    0.42    |    67.56  |
|5.    | Decision Tree       |    0.374   |    74.38  |
|6.    | XG Boost            |    0.314   |    81.87  |
|7.    | Random Forest       |    0.343   |    78.45  |
|8.    | Neural Network      |    0.48    |    57.73  |

From the above table, it is evidend that the best regressor for this problem is **XGBoost**. So for building API, XGBoost is considered for predicting new House Prices.

## Deployment :
I have used **Streamlit** library and **Heroku** platform to deploy the app.\
App URL : https://house-price-prediction-bnr.herokuapp.com/
