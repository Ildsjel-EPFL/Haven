@echo off
setlocal

set "ROOT=%~dp0"

start "SME GPS Backend" /D "%ROOT%backend" cmd /k uvicorn main:app --reload --port 8000
start "SME GPS Frontend" /D "%ROOT%frontend" cmd /k npm run dev

echo Backend and frontend terminals started.
endlocal