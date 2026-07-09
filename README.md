### 1. install uv
window
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### 2. activate uv

uv venv

.venv\Scripts\activate

### 3. install import
./import_library_win.bat

### 4. run
./run_win.bat
