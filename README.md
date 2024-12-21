# Flask Coins API

A Flask-based web application to fetch cryptocurrency market updates from the CoinGecko API.

---

## **Getting Started**

Follow these instructions to set up and run the project on your local machine.

---

### **Prerequisites**

- **Python**: Make sure Python 3.11+ is installed on your system.
- **pip**: Installed with Python for package management.
- **Docker**: Required to build and run the Docker container (if using Docker).

---

### Local Development

Clone the repository to your local machine:

```bash
git clone https://github.com/your-repo-name/flask-project.git
cd flask-project
```

Create and activate the virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file with following parameters

```bash
FLASK_APP=app.py
FLASK_ENV=development
```

Running the app

```bash
flask run
```

Running unit tests with coverage

```bash
python -m pytest --cov=app tests/
```

---

### Docker guide

Build image

```bash
docker build -t flask-app .
```

Run Container

```bash
docker run -p 5000:5000 flask-app
```
