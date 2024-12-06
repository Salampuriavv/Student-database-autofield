 


## Student Management System with Dockerized Setup

This project provides APIs for managing student details and their associated phone numbers using Django and a PostgreSQL database. The setup uses Docker for easy deployment and testing.



## Features
- **Students Table**: Manage student details like roll number and name.
- **StudentsPNo Table**: Manage phone numbers associated with students.



## Prerequisites
1. Install Docker and Docker Compose on your system.
2. Clone this repository:
   ```bash
   git clone 
   cd 
   ```



## Running the Application

### 1. Start the Docker Containers
Run the following command to build and start the containers:
```bash
docker-compose up --build
```

This will:
- Start the Django application.
- Start a PostgreSQL database container.

### 2. Apply Database Migrations
Once the containers are running, open a terminal in the Django container and run:
```bash
docker exec -it postgres-infra bash
python manage.py migrate
```

### 3. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```

### 4. Access the Application
- **API Base URL**: `http://127.0.0.1:8080/`
- **Django Admin**: `http://127.0.0.1:8080/admin/`

---

## Instructions to Test APIs on Postman

### Students Table

#### **GET All Students**
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8080/students/`

#### **GET Single Student**
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8080/students/1/`

#### **POST (Create a Student)**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8080/students/`
- **Body (JSON)**:
  ```json
  {
    "roll_no": "1234",
    "name": "John Doe"
  }
  ```

#### **PUT (Update Entire Student)**
- **Method**: `PUT`
- **URL**: `http://127.0.0.1:8080/students/1/`
- **Body (JSON)**:
  ```json
  {
    "roll_no": "5678",
    "name": "John Smith"
  }
  ```

#### **PATCH (Partial Update)**
- **Method**: `PATCH`
- **URL**: `http://127.0.0.1:8080/students/1/`
- **Body (JSON)**:
  ```json
  {
    "name": "John Updated"
  }
  ```

#### **DELETE (Delete a Student)**
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:8080/students/1/`

---

### StudentsPNo Table

#### **GET All Phone Numbers**
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8080/students_pno/`

#### **GET Phone Numbers by Student ID**
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8080/students_pno/?id=1`

#### **POST (Create a Phone Number)**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8080/students_pno/`
- **Body (JSON)**:
  ```json
  {
    "id": 1,
    "pno": "9876543210"
  }
  ```

#### **PUT (Update Entire Phone Number)**
- **Method**: `PUT`
- **URL**: `http://127.0.0.1:8080/students_pno/`
- **Body (JSON)**:
  ```json
  {
    "pno_id": 2,
    "pno": "1122334455"
  }
  ```

#### **PATCH (Partial Update)**
- **Method**: `PATCH`
- **URL**: `http://127.0.0.1:8080/students_pno/`
- **Body (JSON)**:
  ```json
  {
    "pno_id": 2,
    "pno": "5566778899"
  }
  ```

#### **DELETE (Delete a Phone Number)**
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:8080/students_pno/`
- **Body (JSON)**:
  ```json
  {
    "pno_id": 2
  }
  ```

---

## Database Details

### **Students Table**
| Field Name | Data Type | Description               |
|------------|-----------|---------------------------|
| id         | Integer   | Primary key (auto-generated) |
| roll_no    | String    | Roll number of the student |
| name       | String    | Name of the student        |

### **StudentsPNo Table**
| Field Name | Data Type | Description               |
|------------|-----------|---------------------------|
| id         | Integer   | Primary key (auto-generated) |
| student_id | Integer   | Foreign key referencing `Students.id` |
| pno        | String    | Phone number of the student |

