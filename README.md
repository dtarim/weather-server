# 🌍 Weather Server

This is the **server** component of the Weather Publisher & Server project. The server receives weather data sent by the Publisher, stores it temporarily in memory, and serves a simple web page displaying the weather information for multiple cities.

---

## 🧩 Project Overview

- **Receives weather data** via HTTP POST requests from the Publisher.
- **Stores weather data in memory** (no database used).
- **Serves a web page** that shows city names and their corresponding temperatures in a table.
- Built using **Flask**, a lightweight Python web framework.

---

## 🚀 How to Run

1. Make sure you have Python 3.11+ installed.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

   ---
   
🛠️ Technologies Used

Python 3.11+

Flask web framework

HTTP for communication between Publisher and Server
