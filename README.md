# SRE BOOTCAMP EXCERCISES
## Student Management API

This project is a Django-based API for managing student information. It allows for creating, retrieving, updating, and deleting student records, along with pagination support for listing students. The project is currently in its development phase, and additional features and a DevOps process will be integrated as the project progresses.

### Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Local Development Setup](#local-development-setup)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

### Features

- Create, retrieve, update, and delete student records.
- Pagination support for listing students.
- RESTful API built using Django Rest Framework.



## Setup Instructions

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)
- Git
- docker

### Local Development Setup



1. **Clone the repository**

```
   git clone https://github.com/blackxavier/SRE-bootcamp-exercises.git
   cd SRE-bootcamp-exercises
```

2. **Run compose file**

```
docker compose  up
```


### Access the API

Open your web browser and navigate to http://127.0.0.1:8000/. This opens up a swagger endpoint to interface with the API



### Usage

Running the API
Using the swagger endpoint, you can interact with the API.

### API Endpoints

```
GET api/v1/students/: Retrieve a paginated list of students.
POST api/v1/students/: Create a new student record.
GET api/v1/students/{id}/: Retrieve a specific student's details.
PUT api/v1/students/{id}/: Update a student's details.
DELETE api/v1/students/{id}/: Delete a student record.
GET api/v1/healthcheck/ : Retrieves health information of API
```

### Testing
To run tests, use the following command:

```
python manage.py test
```

This will run the tests defined in tests.py, ensuring that the API functions as expected.

### Future Work
This project is in its early stages and not yet in a final state. Upcoming developments include:

Implementing full CI/CD pipelines and other DevOps practices.
Enhancing the API with additional features such as authentication, validation, and more.
Adding comprehensive documentation and improved error handling.
Contributing
Contributions are welcome! Please open an issue or submit a pull request with any changes or improvements you'd like to see.

### License
This project is licensed under the MIT License. See the LICENSE file for details.





