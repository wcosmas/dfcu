# Setting up the DFCU Loans validation system

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
