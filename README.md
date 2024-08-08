# SRE BOOTCAMP EXCERCISES
## Student Management API

This project is a Django-based API for managing student information. It allows for creating, retrieving, updating, and deleting student records, along with pagination support for listing students. The project is currently in its development phase, and additional features and a DevOps process will be integrated as the project progresses.

### Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
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

### Project Structure

```.
├── app/
│ ├── init.py
│ ├── admin.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ └── pagination.py
├── project_name/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt

```

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)
- Git

### Local Development Setup



1. **Clone the repository**

```
   git clone https://github.com/your-username/student-management-api.git
   cd student-management-api
```

2. **Create a virtual environment**
```
python -m venv env

```
Activate the virtual environment
On Windows:

```
.\env\Scripts\activate
```

On macOS/Linux:

```
source env/bin/activate

```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Apply database migrations**

```
python manage.py migrate
```

5. **Run the development server**

```
python manage.py runserver
```

### Access the API

Open your web browser and navigate to http://127.0.0.1:8000/.



### Usage

Running the API
With the development server running, you can interact with the API using tools like curl, Postman, or directly through your web browser.

### API Endpoints

```
GET /students/: Retrieve a paginated list of students.
POST /students/: Create a new student record.
GET /students/{id}/: Retrieve a specific student's details.
PUT /students/{id}/: Update a student's details.
DELETE /students/{id}/: Delete a student record.
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





