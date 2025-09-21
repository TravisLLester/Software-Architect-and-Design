## Django Hello World Class Project - Week 5 Lab
A simple Django web application demonstrating basic routing with JSON and HTML responses.

# Setup
1.  Clone the repository:

```bash
git clone https://github.com/TravisLLester/django-hello-world.git
```

2.  Create virtual environment:

### Git Bash
  ```bash
  python -m venv .venv
  ```

### Activate virtual environment:
  ```
  source .venv/Scripts/activate
  ```


### Powershell
```
.venv\Scripts\Activate.ps1
```

### Mac/Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

# Install dependencies:

```
pip install -r requirements.txt
```

# Run the server:
```
python manage.py runserver
```

Available Routes
API Endpoint: http://127.0.0.1:8000/api/

Hello Page: http://127.0.0.1:8000/hello/

Personal Greeting: http://127.0.0.1:8000/hello/1/

About Page: http://127.0.0.1:8000/travis-lester/

# Requirements

Python 3.8+

Django 4.0+
