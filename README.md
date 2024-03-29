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

> ⚠ You need to login before sending requests to the api endpoints.

#

### Api Preview :

**Swagger UI**
![Screenshot (5)](https://github.com/nurbekturanov/Review-Task/assets/133900078/024fb099-9488-4305-934e-e8c4946911a9)

**Reviews List**
![Screenshot (6)](https://github.com/nurbekturanov/Review-Task/assets/133900078/69ca545f-2275-4fcc-9921-a7f684f71012)

#

### Acknowledgements
I've completed the core functionality of the project, including models for users, reviews, replies and likes, along with API endpoints for fetching review lists and creating reviews.
#
I noticed the project specification mentioned using Docker and Docker Compose for containerization. While I wasn't able to implement it in this specific project due to time constraints, I understand the value of containerized deployments.
- Docker helps create standardized and portable environments for applications across different machines, simplifying deployment and maintenance.
- It promotes a more modular and independent development process.

I'm eager to learn more about implementing Docker for this project in the future. I can explore online resources or tutorials to get up to speed if needed.
#
I see that the project also requires the use of Celery for handling background tasks. I didn't have the opportunity to implement it this time.
- Celery is a task queue that allows for asynchronous processing of high-volume or time-consuming tasks.
- By using Celery, the API wouldn't be blocked by lengthy operations, improving responsiveness.

I'm interested in learning how Celery can be integrated into this project to enhance its scalability. I'd be happy to pick it up if I get the opportunity.
