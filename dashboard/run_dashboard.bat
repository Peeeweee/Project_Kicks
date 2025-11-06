@echo off
echo ============================================
echo   Kicks: Adidas US Sales Dashboard
echo ============================================
echo.
echo Starting Flask server...
echo.
echo Dashboard will be available at:
echo   - http://localhost:5001
echo   - http://127.0.0.1:5001
echo.
echo Press CTRL+C to stop the server
echo ============================================
echo.

cd /d "%~dp0"
python app.py

pause