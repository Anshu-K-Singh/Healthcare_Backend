# Healthcare Backend System

## Overview
This project is a backend system for a healthcare application built using Django, Django REST Framework (DRF), and PostgreSQL. It provides APIs for user authentication, patient management, doctor management, and patient-doctor mappings.

---

## Features
- User registration and login with JWT authentication.
- CRUD operations for managing patients and doctors.
- Assigning doctors to patients and retrieving mappings.
- Secure and scalable backend with PostgreSQL as the database.

---

## Technologies Used
- **Backend Framework**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT using `djangorestframework-simplejwt`
- **Environment Management**: Environment variables for sensitive data
- **Error Handling**: Proper error responses and input validations
- **Security**: Restricted access to authenticated users

---

## API Endpoints

### 1. Authentication APIs

#### Register a New User
- **Endpoint**: `POST /api/auth/register/`
- **Payload**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "refresh": "<refresh_token>",
    "access": "<access_token>"
  }
  ```

#### Login
- **Endpoint**: `POST /api/auth/login/`
- **Payload**:
  ```json
  {
    "username": "john_doe",
    "password": "securepassword123"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "refresh": "<refresh_token>",
    "access": "<access_token>"
  }
  ```

---

### 2. Patient Management APIs

#### Add a New Patient
- **Endpoint**: `POST /api/patients/`
- **Payload**:
  ```json
  {
    "name": "Jane Doe",
    "age": 30,
    "address": "123 Main Street"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "name": "Jane Doe",
    "age": 30,
    "address": "123 Main Street"
  }
  ```

#### Retrieve All Patients
- **Endpoint**: `GET /api/patients/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "name": "Jane Doe",
      "age": 30,
      "address": "123 Main Street"
    }
  ]
  ```

#### Retrieve a Specific Patient
- **Endpoint**: `GET /api/patients/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Jane Doe",
    "age": 30,
    "address": "123 Main Street"
  }
  ```

#### Update a Patient
- **Endpoint**: `PUT /api/patients/<id>/`
- **Payload**:
  ```json
  {
    "name": "Jane Doe Updated",
    "age": 31,
    "address": "456 Elm Street"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Jane Doe Updated",
    "age": 31,
    "address": "456 Elm Street"
  }
  ```

#### Delete a Patient
- **Endpoint**: `DELETE /api/patients/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (204 No Content):
  No response body.

---

### 3. Doctor Management APIs

#### Add a New Doctor
- **Endpoint**: `POST /api/doctors/`
- **Payload**:
  ```json
  {
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "contact_info": "dr.smith@example.com"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "contact_info": "dr.smith@example.com"
  }
  ```

#### Retrieve All Doctors
- **Endpoint**: `GET /api/doctors/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "name": "Dr. Smith",
      "specialization": "Cardiology",
      "contact_info": "dr.smith@example.com"
    }
  ]
  ```

#### Retrieve a Specific Doctor
- **Endpoint**: `GET /api/doctors/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "contact_info": "dr.smith@example.com"
  }
  ```

#### Update a Doctor
- **Endpoint**: `PUT /api/doctors/<id>/`
- **Payload**:
  ```json
  {
    "name": "Dr. John Smith",
    "specialization": "Neurology",
    "contact_info": "dr.johnsmith@example.com"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Dr. John Smith",
    "specialization": "Neurology",
    "contact_info": "dr.johnsmith@example.com"
  }
  ```

#### Delete a Doctor
- **Endpoint**: `DELETE /api/doctors/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (204 No Content):
  No response body.

---

### 4. Patient-Doctor Mapping APIs

#### Assign a Doctor to a Patient
- **Endpoint**: `POST /api/mappings/`
- **Payload**:
  ```json
  {
    "patient": 1,
    "doctor": 1
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "patient": 1,
    "doctor": 1
  }
  ```

#### Retrieve All Mappings
- **Endpoint**: `GET /api/mappings/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "patient": 1,
      "doctor": 1
    }
  ]
  ```

#### Retrieve Mappings for a Specific Patient
- **Endpoint**: `GET /api/mappings/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "patient": 1,
    "doctor": 1
  }
  ```

#### Remove a Doctor from a Patient
- **Endpoint**: `DELETE /api/mappings/<id>/`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response** (204 No Content):
  No response body.

---

## Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
```

---

## Running the Project

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

4. **Test the APIs**:
   Use Postman or `curl` to test the endpoints.

---

## License
This project is licensed under the MIT License.