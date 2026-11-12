@echo off
setlocal

set "ROOT=%~dp0"

start "Haven Backend" /D "%ROOT%backend" cmd /k uvicorn main:app --reload --port 8000
start "Haven Frontend" /D "%ROOT%frontend" cmd /k npm run dev

echo Backend and frontend terminals started.
endlocal