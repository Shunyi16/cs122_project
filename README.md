# CS122_Project

# Project Title: JobMarket Research

# Authors: Shunyi Liu, Tam Ly

# Project Description: (5 Sentences) 
This project is to gather datas from the job market about current hiring situation and the trends observed over the past 12 months. We aim to present a comprehensive overview of companies actively engaged in the hiring process, along with the corresponding hiring rates for various positions. We will list the hiring companies, hiring positions, and the start and end dates. We will also include the features for date/field/position filtering which allow users to look at a specific position at a specific time. Besides that, we will use appropriate graphs to present different dataset, such as hiring rate for a position, the trendline for the past 12 months, the active hiring months, etc.

# Project Outline/Plan:
## Interface Plan:
The interface will include two windows, which are for collecting data and analyzing data. The program allows users to interact through buttons to collect, update, and analyze data, which are the opening job positions in the field of software development, and then extract the results in the form of charts. Users can choose the time or type of positions they want to collect data from the collecting window. Meanwhile, users can select the number of companies to display in the chart from the analyzing window. We will also include a small window showing the short description of the job along with the job link. 

## Data Collection and Storage Plan:
- For initial thought, we will store data using files and folders, such as spreadsheet, txt file etc
- We are thinking to collect data from job searching engines, such as LinkIn, HandShake, Indeed, Monster, Glassdoor, Ladder, Wellfound, Getwork, Snagajob. Then we will pick the best 5 websites for our data collection based on the functionality of these websites. 

## Data Analysis and Visualization Plan:
The analysis results will be displayed as a line graph. The x-axis is the company's name, and the y-axis is the number of job positions those companies are opening. The initial idea is that the ten companies that have the most opening positions will be chosen to display by default. Additional functions include selecting the number of companies depicted or a specific position.
