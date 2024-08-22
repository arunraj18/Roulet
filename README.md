Roulet
Roulet is a simple full-stack web application built using Django for the backend (API) and React for the frontend (UI). This project demonstrates a basic 3-tier architecture deployed on a local development environment.

roulet/
├── backend/ # Django backend
│ ├── manage.py
│ ├── backend/ # Django project settings
│ ├── api/ # API app
│ ├── venv/ # Python virtual environment
│ └── requirements.txt # Python dependencies
└── frontend/ # React frontend
 ├── public/
 ├── src/
 ├── package.json
 └── node_modules/
Features
Django REST API: Provides backend API for managing and serving data.
React Frontend: User interface built with React.js.
CORS Handling: Django CORS headers configured to allow cross-origin requests from the React frontend.

Requirements
Python (>= 3.6)
Node.js (>= 12.x)
npm (comes with Node.js)
pip (Python package installer)
Django (>= 3.2)
Django REST Framework (>= 3.12)
django-cors-headers (>= 3.7)


Installation
1. Clone the Repository
git clone https://github.com/your-username/roulet.git
cd roulet

3. Backend Setup
Navigate to the backend directory:
cd backend

Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install the required Python packages:
pip install -r requirements.txt
Apply the migrations:
python manage.py migrate

3. Frontend Setup
Navigate to the frontend directory:
cd ../frontend

Install the required npm packages:
npm install

Running the Application
1. Start the Backend Server
Navigate to the backend directory and run the Django development server:
cd backend
python manage.py runserver
The backend API will be running at http://127.0.0.1:8000
<img width="605" alt="Screenshot 2024-08-22 at 4 30 29 PM" src="https://github.com/user-attachments/assets/3c06594f-ecfc-4418-af72-53967071bfc3">


2. Start the Frontend Development Server
In a new terminal, navigate to the frontend directory and start the React development server:
cd frontend
npm start
The frontend UI will be available at http://localhost:3000.
<img width="662" alt="Screenshot 2024-08-22 at 4 30 42 PM" src="https://github.com/user-attachments/assets/fafc44b2-d85d-4586-91e4-397b0aa14214">

API Endpoints
GET /api/data/: Fetch a message from the Django backend.
GET /api/user/: Fetch user information from the Django backend.
