# Expense Tracker API

A Django REST Framework based API for tracking personal expenses across different categories. Users can create accounts, manage their expense categories, and track spending over time.

## Features

- User authentication with JWT tokens
- Category-wise expense tracking
- Date-based filtering of expenses
- Swagger/ReDoc API documentation
- User-specific data isolation
- Total expense calculation per entry

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Oyshik-ICT/SpendWise-API.git
cd SpendWise-API/
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/token/`: Obtain JWT token pair
  - Request body: `{"username": "your_username", "password": "your_password"}`
  - Returns: Access and refresh tokens

- `POST /api/token/refresh/`: Refresh JWT token
  - Request body: `{"refresh": "your_refresh_token"}`
  - Returns: New access token

### User Management
- `POST /users/`: Create new user account (public access)
  - Request body: `{"username": "user", "email": "user@example.com", "password": "pass"}`

- `GET /users/`: List users (admin only)
- `GET /users/{id}/`: Retrieve user details (owner or admin)
- `PUT /users/{id}/`: Update user (owner or admin)
- `DELETE /users/{id}/`: Delete user (owner or admin)

### Expense Categories
All expense endpoints require authentication:

- `GET /expenses/`: List user's expenses
- `POST /expenses/`: Create new expense entry
- `GET /expenses/{id}/`: Retrieve specific expense
- `PUT /expenses/{id}/`: Update specific expense
- `DELETE /expenses/{id}/`: Delete specific expense

#### Filtering Expenses
You can filter expenses by date using query parameters:
- `?created_at=YYYY-MM-DD`: Exact date
- `?created_at_gt=YYYY-MM-DD`: After date
- `?created_at_lt=YYYY-MM-DD`: Before date

## API Documentation

The API documentation is available through Swagger UI and ReDoc:

- Swagger UI: `/api/schema/swagger-ui/`
- ReDoc: `/api/schema/redoc/`
- Raw Schema: `/api/schema/`

To use Swagger UI:
1. Go to `/api/schema/swagger-ui/` in your browser
2. Click "Authorize" button
3. Enter your JWT token in the format: `Bearer <your_access_token>`
4. Try out the endpoints using the interactive documentation

## Example Expense Entry

```json
{
    "groceries": 150.50,
    "leisure": 75.00,
    "electronics": 200.00,
    "utilities": 100.00,
    "clothing": 50.00,
    "health": 25.00,
    "others": 30.00
}
```

## Security Notes

- JWT tokens are used for authentication
- Users can only access and modify their own data
- Passwords are properly hashed before storage
- Admin users have access to user management features
