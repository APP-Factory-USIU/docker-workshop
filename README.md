# Student Feedback Portal - Starter Project Specification

## Project Overview

This is a lightweight web application designed to collect anonymous feedback from students.

The project intentionally ships **without any Docker configuration**. During the Docker workshop, participants will containerize the application by creating the necessary Docker artifacts themselves.

---

### Features

* Submit anonymous feedback.
* View previously submitted feedback.
* Store feedback temporarily using Redis.
* Separate frontend and backend components.

---

### Repository Structure

```text
docker-workshop/
├── README.md
├── DOCKER_THEORY.md
├── DOCKER_PRACTICAL.md
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── backend/
    ├── app.py
    └── requirements.txt
```

---

### Running the Application Without Docker

First ensure you have these installed:

1. Python 3.12+
2. Redis package

#### Start Redis

```bash
redis-server
```

---

#### Start Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python main.py
```

---

## Start Frontend

Open the following file in your browser:

```text
frontend/index.html
```

Optionally, you can use `python.server`:

```bash
python -m https.server 8080
```

---

## Expected Behaviour

Students should be able to:

1. Open the feedback portal.
2. Submit feedback.
3. See the feedback appear immediately.
4. Refresh the page and observe that Redis preserves the data while it is running.

---

## What Is Missing?

The repository intentionally does NOT include:

```text
Dockerfile
docker-compose.yml
.dockerignore
```

These components will be developed during the Docker workshop.

---

## Docker Workshop Goals

By the end of the Docker session, participants should have created:

Backend:

✓ Dockerfile

Frontend:

✓ Dockerfile

Project Root:

✓ docker-compose.yml

✓ .dockerignore

✓ Multi-container application running successfully

---

## Future Extension (CI/CD Session)

This same repository can later be used to demonstrate:

* Automated Docker builds
* GitHub Actions workflows
* Container testing
* Deployment pipelines
