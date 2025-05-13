# 🌐 MCP Tools: Agent APIs & Utilities for Multi-Agent Systems

Welcome to the **MCP Tools** repository! This project hosts a growing suite of API utilities and tools designed for seamless integration with agentic platforms like **MIT Claude MCP** and **A2A (Agent-to-Agent)** networks.

## 🚀 Overview

This toolkit powers multi-agent systems by providing plug-and-play tools for information gathering, user profile enrichment, environmental context, and external service calls. These tools have been tested and deployed in various MCP-based demo agents, including weather agents, news summarizers, and social profile fetchers.

## 🧰 Included Tools

| Tool Name         | Description                                              | Endpoint                     |
|-------------------|----------------------------------------------------------|------------------------------|
| `weather_api`     | Get live weather data by city or coordinates             | `/weather?city=Boston`       |
| `news_api`        | Fetch latest headlines by category or keyword            | `/news?topic=technology`     |
| `nasa_api`        | Access NASA's Astronomy Picture of the Day               | `/nasa/apod`                 |
| `linkedin_profile`| Simulate fetching LinkedIn-style profile information     | `/linkedin?name=John%20Doe`  |
| `agent_status`    | Check health and metadata of registered MCP agents       | `/agents/status`             |

## 🛠 Setup

```bash
git clone https://github.com/YOUR_USERNAME/mcp-tools.git
cd mcp-tools
pip install -r requirements.txt
uvicorn main:app --reload
You’ll need Python 3.8+ and FastAPI, requests, and uvicorn installed.

🔗 Integration with MCP
All tools return JSON-ready outputs and are designed to be easily invoked from MCP-compatible agents via REST APIs. You can also wrap these tools as MCP server plugins or A2A service modules.

📦 Example Usage
bash
Copy
Edit
curl http://localhost:8000/weather?city=San%20Francisco
json
Copy
Edit
{
  "city": "San Francisco",
  "temperature": "18°C",
  "condition": "Partly Cloudy"
}
🧠 Demo
A live demo of the MCP agent using these tools is featured in the Agentic AI Talk (MCP demo at 27:00).

📌 Contributing
Have a useful microservice idea for agents? Pull requests are welcome! Please include tests and API docstrings in your contributions.

📄 License
MIT License © 2025 [Your Name / Organization]

