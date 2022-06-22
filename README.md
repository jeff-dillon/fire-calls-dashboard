# fire-calls-dashboard
This is a coding challenge for the Code Louisville Data Analysis 2 class. The 
goal of this challenge is to get experience creating dashboards in Tableau. 

## Introduction
In this exercise you will use and extend an existing data cleaning script to 
create a Tableau dashboard using Fire District Call data from the Louisville Open Data website. 

Data Source: 
[Louisville/Jefferson County Fire Districts calls for service](https://data.louisvilleky.gov/dataset/louisvillejefferson-county-fire-districts-calls-service) 

### Step 1: Tableau Setup

Create an account on the [Tableau Public](https://public.tableau.com/en-us/s/) website and downlaod the app.


### Step 2: Script Setup

Clone this repo, create a virtual environment, and install the required libraries from the `requirements.txt` file.

### Step 3: Clean the Data

Run the `clean-data.py` script to generate the `data/clean/fire_dashboard.csv` file fo use in Tableau.

### Challenge: Create a Dashboard

Create a Tableau dashboard with multiple visualizations of the data. Example visualizations include:

- Geographic heatmap of calls by zip
- Line graph of calls by month
- Heatmap of calls by priority
- Heatmap of calls by Event Category
- Graph of calls by Agency Name

Your dashboard can include dynamic filtering, sorting graph elements, and other Tableau features. Publish the Dashboard to Tableau Public and share your dashboard in the #may22-course2-data-analytics Slack channel.

[Example dashboard](https://public.tableau.com/app/profile/jeff.dillon3251/viz/FireCalls_16558458057010/FireCallsDashboard)

[Tableau How-to Videos](https://public.tableau.com/en-us/s/resources)



### Bonus: Extend the Script and Dashboard

Update the cleaning script to include a new column called `TIME_TO_CLEAR_CATEGORY`. This column should categorize each record based on the `TIME_TO_CLEAR` column into the following categories:

- Less than 5
- 5 to 10
- 10 to 20
- 20 or more

Use this new column to create a Histogram visualization. You can create a pull request against this repo and I will review the code. You can include a link to your dashboard in the pull request too,
