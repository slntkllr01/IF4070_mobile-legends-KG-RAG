@echo off
echo ========================================
echo   Mobile Legends RAG - Web UI Launcher
echo ========================================
echo.

echo [1/2] Starting Backend API Server...
echo.
start "ML RAG API" cmd /k "python api_server.py"

echo Waiting for backend to initialize (30 seconds)...
timeout /t 30 /nobreak

echo.
echo [2/2] Starting Frontend Dev Server...
echo.
cd web-ui
start "ML RAG Frontend" cmd /k "npm run dev"

echo.
echo ========================================
echo   Services Started!
echo ========================================
echo.
echo Backend API:  http://localhost:8000
echo Frontend UI:  http://localhost:3000
echo.
echo Press any key to open browser...
pause
start http://localhost:3000
