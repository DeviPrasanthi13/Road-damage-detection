# Road-damage-detection
Road Damage Detection using Deep learning(YOLOv8)
This project is a web-based application that allows users to upload images or videos of roads to detect damages using a backend Python script. The frontend is built with HTML, CSS, and JavaScript, while the backend is powered by Python.

Features:
---------
Upload images or videos for road damage detection.

Display uploaded media on the webpage.

Process media using a Python-based detection algorithm.

Show detection results on the frontend.

Technologies Used:
------------------
Frontend: HTML, CSS, JavaScript

Backend: Python (Flask for API)

Setup Instructions
------------------
Prerequisites

Ensure you have the following installed:

Python 3.x

Flask ( using Flask for the backend) 

Required Python libraries (OpenCV, NumPy, etc.)

Installation Steps
-------------------
1. Clone the Repository:

   git clone https://github.com/your-username/road-damage-detection.git
   cd road-damage-detection

2. Set Up the Python Environment:

   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies:

   pip install -r requirements.txt

4. Run the Backend Server:
   If using Flask:

   python app.py

   If using Django:

   python manage.py runserver

5. Open the Frontend:
   Open index.html in your browser or serve it using a local server.
