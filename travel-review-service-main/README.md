# Review-Microservice

## Introduction

This is a simple Flask based Travel Itinerary microservice that is deployed in ElasticBeanstalk.


## Setup

Please make sure that your system has already installed:
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

```pip install -r requirements.txt```

Beofre you run the application, just make sure you have set the following environment variables properly:
```
DBUSER
```
```
DBPW
```
```
DBHOST
```

```python application.py``` or from pycharm use the ```Run Application``` option


Select the file ```application.py``` in the directory ```./`` in the file explorer. Right click on the file and
select "run." In the execution panel at the bottom of the screen, you should see messages about "running on ... ..."
This indicates that the web application has started.


## How to interact with service

The Review service lets you create, delete, search and update reviews posted by users.

Once the application is running following the steps described above the serivce exposes certain API endpints which you can use to do the following actions:

### 1. Create Review
Method: ```POST```

Example Body:
```
{
	"review": "Best place I have ever visited :)", 
	"rating": "4", 
	"user_id": 10002, 
	"city": "cairo"
}
```

Using python requests:
```
import requests

url = "http://127.0.0.1:5000/api/review"

payload = "{\n\t\"review\": \"Worst place I have ever visited :(\", \n\t\"rating\": \"2\", \n\t\"user_id\": 10002, \n\t\"city\": \"cairo\"\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```


### 2. Delete Review
Method: ```DELETE```

Example Body:
```
{
	"user_id": 10001, 
	"city": "chicago"
}
```

Using python requests:
```
import requests

url = "http://127.0.0.1:5000/api/review"

payload = "{\n\t\"user_id\": 10001, \n\t\"city\": \"chicago\"\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, data=payload, headers=headers)

print(response.text)
```

### 3. Update Review
Method ```PUT```

Example Body:
```
{ 
  "city": "dubai", 
  "review": "nice place for shopping!!!!", 
  "rating": "4", 
  "user_id": 12345
}
```

Using python requests

```
import requests

url = "http://127.0.0.1:5000/api/review"

payload = "{\"city\": \"dubai\", \"review\": \"nice place for shopping!!!!\", \"rating\": \"4\", \"user_id\": 12345}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
```

### 4. Search Review

Method: ```GET```

#### Using python requests 

##### i. (review by a user)

```
import requests

url = "http://127.0.0.1:5000/api/review"

querystring = {"user_id":"10001"}

payload = "{\"city\": \"dubai\", \"review\": \"great place for shopping!!!!\", \"rating\": \"4\", \"user_id\": 12345}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
```


##### ii. (review by city)

```import requests

url = "http://127.0.0.1:5000/api/review"

querystring = {"city":"sydney"}

payload = "{\"city\": \"dubai\", \"review\": \"great place for shopping!!!!\", \"rating\": \"4\", \"user_id\": 12345}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
```


Note: You can also combine both ```user_id``` and ```city``` in query. For instance when looking for a review by a user for a specific city. 
## Deploy to Elasticbeanstalk

In order to deploy to elasticbeanstalk seamlessly, use the following tool

```eb```

For all the stepss below make sure you are in the root directory of you repository.

### Step 1

Install ebcli using the following link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html
Configure your machine ot use ebcli using the following link: 

The folder ```.elasticbeanstalk``` contains the necessary deployment configuration to deploy to Elasticbeanstalk


### Step 2
Initialize your flask web application in Elastic beanstalk using the following command:

```eb init -p python-3.8 <APPLICATION_NAME> --region <REGION>```

Once this step is completed, you can confirm by going to Elasticbeanstalk console in the region that you chose above 
and making sure the Application that you created just now is there.

### Step 3
Create an environment of your application using the following:
```eb create <APPLICATION_ENV>```
 Again confirm the application environment is created by going to the console.

### Step 4

To open the application in a browser, use the following:

```eb open```

### Step 5
If you are actively making changes ad want to redeploy a new version of your application, sue the following:

```eb deploy```

### Step 6
To terminate all the resources that you created, do the following 

```eb terminate <APPLICATION_ENV>```


