# Faster Ways to Containerize Applications

<!--toc:start-->
- [Faster Ways to Containerize Applications](#faster-ways-to-containerize-applications)
  - [Docker Init](#docker-init)
    - [Advantages](#advantages)
    - [Disadvantages](#disadvantages)
  - [VS Code Container Tools Extension](#vs-code-container-tools-extension)
    - [Features](#features)
    - [Typical Workflow](#typical-workflow)
    - [Advantages](#advantages-1)
    - [Disadvantages](#disadvantages-1)
- [Recommended Learning Path](#recommended-learning-path)
<!--toc:end-->

In this workshop, we created Docker configuration files manually so that we could understand how Docker works.

However, developers often use tools to automatically generate the following files:

* `Dockerfile`
* `docker-compose.yaml` (can be named `compose.yaml`, `compose.yml`, `docker-compose.yml`; all are supported)
* `.dockerignore`
* `README.Docker.md`

Two commonly used approaches are:

* Docker Init (`docker init`)
* The Container Tools extension for Visual Studio Code

Both give you a series of questions before generating Docker-related files such as:

* What language are you using?
* What framework are you using?
* What port should the container listen on?
* What command should be used to run the container?

---

## Docker Init

Docker provides a command called:

```bash
docker init
```

To generate Docker-related files for your project.

---

### Advantages

* Faster setup.
* Reduces typing.
* Provides sensible defaults.
* Useful for prototyping.

---

### Disadvantages

* Generated files may contain unnecessary instructions.
* You may not understand what the generated files do.
* Multi-service applications still require manual refinement.
* Only accessible if Docker desktop is installed.

---

## VS Code Container Tools Extension

Visual Studio Code provides extensions that assist with Docker development.

Examples include:

```text
Container Tools
Dev Containers
```

These extensions provide graphical interfaces for common Docker operations.

---

### Features

Developers can:

* Generate Dockerfiles.
* Generate Compose files.
* Build images.
* Start containers.
* View logs.
* Inspect running containers.
* Manage Docker resources.

---

### Typical Workflow

1. Open the project in VS Code.
2. Install the Docker extension.
3. Open the Command Palette.
4. Search for Docker-related commands.
5. Generate Docker assets.

---

### Advantages

* Beginner-friendly.
* Reduces memorisation of commands.
* Faster iteration.
* Helpful visualisation of containers and images.

---

### Disadvantages

* Generated assets still require review.
* Behaviour may differ between IDEs/not all IDEs support the extension.
* Troubleshooting often requires command-line knowledge.

---

# Recommended Learning Path

For this workshop, the recommended progression is:

```text
Understand the concepts
        ↓
Write the Docker files manually
        ↓
Use Docker Compose manually
        ↓
Experiment with scaffolding tools
        ↓
Adopt tooling in future projects
```

I highly recommend using the tools to generate Docker assets first then customise them.
This helps prevent accidental overwrites.

---
