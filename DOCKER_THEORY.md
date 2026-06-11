
# Docker Theory Notes

---

# Introduction

In this workshop, you will learn how Docker can be used to package applications and their dependencies into portable, reproducible environments called **containers**.

By the end of the Docker session, you will have transformed an existing application into a multi-container system consisting of:

* A frontend service
* A backend service
* A Redis service

---

# Why Docker?

One of the most common problems in software development is:

> "It works on my machine."

Different developers may have:

* Different operating systems
* Different software versions
* Missing dependencies
* Different configurations

Docker helps solve these problems by packaging applications together with everything they need to run.

---

# What is Docker?

Docker is a platform for developing, shipping, and running applications using **containers**.

Containers provide:

* Portability
* Isolation
* Consistency
* Faster deployment

---

# Containers vs Virtual Machines

## Virtual Machines

Virtual machines emulate an entire computer system.

```text
┌──────────────────────┐
│ Application          │
├──────────────────────┤
│ Dependencies         │
├──────────────────────┤
│ Guest Operating Sys. │
├──────────────────────┤
│ Hypervisor           │
├──────────────────────┤
│ Host Operating Sys.  │
└──────────────────────┘
```

Characteristics:

* Larger in size
* Slower startup times
* Higher resource usage

---

## Containers

Containers share the host operating system kernel.

```text
┌──────────────────────┐
│ Application          │
├──────────────────────┤
│ Dependencies         │
├──────────────────────┤
│ Docker Engine        │
├──────────────────────┤
│ Host Operating Sys.  │
└──────────────────────┘
```

Characteristics:

* Lightweight
* Fast startup times
* Efficient resource utilization

---

# Docker Images

An **image** is a read-only template used to create containers.

Think of an image as a blueprint.

Examples:

```text
python:3.12-slim
nginx:alpine
redis:latest
ubuntu:24.04
```

Images contain:

* Application code
* Dependencies
* Runtime environment
* Configuration

---

# Docker Containers

A **container** is a running instance of an image.

Analogy:

```text
Recipe   → Image

Meal     → Container
```

You can create multiple containers from the same image.

---

# Dockerfile

A Dockerfile is a text file containing instructions for building an image.

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

---

# Common Dockerfile Instructions

## FROM

Specifies the base image.

Example:

```dockerfile
FROM python:3.12-slim
```

---

## WORKDIR

Sets the working directory inside the container.

Example:

```dockerfile
WORKDIR /app
```

---

## COPY

Copies files from the host machine into the image.

Example:

```dockerfile
COPY requirements.txt .
```

---

## RUN

Executes commands during image build time.

Example:

```dockerfile
RUN pip install -r requirements.txt
```

---

## CMD

Specifies the default command executed when the container starts.

Example:

```dockerfile
CMD ["python", "main.py"]
```

---

# Building Images

Docker images are built using:

```bash
docker build -t image-name .
```

Example:

```bash
docker build -t feedback-backend ./backend
```

---

# Running Containers

Containers are started using:

```bash
docker run image-name
```

Example:

```bash
docker run redis
```

---

# Port Mapping

Containers run in isolated environments.

Port mapping exposes container services to the host machine.

Syntax:

```text
HOST_PORT:CONTAINER_PORT
```

Example:

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
localhost:8080
        ↓
container:80
```

---

# Docker Hub

Docker Hub is a public registry for Docker images.

It contains official images maintained by software vendors and the Docker community.

Examples:

```text
python
nginx
redis
postgres
node
```

Images can be downloaded using:

```bash
docker pull image-name
```

Example:

```bash
docker pull redis
```

---

# Why Use Official Images?

Benefits include:

* Faster development
* Community support
* Regular updates
* Security patches
* Reduced maintenance effort

Instead of building every service yourself, you can focus on your application.

---

# Docker Compose

Many applications consist of multiple services.

Example:

```text
Frontend
    ↓
Backend
    ↓
Redis
```

Managing these services individually becomes difficult.

Docker Compose solves this problem.

---

# What is Docker Compose?

Docker Compose allows you to define and run multi-container applications using a YAML file.

Example services:

```text
frontend
backend
redis
```

Instead of multiple commands:

```bash
docker run ...

docker run ...

docker run ...
```

you can use:

```bash
docker compose up
```

---

# Compose Workflow

```text
docker-compose.yml
           ↓
docker compose up
           ↓
Application Stack
```

---

# Basic Compose Concepts

## Service

A service defines a container.

Examples:

```text
frontend
backend
redis
```

---

## Build

Builds an image from a Dockerfile.

Example:

```yaml
build: ./backend
```

---

## Image

Pulls an existing image.

Example:

```yaml
image: redis:latest
```

---

## Ports

Maps container ports to host ports.

Example:

```yaml
ports:
  - "8080:80"
```

---

## Environment Variables

Provide configuration values to containers.

Example:

```yaml
environment:
  REDIS_HOST: redis
```

---

# Useful Docker Commands

## List running containers

```bash
docker ps
```

---

## List all containers

```bash
docker ps -a
```

---

## List images

```bash
docker images
```

---

## Stop a container

```bash
docker stop container-id
```

---

## Remove a container

```bash
docker rm container-id
```

---

## Build an image

```bash
docker build -t image-name .
```

---

## Pull an image

```bash
docker pull image-name
```

---

## Start Compose application

```bash
docker compose up
```

---

## Rebuild and start Compose application

```bash
docker compose up --build
```

---

## Stop Compose application

```bash
docker compose down
```

---

## View Compose logs

```bash
docker compose logs
```

---

# Docker and CI/CD

Docker plays an important role in modern CI/CD pipelines.

A common workflow is:

```text
Write Code
    ↓
Commit Changes
    ↓
Push to GitHub
    ↓
CI Pipeline Runs
    ↓
Docker Image Built
    ↓
Tests Executed
    ↓
Deployment
```

Containers help ensure that the environment used during testing matches the environment used in production.

---

# Key Takeaways

By the end of this workshop, you should understand that:

* Docker packages applications into containers.
* Images are templates used to create containers.
* Dockerfiles define how images are built.
* Docker Hub provides reusable images.
* Docker Compose manages multi-container applications.
* Docker integrates naturally into CI/CD workflows.

---

# Further Reading

Official Docker Documentation:

<https://docs.docker.com/>

Docker Compose Documentation:

<https://docs.docker.com/compose/>

Docker Hub:

<https://hub.docker.com/>
