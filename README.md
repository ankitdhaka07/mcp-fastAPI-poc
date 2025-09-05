## QuickStart

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/FastMCP-and-FastAPI.git
cd FastMCP-and-FastAPI
```

## 2. Create Virtual Environment (optional)
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn mcp fastmcp httpx

```

### 4. Start the FastAPI Server
```bash
# From the root directory
uvicorn src.app:app --reload
```

### 5. Start MCP Inspector (in a new terminal)
```bash
npx @modelcontextprotocol/inspector
```

### 6. Test the Application
1. Visit endpoints in browser:
   - http://localhost:8000/ - Welcome page
   - http://localhost:8000/status - Server status
   - http://localhost:8000/about - About info

2. In MCP Inspector:
   - Connect to: `http://localhost:8000/sse`
   - Test tools:
     ```python
     add(2, 3)
     greeting://YourName
     get_weather_alerts("CA")
     get_weather_forecast(37.7749, -122.4194)
     ```

### Project Structure
```
FastMCP-and-FastAPI/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── routes.py
│   ├── server.py
│   └── weather.py
├── main.py
└── server.py
```