
# Docker Practical Guide

## Containerizing the Student Feedback Portal

---

# Introduction

Welcome to the practical portion of the Docker workshop.

You have been provided with a working application consisting of:

* A frontend
* A backend
* Redis-based data storage

Your goal is to transform this application into a **multi-container application** using Docker.

By the end of this exercise, you should have created:

```text
backend/Dockerfile
frontend/Dockerfile
backend/.dockerignore
docker-compose.yml
```

---

# Learning Objectives

By the end of this practical, you should be able to:

* Build Docker images.
* Run Docker containers.
* Pull official images from Docker Hub.
* Create Dockerfiles.
* Use Docker Compose.
* Launch an entire application stack using a single command.

---

# Repository Structure

You should have the following repository structure:

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

# Part 1 – Explore the Application

Before using Docker, understand the project.

## Questions

1. Which directory contains the frontend?
2. Which directory contains the backend?
3. Which technology powers the backend?
4. Which service stores the feedback data?

---

# Part 2 – Create the Backend Dockerfile

Navigate to the backend directory.

Create a file named:

```text
backend/Dockerfile
```

---

## Complete the Dockerfile

Replace the placeholders below.

```dockerfile
FROM ____________________

WORKDIR ____________________

COPY ____________________

RUN ____________________

COPY ____________________

CMD ____________________
```

---

## Hints

* Which official image provides Python?
* Where should the application live inside the container?
* Which file contains the dependencies?
* Which command installs dependencies?
* Which command starts the Flask application?

---

## Build the Backend Image

Run:

```bash
docker build -t feedback-backend ./backend
```

---

## Verify

Check that the image exists:

```bash
docker images
```

You should see:

```text
feedback-backend
```

---

# Part 3 – Run the Backend Container

The Flask application listens on port:

```text
5000
```

---

## Challenge

Run the backend container and expose the Flask application to your host machine.

---

## Verify

Visit:

```text
http://localhost:5000/health
```

If successful, you should receive a response indicating the service is healthy.

---

# Part 4 – Create the Frontend Dockerfile

Navigate to the frontend directory.

Create:

```text
frontend/Dockerfile
```

---

## Complete the Dockerfile

Replace the placeholders below.

```dockerfile
FROM ____________________

COPY ____________________
```

---

## Hints

* The frontend consists only of static files.
* Which official image is commonly used to serve static websites?
* Where should `index.html`, `script.js`, and `style.css` be copied?

---

## Build the Frontend Image

Run:

```bash
docker build -t feedback-frontend ./frontend
```

---

## Verify

Check that the image exists:

```bash
docker images
```

You should see:

```text
feedback-frontend
```

---

# Part 5 – Create a .dockerignore File

Docker sends files from the build context to the Docker daemon.

Some files should not be included.

Create:

```text
backend/.dockerignore
```

---

## Add Appropriate Entries

Decide which of the following should be ignored:

```text
__pycache__/
*.pyc
venv/
.git/
.pytest_cache/
```

---

## Reflection

Why is reducing the build context important?

---

# Part 6 – Pull the Redis Image

Redis is already available as an official Docker image.

Run:

```bash
docker pull redis
```

---

## Verify

Check downloaded images:

```bash
docker images
```

---

## Reflection

Why are official images useful?

---

# Part 7 – Create the Compose File

Managing multiple containers individually quickly becomes difficult.

Docker Compose allows us to describe the entire application stack.

Create:

```text
docker-compose.yml
```

---

# Complete the Compose File

Replace the placeholders below.

```yaml
services:

  frontend:
    build: ____________________

    ports:
      - "____________________"

  backend:
    build: ____________________

    ports:
      - "____________________"

    environment:
      REDIS_HOST: ____________________

  redis:
    image: ____________________
```

---

## Hints

### Frontend

* Which directory contains its Dockerfile?
* Which port should users access in their browser?
* Which port does Nginx expose?

---

### Backend

* Which directory contains its Dockerfile?
* Which port does Flask use?
* What hostname should the backend use to connect to Redis?

---

### Redis

* Do we need to build Redis ourselves?
* Which image should we use?

---

# Part 8 – Launch the Application Stack

Run:

```bash
docker compose up --build
```

---

## Verify Running Services

Check:

```bash
docker compose ps
```

You should see three services:

```text
frontend
backend
redis
```

---

# Part 9 – Test the Application

Open:

```text
http://localhost:8080
```

---

## Perform the Following Tests

### Test 1

Submit a piece of feedback.

Expected result:

```text
Feedback appears in the list.
```

---

### Test 2

Refresh the page.

Expected result:

```text
Feedback is still present.
```

---

### Test 3

View the application logs.

Run:

```bash
docker compose logs
```

---

### Test 4

View backend logs only.

Run:

```bash
docker compose logs backend
```

---

# Part 10 – Stop the Application

Shut down the application stack.

Run:

```bash
docker compose down
```

---

## Verify

Run:

```bash
docker ps
```

No workshop containers should still be running.

---

# Reflection Questions

Discuss the following with your group:

1. What problem does Docker solve?
2. What is the difference between an image and a container?
3. Why did we build some images but pull Redis from Docker Hub?
4. What advantages does Docker Compose provide?
5. How could this workflow fit into a CI/CD pipeline?

---

# Stretch Challenges

If you finish early, attempt one or more of the following:

## Challenge 1

Modify the frontend styling.

---

## Challenge 2

Add a volume to Redis so feedback persists even after containers are removed.

---

## Challenge 3

Configure automatic restarts for services.

---

## Challenge 4

Add another API endpoint to the backend.

---

## Challenge 5

Update the frontend to display the total number of feedback submissions.

---

# Workshop Wrap-Up

Congratulations!

You have successfully transformed a traditional application into a Dockerized, multi-container application.

You have:

* Built Docker images.
* Run containers.
* Used official images.
* Written Dockerfiles.
* Created a Docker Compose configuration.
* Launched an entire application stack.

In the next session, you will explore how these Docker workflows can be automated using CI/CD pipelines.
