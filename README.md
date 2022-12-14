**Technical Assignment**

Using the API given below create an automated test with the listed acceptance criteria:

 

`API = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false`

 

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

Jump to:

- [Getting Started](#getting-started)
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Test](#running-the-test)
- [Development](#development)
- [Testing](#testing)

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

    Packages:

    `import requests`

    `import json`

2. The development was done using python 3.10 version and Pycharm community edition.
3. The packages were download from the Pycharm Install package.
4. The first task is to get the api given in the test and then save its response in the response object.

     `response = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false")`

Another task is to check if the api is responding correctly which means the response code fetched from the API is OK or 200 which can be achived using the response.ok mehtod and then saving the response in a python variable.

    `response_status = response.ok
     print("API response status", ";", response_status)`

5. Once the status of the API was confirmed to be 200, the Json object was then converted into the python dictionary by suing below command

     `dict_values = response.json()`

6.The dictonary values can then be manipulated using the below code:

     `Name = dict_values['Name']
      if Name == 'Carbon credits':
         print("Name", ":", Name)
      else:
         False`

7. The code above takes the dictionary key Name and stores its value in the Name variable. If the Name is Carbon credits then the IF condition passes otherwise False.
8. The similar approach is followed for validating the CanReList parameter of the API.

     `Can_relist = dict_values['CanRelist']
      if Can_relist:
         print("CanRelist", ":", Can_relist)
      else:
         False`
    
9. Once the Name and CanReList values are validated. Then fetch the Promotions element using the below code. The type for the Promotions element is a list type.
The best way to fetch values from a list is to use the FOR loop.

       `print(type(prom_data))`

Fetching name and description from promotions element

      `for i in prom_data:
         if i['Name'] == 'Gallery' and i['Description'] == 'Good position in category':
            print("Name = ", i['Name'], ",", "Description", i['Description'])`
        
10. The print statements above were used to present the required acceptance criteria values. 


**Testing**
-------

1. To fulfill the acceptance criteria, validated the Name and CanRelist parameter of the API was validated using the if else condition.
Validate Name:

        `if Name == 'Carbon credits':
             print("Name", ":", Name)
         else:
             False`
    
Validate CanReList:

        `if Can_relist:
            print("CanRelist", ":", Can_relist)
         else:
            False`
    
2. To fulfill the acceptance criteria, validated the promotions parameter's Name and Description of the API was validated using the for loop and iteration over list.
    
         `if i['Name'] == 'Gallery' and i['Description'] == 'Good position in category':`

Author
Harsha Arora


