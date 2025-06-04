@echo off
echo Creating Modern Calculator Package...

REM Create dist directory if it doesn't exist
if not exist "dist" mkdir dist
if not exist "releases" mkdir releases

REM Install required packages
pip install pyinstaller pillow cairosvg

REM Convert SVG to ICO using Python
echo Converting icon...
python -c "from cairosvg import svg2png; from PIL import Image; svg2png(url='icon.svg', write_to='temp.png', output_width=256, output_height=256); img = Image.open('temp.png'); img.save('icon.ico', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]); import os; os.remove('temp.png')"

REM Create executable
echo Creating executable...
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico --name="Calculator" calculator.py

REM Create release package
echo Creating ZIP package...
powershell Compress-Archive -Force -Path "dist\Calculator.exe", "README.md", "Launch Calculator.bat" -DestinationPath "releases\ModernCalculator-Windows.zip"

echo Package created successfully!
echo Location: releases\ModernCalculator-Windows.zip
pause 