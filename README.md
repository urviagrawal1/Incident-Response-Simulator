# 🚨 Incident Response Simulator

A CLI-based simulation tool to practice handling real-world system incidents like database failures, CPU spikes, and network timeouts — with scoring based on your response time.

---

## 📌 What This Project Does

This project simulates common backend/system incidents in a controlled environment and allows users to:

* Trigger and handle incidents via CLI
* Practice real-time response workflows
* Track response time and performance
* View logs and past performance

---

## ⚙️ Tech Stack

* **Backend:** Python
* **Frontend (UI):** HTML, CSS (for dashboard/templates)
* **Async Engine:** asyncio
* **TUI (optional):** Textual

---


## 🚀 Features

* 🔥 Simulates real incidents:

  * Database down
  * High CPU usage
  * Network timeouts and more such...

* ⏱️ Response time tracking & scoring

* 🧠 Practice-based learning via CLI

* 📊 Logs stored using TinyDB

* 🎯 Difficulty levels (Easy / Medium / Hard) *(planned / optional)*

* 🖥️ Dashboard support (HTML/CSS or Textual)

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone <https://github.com/urviagrawal1/Incident-Response-Simulator>
cd <project-folder>
```

### 2. Create virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the simulator:

```bash
python main.py
```

Follow CLI prompts to:

* View active incidents
* Respond to them
* Track your score

---

## 🧪 Example Workflow

1. Incident triggered: **Database Down**
2. User responds via CLI command
3. System logs response
4. Score calculated based on response time

---

## 📊 Scoring System

* Faster response → Higher score
* Delays reduce performance score
* All attempts are logged for review

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss.

---

## 📄 License

This project is for educational and practice purposes.

---

## 💡 Inspiration

Built to help developers and students practice real-world incident handling in a safe environment.

---

✨ *Practice like it's production.*
