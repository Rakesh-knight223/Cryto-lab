# Lab 2: Broken Object Level Authorization (BOLA)

## Overview
In this lab, you will explore **Broken Object Level Authorization (BOLA)**, also known as IDOR (Insecure Direct Object Reference). Your goal is to identify and exploit vulnerabilities in the provided "Enterprise Portal" application.

## Objectives
1.  **Analyze** the application's authorization mechanisms.
2.  **Identify** potential BOLA vulnerabilities in direct and nested object references.
3.  **Exploit** these vulnerabilities to access data belonging to other users.
4.  **Protocol** your findings with proof of concept.

## Setup
To start the lab environment, run the following command in your terminal:

```bash
docker run --rm -p 5000:80 \
  -e ASPNETCORE_HTTP_PORTS=80 \
  -e ASPNETCORE_ENVIRONMENT=Development \
  ghcr.io/ryazanov-dmitry/lab2-bola:latest
```

Once running, access the application at: `http://localhost:5000`

Backend API at `http://localhost:5000/swagger/index.html`