# Face Recognition Web Application

A web application that uses deep learning to detect and recognize faces in images. The application provides three main features:
1. Face detection in uploaded images
2. Face comparison between two images
3. Real-time face detection using webcam

## Features

- Face detection using the `face_recognition` library
- Face comparison with confidence score
- Real-time webcam face detection
- Modern and responsive UI
- RESTful API using FastAPI

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Web browser with WebRTC support (for webcam functionality)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd face-recognition-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the backend server:
```bash
cd backend
python main.py
```

2. Open the frontend:
- Open `frontend/index.html` in your web browser
- Or use a local web server (e.g., Python's built-in server):
```bash
cd frontend
python -m http.server 8080
```
Then open `http://localhost:8080` in your browser

## Usage

### Face Detection
1. Click "Upload Image" to select an image file
2. The application will detect faces and display them with bounding boxes
3. The number of detected faces will be shown

### Face Comparison
1. Upload two images using the "Upload Image 1" and "Upload Image 2" buttons
2. The application will compare the faces and show if they match
3. A confidence score will be displayed

### Webcam Face Detection
1. Click "Start Webcam" to begin real-time face detection
2. The application will show the webcam feed with face detection
3. Click "Stop Webcam" to stop the camera

## API Endpoints

- `POST /detect-faces`: Detect faces in an uploaded image
- `POST /compare-faces`: Compare faces between two uploaded images

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Face Recognition: face_recognition library
- Image Processing: OpenCV, Pillow

## License

This project is licensed under the MIT License - see the LICENSE file for details. 