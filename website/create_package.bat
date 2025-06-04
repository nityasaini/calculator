@echo off
echo Checking required files...

if not exist "calculator.py" (
    echo Error: calculator.py not found!
    pause
    exit /b 1
)

if not exist "Launch Calculator.vbs" (
    echo Error: Launch Calculator.vbs not found!
    pause
    exit /b 1
)

if not exist "setup.vbs" (
    echo Error: setup.vbs not found!
    pause
    exit /b 1
)

echo All files found. Creating package...
powershell -Command "Compress-Archive -Force -Path 'calculator.py','Launch Calculator.vbs','setup.vbs' -DestinationPath 'ModernCalculator.zip'"

if %ERRORLEVEL% EQU 0 (
    echo Package created successfully!
    echo The zip file is located at: %CD%\ModernCalculator.zip
) else (
    echo Error creating package! Error code: %ERRORLEVEL%
)

pause 