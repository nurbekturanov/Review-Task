### Review-Task

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/nurbekturanov/Review-Task.git

```

--> Move into the directory where we have the project files : 
```bash
cd Review-Task

```

--> Create a virtual environment :
```bash
# We create our virtual environment
python -m venv venv

```

--> Activate the virtual environment :
```bash
.\venv\Scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

## Getting Started

To run this project you will need to set your environment variables.

1. Create a new file named `.env` inside the `core` folder
2. Copy all of the variables inside `core/.template.env` and assign your own values to them

### Create Super User

--> To create super user, we use :
```bash
python manage.py createsuperuser

```

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/api/

> ⚠ Or you can see swagger-ui apis at http://127.0.0.1:8000/api/schema/swagger-ui/

#
