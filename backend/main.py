from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import numpy as np
import cv2
from PIL import Image
import io
import base64

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect-faces")
async def detect_faces(file: UploadFile = File(...)):
    try:
        # Read the image file
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Convert BGR to RGB
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Find all face locations in the image
        face_locations = face_recognition.face_locations(rgb_img)
        
        # Get face encodings
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
        
        # Draw rectangles around faces
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Convert the image back to bytes
        _, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "image": img_str,
            "face_count": len(face_locations),
            "face_locations": face_locations,
            "face_encodings": [encoding.tolist() for encoding in face_encodings]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare-faces")
async def compare_faces(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    try:
        # Read and process first image
        contents1 = await file1.read()
        nparr1 = np.frombuffer(contents1, np.uint8)
        img1 = cv2.imdecode(nparr1, cv2.IMREAD_COLOR)
        rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        
        # Read and process second image
        contents2 = await file2.read()
        nparr2 = np.frombuffer(contents2, np.uint8)
        img2 = cv2.imdecode(nparr2, cv2.IMREAD_COLOR)
        rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        
        # Get face encodings
        face_encodings1 = face_recognition.face_encodings(rgb_img1)
        face_encodings2 = face_recognition.face_encodings(rgb_img2)
        
        if not face_encodings1 or not face_encodings2:
            return {"match": False, "message": "No faces detected in one or both images"}
        
        # Compare faces
        results = face_recognition.compare_faces([face_encodings1[0]], face_encodings2[0])
        face_distance = face_recognition.face_distance([face_encodings1[0]], face_encodings2[0])
        
        return {
            "match": bool(results[0]),
            "confidence": float(1 - face_distance[0])
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 