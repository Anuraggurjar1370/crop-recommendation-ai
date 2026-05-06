# 🌾 Crop Recommendation System (AI + Data Science Project)

## 📌 Overview

This project is an **AI-powered Crop Recommendation System** that suggests the most suitable crop to grow based on soil nutrients and environmental conditions.

It uses **Machine Learning** for prediction and a **Flask API + Web UI** to make it interactive and user-friendly.

---

## 🚀 Features

* 🌱 Predict best crop using AI model
* 📊 Uses soil parameters (N, P, K) and environmental data
* 🌐 Web-based interface (HTML, CSS, JS)
* 🔗 Backend API using Flask
* ⚡ Fast and real-time prediction

---

## 🧠 Tech Stack

### 🔹 Machine Learning

* Python
* Pandas
* Scikit-learn

### 🔹 Backend

* Flask
* Flask-CORS

### 🔹 Frontend

* HTML
* CSS
* JavaScript

### 🔹 Deployment (Optional)

* Render (Backend)
* Vercel (Frontend)

---

## 📂 Project Structure

```
Agriculture-ai-crop-project/
│
├── Backend/
│   ├── app.py
│   ├── model.pkl
│   ├── requirements.txt
│
├── frontend/
│   └── index.html
│
├── dataset/
│   └── crop_data.csv
│
├── notebooks/
│   └── training.ipynb
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters soil and weather data in UI
2. Frontend sends data to Flask API
3. API loads trained ML model (`model.pkl`)
4. Model predicts the best crop
5. Result is returned and displayed

---

## 🔄 Workflow

```
User Input → Frontend → Flask API → ML Model → Prediction → UI Output
```

---

## 🧪 Input Parameters

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

---

## 📊 Output

* Recommended Crop (e.g., Rice, Wheat, Maize, etc.)

---

## 🛠️ Installation & Setup

### 🔹 Step 1: Clone Project

```
git clone <your-repo-link>
cd Agriculture-ai-crop-project
```

---

### 🔹 Step 2: Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 Step 4: Run Backend (Flask API)

```
cd Backend
python app.py
```

👉 API runs at:

```
http://127.0.0.1:5000
```

---

### 🔹 Step 5: Run Frontend

```
cd frontend
python -m http.server 5500
```

👉 Open in browser:

```
http://127.0.0.1:5500
```

---

## 🔗 API Endpoint

### 📍 Predict Crop

```
POST /predict
```

### 📥 Request JSON

```
{
  "N": 90,
  "P": 40,
  "K": 40,
  "temperature": 25,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}
```

### 📤 Response

```
{
  "recommended_crop": "rice"
}
```

---

## 🚨 Common Issues

### ❌ CORS Error

Install:

```
pip install flask-cors
```

Add in `app.py`:

```
from flask_cors import CORS
CORS(app)
```

---

### ❌ model.pkl not found

Make sure it is inside:

```
Backend/model.pkl
```

---

### ❌ Module not found

```
pip install flask pandas scikit-learn
```

---

## 🌍 Deployment

### 🔹 Backend

Deploy using Render

### 🔹 Frontend

Deploy using Vercel

---

## 📈 Future Enhancements

* 🌦️ Weather API integration
* 📊 Data visualization dashboard
* 📱 Mobile app version
* 🌍 Multi-language support
* 🤖 Chatbot assistant for farmers

---

## 👨‍💻 Author

**Anurag Gurjar**

---

## 📜 License

This project is for educational purposes.
