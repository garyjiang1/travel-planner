# Itinerary-Microservice

## Introduction

This is a simple Flask based Travel Itinerary microservice.


## Setup

- Please make sure that your system has already installed:
  - Python (3.9 or greater)
  - MySQL Community Server

Use pycharm to develop and run this application. This project already comes with a ```venv``` folder that has all the prerequisites. 
You just need to open the project in pycharm. If it doesn't work then delete the venv folder and follow the instruction below.


Open the project in PyCharm and create a new virtual environment for the project. You can find the instructions
online in the PyCharm documentation. After creating the virtual environment, open a terminal window using the bottom
pane (open the terminal within PyCharm). In the root of the directory, execute the command

```pip install -r requirements.txt```

This should install the necessary Python requirements.

## Executing the Program

Select the file ```application.py``` in the directory ```./src``` in the file explorer. Right click on the file and
select "run." In the execution panel at the bottom of the screen, you should see messages about "running on ... ..."
This indicates that the web application has started.
Ensure that you see the expected output of root url ```http://127.0.0.1:5000```:
<img width="705" alt="Screen Shot 2022-10-31 at 7 01 46 PM" src="https://user-images.githubusercontent.com/52360459/199125834-760b9fde-b311-4ef5-8b8a-e80c0b4b2f10.png">

Alternatively, visit ```http://127.0.0.1:5000/api/health``` to see the app health check expected as below:
<img width="742" alt="Screen Shot 2022-10-31 at 7 00 51 PM" src="https://user-images.githubusercontent.com/52360459/199125744-a355952e-f923-4885-bb43-7dcd4da55cfc.png">


## Connecting to the Database

The file ```database_resource.py``` in the directory ```./src``` is a simple, starter REST resource.
This database resource python file contains connectivity details, database name, and the sql command to be executed to retrieve information based on Itinerary Id

For this service, we have 2 Tables:
-Itinerary: primary is itinerary id, contains limited attributes
-Travel: primary key is travel id, contains majority of the attribute data and has itinerary id as a foreign key. 

You can find the queries we wrote in commands.sql file to run in DataGrip 
