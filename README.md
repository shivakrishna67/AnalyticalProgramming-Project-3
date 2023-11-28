# AnalyticalProgramming-Project-3
Motor Vehicle Crashes in New York City Analysis

## Overview
This project explores and analyzes motor vehicle crash data in New York City (NYC). The dataset used in this analysis contains information about various aspects of motor vehicle crashes, including time and location, contributing factors, vehicle types, and severity of incidents.
The primary objectives of this project are:

* Exploratory Data Analysis (EDA): Conduct a thorough exploration of the motor vehicle crash data to identify patterns, trends, and insights.
*  Temporal and Spatial Analysis: Investigate how crash rates vary over time (hourly, daily, monthly) and across different locations within NYC.
* Contributing Factors: Analyze the contributing factors to motor vehicle crashes, such as distracted driving, speeding, and impaired driving.
* Comparative Analysis: Compare the motor vehicle crash data in NYC to national averages or other urban areas to identify unique characteristics and potential areas for improvement.

## Dataset
Our journey begins with the requisite preparation, importing the essential Python libraries. The 'sodapy' library, in particular, stands out, as it facilitates seamless interaction with the Socrata API. The introductory print statements signal the initiation of this data-fetching adventure.

The subsequent steps involve setting up the Socrata API client, a gateway to the treasure trove of NYC Open Data. The endpoint, "data.cityofnewyork.us," serves as our portal to the dataset of interest, identified by the unique identifier "h9gi-nx95." The 'get' method of the Socrata client is enlisted to retrieve the data. It's noteworthy that a limit of 180,030 is imposed, a strategic decision informed by the data description suggesting a more extensive dataset than the default 1,000 observations.

## Tools and Libraries
The analysis is performed using Python programming language and utilizes popular data analysis and visualization libraries, including:
Pandas: Data manipulation and analysis.
NumPy: Numerical operations and calculations.
Matplotlib and Seaborn: Data visualization to create insightful plots and charts.
Project Structure

## The project structure is organized as follows:
* data/: Contains the dataset used in the analysis.
* notebooks/: Jupyter notebooks detailing the step-by-step analysis process.
* scripts/: Python scripts for specific functions or analyses.
* visualizations/: Saved visualizations generated during the analysis.
