# Coursera Applied Data Science Capstone Project

Completed by Martti Nirkko on 5th December, 2022.

This repository contains all the notebooks and scripts used to complete the final data science project of the Coursera module "IBM Data Science".
In this Professional Certificate, learners developed and honed hands-on skills in Data Science and Machine Learning.

### Executive summary
* In this project, criteria for successful booster landings of SpaceX launches were evaluated. The relevant features that were investigated included payload mass, launch site and orbit.
* Data collection was performed using a combination of available datasets and webscraping. Data cleaning and wrangling was used to fill in missing data or convert it to numerical values.
* Next, exploratory data analysis (EDA) was done using SQL queries and Python libraries, in particular the seaborn package for data visualization. Interactive visual analytics and the creation of a dashboard allow for a high level presentation of the data to management.
* Finally, a set of Machine Learning (ML) algorithms was used to predict the success or failure of future launches. For this, the dataset was split into train and test data.
* We found that the percentage of successful launches increased significantly with time. Certain launch sites and orbits had a higher success rate, as did missions with higher payloads. Predictive modeling yielded 83% accuracy for predicting successful landings.

<p align="center">
![image](https://github.com/mnirkko/datascience/assets/6942556/2c16bf9a-659c-4735-b314-2d493ee73868)
</p>

### Methodology
* Data collection -- Loading data via API and web scraping, decoding the data and converting it to DataFrames
* Data wrangling -- Filling in missing values, converting labels to numerical values
* Exploratory data analysis -- Analysing the data using visualization and SQL
* Interactive visual analytics -- Enabling potential stakeholders to navigate the data using Folium and Plotly Dash
* Predictive analysis using classification models -- Building the dataset, standardising the data, splitting into training/test datasets, tuning and optimizing models using training data, evaluating prediction accuracy using test data, comparing results.

<p align="center">
![image](https://github.com/mnirkko/datascience/assets/6942556/c35c8c7c-77a0-4090-892d-cb54e8b4e192)
</p>

### Results
* Exploratory data analysis showed that successful launches are correlated with the flight number (better performance in recent years), the payload (better performance with higher mass), and to some extent with the launch site and orbit used.
* Interactive analytics showed that the launch sites are close to the coastline, and further away from more densely populated areas (roads, cities etc.) clearly to reduce collateral damages in the event of a failed launch.
* Predictive analysis showed decent results for logistic regression (LogReg), support vector machines (SVM), and k nearest neighbors (KNN). For these methods, the classifier correctly predicted the outcome of a launch 83% of the time. The main issue remaining are false positives, as indicated by the confusion matrix.

<p align="center">
![image](https://github.com/mnirkko/datascience/assets/6942556/6695f459-11c0-4a5d-967e-2b34b720a291)
</p>

<p align="center">
![image](https://github.com/mnirkko/datascience/assets/6942556/939f384b-fd2e-4e6c-9e81-fdbd1107eac6)
</p>
