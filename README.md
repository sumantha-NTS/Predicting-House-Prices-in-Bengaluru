# Predicting-House-Prices-in-Bengaluru
This project predicts price of new houses in Bengaluru.\
Data is taken from kaggle : https://www.kaggle.com/architsingh15/bengaluru-house-prices

## Feature Details :


## Algirithm Used for Prediction :
Following are the algorithms used for predicting new house prices and performance metrics used are RMSE and R square value.
|Sl.No.|      Algorithm      |RMSE|R2 (%)|
|:----:|:-------------------:|:----------:|:---------:|
|1.    | Linear Regression   |    0.439   |    64.60  |
|2.    | Ridge               |    0.44    |    64.56  |
|3.    | Lasso               |    0.44    |    64.56  | 
|4.    | KNN                 |    0.42    |    67.56  |
|5.    | Decision Tree       |    0.374   |    74.38  |
|6.    | Neural Network      |    0.314   |    81.87  |
|7.    | XG Boost            |    0.343   |    78.45  |
|8.    | Random Forest       |    0.48    |    57.73  |

From the above table, it is evidend that the best regressor for this problem is **XGBoost**. So for the app building, XGBoost is considered for predicting new House Prices.

## Deployment :
I have used **Streamlit** library and **Heroku** platform to deploy the app.\
App URL : 
