### 1. install uv
window
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### 2. activate uv

uv venv

.venv\Scripts\activate

### 3. install import
./import_library_win.bat

### 4. config.py
OLLAMA_URL = "http://localhost:11434"

SERVER_MODE = "tailscale"
# SERVER_MODE = "public" or "tailscale"
# public is not active

API_KEY = ""

NAVER_CLIENT_ID = ""
NAVER_CLIENT_SECRET = ""
SERPER_API_KEY = ""

### 5. run
./run_win.bat
