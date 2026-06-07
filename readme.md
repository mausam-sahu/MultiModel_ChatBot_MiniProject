# 🤖 AI Customer Support Chatbot

An AI-powered customer support chatbot built using **FastAPI**, **LangChain**, and **Groq Llama Models**. The application generates structured and intelligent responses using prompt engineering, LCEL (LangChain Expression Language), and Pydantic-based output validation.

---

## 🚀 Features

* FastAPI backend for high-performance API development
* Groq Llama model integration
* LangChain prompt templates and LCEL pipelines
* Structured JSON outputs using Pydantic
* REST API endpoints
* Modular and scalable project architecture
* Easy integration with frontend applications

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* Groq API
* Pydantic
* Uvicorn
* HTML/CSS/JavaScript

---

## 📂 Project Structure

```text
Multi_Chatbot_Mini_Project/

├── app/
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── __init__.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   └── script.js
│
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Multi_Chatbot_Mini_Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 Example API Request

```json
{
  "message": "What is Artificial Intelligence?"
}
```

### Example Response

```json
{
  "summary": "User asked about AI",
  "sentiment": 85,
  "response": "Artificial Intelligence is a field of computer science..."
}
```

---

## 🧠 Learning Outcomes

This project demonstrates:

* FastAPI application development
* LangChain prompt engineering
* LCEL chain creation
* Structured output parsing
* LLM integration with Groq
* REST API development
* Production-ready project organization

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Mausam

AI & Machine Learning Enthusiast | Generative AI Developer
