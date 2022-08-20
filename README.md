# AssurityTest
**Technical Assignment**
Using the API given below create an automated test with the listed acceptance criteria:

 

API = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false

 

Acceptance Criteria:

Name = "Carbon credits"
CanRelist = true
The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
Instructions:

Your test needs to be written using a programming language of your choice (not a tool like SoapUI). Ensure you include a clear ReadMe
Submit your test to us in a format that lets us execute and review the code (it must be submitted in a public repository like Bitbucket or Github)
Your test must validate all the three acceptance criteria
Points will be awarded for meeting the criteria, style and the use of good practices and appropriate use of source control
We want to see your best work - no lazy coding or comments.
We would appreciate it if you could please return your submission within one week of this email.


## **Getting started**
Follow the setup procedure to get the Python end-to-end testing framework up and running. Estimated time 5min.

**Description**
-------------
This is a simple python application intended to validate parameters from the given API to fulfill the given acceptance criteria.
The main task is to validate API parameters such as Name, CanRelist and Promotions element (Name and Description parameters )from the API.

## **Prerequisites**

Python is an open-source programming language that supports these operating systems:

Linux,
Windows 7,8,10,11 and newer for Python 3.7, Windows XP and newer for Python 3.10,
macOS Snow Leopard (macOS 10.6, 2008) and newer

**Installation**
----------------
To use the python code. Follow the steps given below:

1. Install PyCharm community edition 2022.2.1 from https://www.jetbrains.com/pycharm/download/#section=windows
2. Install Python version 3.10 from https://www.python.org/downloads/release/python-3100/
3. Import Requests package from the Python Packages inside Pycharm. Write the name of the package in python packages and click install package.
4. Import json package from the Python Packages inside Pycharm. Write the name of the package in the python packages and click install package.

## Running the test
------------------
1. Open the Pycharm application
2. In the main.py import the packages Requests and json 
3. Fetch the response of the api, and validate the response of the API is OK or 200.
4. Save the API response in the python object
5. Fetch the parameters from the API include Name, CanRelist as per the acceptance criteria and validate them.
6. For Promotions element, fetch the Name and description for the acceptance criteria using the for loop and iterate over the list.

**Development**
-----------

1. The development required understanding of python packages required for the API requests and response.
2. The development was done using python 3.10 version and Pycharm community edition.
3. The packages were download from the Pycharm Install package.
4. The basic commands of API requests and response were used for validation.
5. Once the status of the API was confirmed to be 200, the Json object was then manipulated using if else and for loop conditions.
6. The print statements were used to present the validated acceptance criteria values. 


**Testing**
-------

1. To fulfill the acceptance criteria, validated the Name and CanRelist parameter of the API was validated using the if else condition.
2. To fulfill the acceptance criteria, validated the promotions parameter's Name and Description of the API was validated using the for loop and iteration over list.




