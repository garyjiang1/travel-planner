# User-Microservice

## Setup

- Make sure that your system has already installed:
  - Python (3.9 or greater)
  - MySQL Community Server

In the root of the directory, please execute the command before running the application
```pip install -r requirements.txt```

This should install the necessary Python requirements.

## Recommended software to run the program
The environment variables are used for database connection. 
Please reset the environment variable in Pycharm with the expected system username and password for the database setup.

## Notification
Use ```sqlschema.sql``` to init database before running ```application.py```.

Before running please make sure the following environment variables are set:
```shell
#if you are using pycharm, set the environment variables by:
# run -> edit configurations -> environment variables
DBUSER -> "YOURUSER"
DBPW -> "YOURPW"
DBHOST -> "YOURHOST"
WEB_APP_URL -> xxx
ITINERARY_URL -> xxx
GOOGLE_CLIENT_ID -> 36581782153-sjcmg04bt2p39g7kcsmse4qralrfeb6j.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET -> 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

Alternatively, you can manually exporting them
export DBUSER=xxx
export DBHOST=xxx
export DBPW=xxx
export WEB_APP_URL= xxx
export ITINERARY_URL= xxx
export GOOGLE_CLIENT_ID=36581782153-sjcmg04bt2p39g7kcsmse4qralrfeb6j.apps.googleusercontent.com
export GOOGLE_CLIENT_SECRET=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

```

**Please keep in mind that these variables has to bechanged when deploying to cloud**

## Executing the Program

Select the file ```application.py``` in the directory ```./src``` in the file explorer. Right click on the file and
select "run." In the execution panel at the bottom of the screen, you should see messages about "running on ... ..."
This indicates that the web application has started.

## Connecting to the Database

The file ```user_service_resource.py``` is a simple, starter REST resource.

## Expected Output Rendered from Postman

/users_service/login
```shell
Example output
{
    "success": true,
    "message": "login successful",
    "user_id": 12345
}
```

/users_service/user/reset_password
```shell
Example input:
{
  "email": "editxxx@columbia.edu",
  "old_password": "testpassword",
  "new_password": "testnewpassword"
}
Example output:
{
    "success": true,
    "message": "changing successful"
}
```
/users_service/create_new_user
```shell
Example input:
{
    "email": "xxx@columbia.edu",
	"username": "testname",
	"password": "testpassword",
    "user_first_name": "testfirstname",
    "user_last_name": "testlasttname"
}
Example output:
{
    "success": true,
    "message": "Register successfully, continue to log in"
}
```

/users_service/show_user/<user_id>
```shell
Example output
{
    "user_id": 12345,
    "user_first_name": "Gary",
    "user_last_name": "Jiang",
    "email": "xxx@columbia.edu"
}
```

users_service/user/edit/<user_id>
```shell
Example input
{
    "user_first_name": "edittestfirstname",
    "user_last_name": "edittestlasttname",
    "email": "editxxx@columbia.edu"
}

Example output
{
  "success": true,
  "message": "You have successfully edited the profile"
}
```
/users_service/create_new_user
```shell
Example input
{
    "email": "newemail@columbia.edu",
    "username": "newusername",
    "password": "newpassword",
    "user_first_name": "newfirstname",
    "user_last_name":"newlastname"
}

Example output
{
  "success": true,
  "message": "Register successfully, continue to log in"
}
```

/users_service/delete_user/<user_id>
```shell
Example output
{
    "success": true,
    "message": "You have deleted the user"
}
```

/users_service/create_new_trip/<user_id>
```shell
Example input
{
    "destination": "New York",
    "origin": "LA",
    "num_people": 1,
    "budget": 10030.0
}
Example output
{
    "success": true,
    "message": "Added new trip"
}
```

/users_service/show_trips/<trip_id>
```shell
Example output
{
  "trip_id": 1,
  "user_id": 12345,
  "destination": "New York",
  "origin": "London",
  "num_people": 12,
  "budget": 1000.0
}
```

/users_service/edit_trips/<trip_id>
```shell
Example input
{
    "destination": "China",
    "origin": "Shanghai",
    "num_people": "2",
    "budget": "100"
}

Example output
{
    "success": true,
    "message": "Updated trip successfully"
}

```

/users_service/delete_trip/<trip_id>
```shell
Example output
{
    "success": true,
    "message": "You have deleted the trip"
}
```
/users_service/create_new_itinerary
```shell
Example input
{
    "trip_id": "2",
    "total_cost": "1000"
}

Example output
{
    "success": true,
    "message": "New itinerary registered successfully"
}

```

/users_service/edit_itinerary/<itinerary_id>
```shell
Example input
{
    "total_cost": "250"
}
Example output
{
    "success": true,
    "message": "Updated itinerary successfully"
}
```

/users_service/delete_itinerary/<itinerary_id>
```shell
Example output
{
    "success": true,
    "message": "You have deleted the itinerary"
}
```

/users_service/get_itinerary/<itinerary_id>
```shell
Example output
{
    "success": true,
    "data": 1
}
```
