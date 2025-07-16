# 🌍 Weather Server

This is the **server** component of the Weather Publisher & Server project. The server receives weather data sent by the Publisher, stores it temporarily in memory, and serves a simple web page displaying the weather information for multiple cities.

---

## 🧩 Project Overview

- **Receives weather data** via HTTP POST requests from the Publisher.
- **Stores weather data in memory** (no database used).
- **Serves a web page** that shows city names and their corresponding temperatures in a table.
- Built using **Flask**, a lightweight Python web framework.

---

🛠️ Automation & Containerization

**-GitHub Actions is set up to:**

Automatically run tests and lint checks on pushes and pull requests to the master branch.

Create and test a Python virtual environment.

Ensure code quality with flake8.

**Future plans include:**

Building Docker images for both Publisher and Server.

Pushing these images to Docker Hub or another container registry.

Using containers for easier deployment and consistent environments.

Possibly deploying to Kubernetes or cloud container services.



