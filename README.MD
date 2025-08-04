# 💬 Uzbek Chatbot using Ollama (LLaMA 3.1)

This is a simple terminal-based chatbot that communicates in **Uzbek** using locally hosted **LLaMA models** via the `ollama` Python package.

---

## ✅ Requirements

- Python 3.8 or higher
- [Ollama](https://ollama.com/download) installed on your OS (Windows/macOS/Linux)
- Pulled LLM model (e.g., `llama3.1:latest`)

---

## 🔧 Setup Instructions

### 1. Create and activate a virtual environment

<details>
<summary>Windows</summary>
##1.Create Virtual Environment
```bash
python -m venv venv```
##2. Active 
```bash
venv\Scripts\activate``` 
</details>

<details> 
<summary>Linux/macOS</summary>
```bash
python3 -m venv venv```
```bash
source venv/bin/activate```
</details>

## 2. Install Python dependencies
```bash
pip install -r requirements.txt
```
## 3. Install Ollama
Download and install from the official page:

➡️ https://ollama.com/download

4. Pull the LLM model
```bash
ollama pull llama3.1:latest
```
### You may replace llama3.1:latest with any other supported model.


