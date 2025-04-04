# Agentic CI/CD Pipeline

This project implements an agentic CI/CD pipeline that automates workflows using Git commit hooks. When a commit is made with the name `testmycode`, a bash script with `curl` sends the required files to a backend server. The backend, built with FastAPI and LangGraph, processes these files by organizing tasks into a graph of nodes for CI/CD operations.
The frontend is svelte basic ui template with env, prettier, eslint etc

---

## Features

- **Git Commit Hooks**: Triggers actions locally on each commit using a `pre-commit` hook.
- **Bash Script with `curl`**: Sends files to the backend server upon committing changes.
- **FastAPI Backend**: Handles incoming files and processes them efficiently.
- **LangGraph Integration**: Creates a graph of nodes in the backend to manage and execute CI/CD tasks.

---

## How It Works

1. When you run `git commit`, the `pre-commit` hook executes a bash script.
2. The bash script uses `curl` to send the necessary files to the backend.
3. The FastAPI backend receives the files and uses LangGraph to construct a graph of nodes.
4. These nodes process the files and perform CI/CD tasks, such as generating reports or running automated checks.

---

## Backend Details

The backend is powered by **FastAPI** and uses **LangGraph** to create a graph of nodes. Here’s how it works:
- **File Reception**: Accepts files sent via `curl` from the commit hook.
- **Graph Construction**: LangGraph organizes the processing logic into a series of nodes.
- **Task Execution**: Each node handles specific CI/CD tasks, such as file validation, processing, or report generation.

This project is under development, as only some of the things are being done now, i will the best features later on
