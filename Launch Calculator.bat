@echo off
title Modern Calculator
cd /d "%~dp0"

echo Starting Modern Calculator...
echo Please wait...

if not exist "Calculator.exe" (
    echo Error: Calculator.exe not found!
    echo Please make sure you extracted all files from the ZIP package.
    echo.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

start "" "Calculator.exe"
exit
