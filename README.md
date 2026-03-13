# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimension Adaptive Testing Prototype** that dynamically adjusts question difficulty based on a student's responses. The system estimates the student’s ability level and selects questions accordingly.

After completing the test, the system generates a **personalized AI study plan** based on the student’s weaknesses.

This project demonstrates:

* Adaptive learning systems
* Backend API development
* MongoDB data modeling
* AI integration with LLMs
* Clean modular architecture

---

# System Architecture

```
Student
   ↓
FastAPI Backend
   ↓
Adaptive Algorithm
   ↓
MongoDB Question Database
   ↓
OpenAI API
   ↓
Personalized Study Plan
```

---

# Tech Stack

| Component         | Technology             |
| ----------------- | ---------------------- |
| Backend           | FastAPI (Python)       |
| Database          | MongoDB Atlas          |
| AI Integration    | OpenAI API             |
| API Documentation | Swagger (FastAPI Docs) |
| Version Control   | Git & GitHub           |

---

# Project Structure

```
adaptive-diagnostic-engine
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── adaptive_engine.py
│   ├── ai_service.py
│   └── models.py
│
├── seed_questions.py
├── test_db.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How to Run the Project

## 1 Install dependencies

```
pip install -r requirements.txt
```

---

## 2 Configure environment variables

Create a `.env` file in the root directory.

```
MONGO_URI=your_mongodb_connection_string
OPENAI_API_KEY=your_openai_api_key
```

---

## 3 Seed the question database

```
python seed_questions.py
```

This inserts GRE-style questions into MongoDB.

---

## 4 Run the server

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 5 Open API documentation

```
http://127.0.0.1:8000/docs
```

Swagger UI allows testing all endpoints.

---

# Adaptive Algorithm Logic

The system uses a **simplified Item Response Theory (IRT) approach**.

### Starting ability

```
ability = 0.5
```

### Ability update rule

| Response  | Ability Change |
| --------- | -------------- |
| Correct   | +0.1           |
| Incorrect | −0.1           |

Ability is constrained between:

```
0.1 ≤ ability ≤ 1.0
```

### Question selection

The next question is selected based on:

```
difficulty ≥ user ability
```

This ensures the system gradually adapts difficulty to match the student's skill level.

---

# API Endpoints

## GET /next-question

Returns the next question based on the student's current ability level.

Example response:

```
{
 "current_ability": 0.5,
 "question": {
   "question": "What is 15% of 200?",
   "options": ["20","25","30","35"],
   "difficulty": 0.6,
   "topic": "Arithmetic"
 }
}
```

---

## POST /submit-answer

Updates the student's ability score based on whether the answer was correct.

Example:

```
/submit-answer?is_correct=true
```

Response:

```
{
 "new_ability": 0.6
}
```

---

## GET /study-plan

Generates a personalized AI study plan based on weaknesses.

Example response:

```
{
 "study_plan": "1. Review algebra fundamentals. 2. Practice GRE vocabulary daily. 3. Solve medium difficulty quantitative problems."
}
```

---

# Database Schema

## Questions Collection

Example document:

```
{
 "question": "What is 5 + 7?",
 "options": ["10","11","12","13"],
 "correct_answer": "12",
 "difficulty": 0.2,
 "topic": "Algebra",
 "tags": ["addition"]
}
```

---

## Sessions Collection

Tracks the student's test progress and estimated ability level.

Example:

```
{
 "user_id": "123",
 "ability": 0.5,
 "questions_answered": []
}
```

---

# AI Usage Log

AI tools were used to accelerate development and improve system design.

### Tools used

* ChatGPT for algorithm design and architecture planning
* Cursor AI / GitHub Copilot for code suggestions

### Challenges

Implementing a full **Item Response Theory model** would require complex probability calculations.
For this prototype, a simplified ability adjustment approach was implemented to maintain clarity and performance.

---

# Future Improvements

Potential enhancements include:

* Full IRT probability model
* User session tracking
* Difficulty calibration
* Frontend dashboard for students
* Performance analytics

---

# Author

Eshwar Vivek Sanam

Project developed as part of an **AI Internship Assignment: Adaptive Diagnostic Engine**.