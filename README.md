# CollegiateChatter — College Enquiry Chatbot

**CollegiateChatter** is a web-based college enquiry chatbot that helps users get quick answers to common questions (courses, admissions, events, contact, etc.) through an interactive chat interface.

It provides:
- A simple website with multiple pages (`/`, `/about`, `/courses`, `/events`, `/contact`)
- A chatbot UI (`/chats`) where users can ask questions
- A backend endpoint (`/chat`) that takes user input and returns a chatbot response

---

## What this project does

This project runs a **Flask web app** that serves HTML pages and a chat interface.  
When a user types a question in the chat UI, the backend:

1. Converts the user message into vector form using a saved **vectorizer** (`vectorizer.pkl`)
2. Uses a trained ML model (`chatbot_model.pkl`) to predict the **intent/tag**
3. Looks up that intent in an **intents JSON file** (`intents1.json`)
4. Returns a random response from the matching intent’s response list

So the chatbot works using a classic **intent classification + response selection** approach.

---

## How it was built

### Tech stack
- **Backend:** Python + Flask
- **ML Model:** Stored as pickle files (`.pkl`)
- **Intent data:** JSON file (`chatbot/dataset/intents1.json`)
- **Frontend:** HTML/CSS templates (served via Flask)
- **Database (configured):** SQLite via Flask-SQLAlchemy (`sqlite:///chatbot.db`)

### Project structure (high level)
- `run.py`  
  Starts the Flask app on port `5000`

- `chatbot/__init__.py`  
  Initializes Flask, sets config, connects SQLAlchemy, registers routes

- `chatbot/routes.py`  
  Defines website routes + loads the trained chatbot model/vectorizer + implements the `/chat` endpoint

- `chatbot/model/`  
  Contains:
  - `chatbot_model.pkl`
  - `vectorizer.pkl`

- `chatbot/dataset/`  
  Contains:
  - `intents1.json` (intents + responses)

---

## How to run this project on your computer

### 1) Clone the repository
```bash
git clone https://github.com/Aryakp1/collegiatechatter.git
cd collegiatechatter
```

### 2) Create and activate a virtual environment (recommended)

**Windows (PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

> Note: your `requirements.txt` is very large. If install is slow or fails, you can later trim it to only the packages the app actually needs (Flask, Flask-Session, Flask-Login, Flask-SQLAlchemy, scikit-learn, etc.).

### 4) Ensure model + dataset files exist
Make sure these files are present (they are required at runtime):

- `chatbot/model/chatbot_model.pkl`
- `chatbot/model/vectorizer.pkl`
- `chatbot/dataset/intents1.json`

### 5) Run the Flask app
```bash
python run.py
```

The app should start at:
- `http://127.0.0.1:5000/`

Chat page:
- `http://127.0.0.1:5000/chats`

---

## Usage

1. Open the chat page in your browser (`/chats`)
2. Type a question into the chat input
3. The backend calls `/chat` and returns a response based on the predicted intent

---

## Future improvements (optional ideas)
- Add better error handling if model files are missing
- Add conversation history using Flask session
- Replace pickle model with a more deploy-friendly format
- Add admin panel to update intents/responses without code changes

---

## License
Add a license if you plan to make this open-source (MIT, Apache-2.0, etc.).
