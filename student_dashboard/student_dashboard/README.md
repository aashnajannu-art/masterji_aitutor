# Student Dashboard Project

This project is a Django-based web application designed to provide a dashboard interface for students. The dashboard includes an XP bar at the top, an assignments bar on the left, and a Python workspace on the right.

## Project Structure

```
student_dashboard
├── student_dashboard
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── dashboard
│   ├── migrations
│   │   └── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── templates
│   │   └── dashboard
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd student_dashboard
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

1. Apply migrations:
   ```
   python manage.py migrate
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Open your web browser and go to `http://127.0.0.1:8000/` to view the dashboard.

## Features

- XP Bar: Displays the user's experience points at the top of the dashboard.
- Assignments Bar: Lists assignments on the left side for easy access.
- Python Workspace: Provides an interactive area for Python coding.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.