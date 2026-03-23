# 🤖 AI HR Assistant (MCP-Style Tool Calling)

An AI-powered HR assistant built using Python and OpenAI, designed to simulate real-world AI application architecture with dynamic tool calling.

---

## 🚀 Overview

This project demonstrates how a Large Language Model (LLM) can:

* Understand user queries
* Decide which backend function to invoke
* Execute business logic dynamically

The system follows an MCP-style (Model Context Protocol) architecture where AI orchestrates tool usage instead of relying on static rules.

---

## 🧠 Key Features

* 🔹 Natural language query handling
* 🔹 Dynamic function selection (Tool Calling)
* 🔹 HR use cases:

  * Leave balance lookup
  * Salary details
  * HR policy explanations
* 🔹 Streamlit-based web UI
* 🔹 Environment-based API key management

---

## 🏗️ Architecture

```
User Input (UI / CLI)
        ↓
   OpenAI LLM
        ↓
Decision (Action + Input)
        ↓
Backend Tools (Python Functions)
        ↓
   Final Response
```

---

## 🛠️ Tech Stack

* Python
* OpenAI (GPT-4o-mini)
* Streamlit (UI)
* dotenv (environment management)

---

## 📂 Project Structure

```
HR_Assist_mcp/
│── app.py            # Core AI logic
│── app_ui.py         # Streamlit UI
│── tools.py          # Business logic functions
│── data.py           # Sample HR data
│── prompts.py        # Prompt templates
│── .env              # API keys (not committed)
│── requirements.txt
```

---

## 🔑 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/HR_Assist_mcp.git
cd HR_Assist_mcp
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run the application

#### CLI Mode

```
python app.py
```

#### Web UI (Recommended)

```
streamlit run app_ui.py
```

---

## 🧪 Sample Queries

* "How many leaves does employee 101 have?"
* "Give me salary details for employee 102"
* "Explain maternity policy"

---

## 🎯 Learning Outcomes

* Built an end-to-end AI application
* Understood LLM-based decision making
* Implemented MCP-style architecture
* Integrated backend tools with AI
* Developed UI for real-world usability

---

## 📸 Screenshots
![HR_Assist_mcp](screenshot.png)

---

## 💡 Future Enhancements

* Chat history support
* Authentication layer
* Database integration
* Advanced prompt engineering
* Multi-tool orchestration

---

## 👩‍💻 Author

**Girija Barathi**
Oracle HCM Functional & AI Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ and connect on LinkedIn!

