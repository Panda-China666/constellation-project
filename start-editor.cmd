@echo off
cd /d "%~dp0"
if not exist ".local-editor\server.py" (
  echo Local editor bundle missing. Please use the complete project ZIP.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" python -m venv .venv
.venv\Scripts\python.exe -c "import material, mkdocs" >nul 2>&1
if errorlevel 1 .venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe .local-editor\server.py
pause
