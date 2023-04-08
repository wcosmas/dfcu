# DFCU Loans validation system

This README file provides instructions for setting up and run the system. These instructions assume that you have basic knowledge of Python and the command line.

## Prerequisites

Before you can set up and run your Python Django app, you will need the following:

- Python 3 installed on your machine
- pip package manager installed on your machine
- A code editor of your choice (e.g. Visual Studio Code, PyCharm, etc.)
- Basic knowledge of using the command line

## Setting up project

Open your terminal and navigate to the directory where you want to create your virtual environment.
Run the following command to create a virtual environment:

```
python3 -m venv myenv
```

Replace `myenv` with the name you want to give your virtual environment.

Activate your virtual environment by running the following command for Mac OS:

```
source myenv/bin/activate
```

For windows

```
 myenv/Scripts/activate
```

Install packages by running the command below:

```
 pip install requirements.txt
```

Migrate the database by running the command below:

```
 python manage.py migrate
```

I'm using an sqlite3 db so no extra database configurations required. When you run the migration command an sqlite3 db intance will be created in thre root directory of the project.

To seed the database run the command below:

```
 python manage.py seed_data
```

This will create two customers

1. Wamozo Cosmas with account number 3459871348
2. Muhumuza Joshua with account number 2348765156

The account for Wamozo Cosmas will be seeded with 3 loans and that of Muhumuza Joshua will not be seeded with any loans. This will help in testing the main usecases of our `api`

To run the development server, run the command below:

```
python manage.py runserver
```

You should see output similar to the following:

Starting development server at <http://127.0.0.1:8000/>

Quit the server with CONTROL-C.

Open your web browser and go to <http://127.0.0.1:8000/dashboard>. You should see the dahsboard
![dashboard](https://user-images.githubusercontent.com/37125096/230707376-ffd7281a-2903-443f-b9cd-4788251cb2b1.jpg)

## Test API
To use the api you need an api client tool like postman, insomia or you can use curl and make a post request to the url <http://127.0.0.1:8000/loans> and pass the user account_number in the request body as a JSON object. We already seeded the database so their should be dummy data for testing. Use the customer wamozo cosmas with account number 3459871348:
![valid_account_number](https://user-images.githubusercontent.com/37125096/230707490-f5699254-2a71-4a70-a237-f82f69276428.jpg)

To test the scenario for auser with no loans available use the account for muhumuza joshua with account number 2348765156:
![no_loan_found](https://user-images.githubusercontent.com/37125096/230707596-15b3af05-957d-4c02-b4a3-fc5baca294f2.jpg)

If you provide an invalid account number(with characters less than or greater than 10). You will get the response below:
![inavlid_number](https://user-images.githubusercontent.com/37125096/230707789-fc450214-a9d8-4d41-83e8-b32123f68e8c.jpg)

Incase you provide a null account number(client didn't provide account number), the response below will be sent back:
![empty_number](https://user-images.githubusercontent.com/37125096/230707896-25baee82-87f2-4bf6-a359-f66312e00bce.jpg)

## Simulate Requests
Use your api client(postman,insomia or curl) to make a get request to  url  <http://127.0.0.1:8000/simulate_request/>. Dummy account numbers already exist in the account_numbers.json file. You can add as many as you want. 
![simulate](https://user-images.githubusercontent.com/37125096/230741218-57e145a0-bbaa-4775-b43e-f8c7cca664e4.jpg)

The responses of the simulated requests will be saved in the results.txt file in the project root directory. You don't have to create the file. It will be created automatically if it doesn't exist
![results txt](https://user-images.githubusercontent.com/37125096/230741258-2a95d5cb-1afd-4aee-b43f-6c4de6c3fafb.jpg)

