@echo off
echo Setting up website structure...

REM Create website directory structure
mkdir website 2>nul
mkdir website\css 2>nul
mkdir website\js 2>nul
mkdir website\images 2>nul
mkdir website\downloads 2>nul

REM Copy and organize files
copy styles.css website\css\ /Y
copy script.js website\js\ /Y
copy icon.svg website\images\ /Y
copy index.html website\ /Y
copy download.html website\ /Y

REM Create preview image from SVG
echo Converting SVG to preview image...
python -c "from cairosvg import svg2png; svg2png(url='icon.svg', write_to='website/images/preview.png', output_width=1200, output_height=630)"

REM Create favicon
echo Creating favicon...
python -c "from cairosvg import svg2png; from PIL import Image; svg2png(url='icon.svg', write_to='temp.png', output_width=256, output_height=256); img = Image.open('temp.png'); img.save('website/favicon.ico', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]); import os; os.remove('temp.png')"

REM Copy release files
copy releases\ModernCalculator-Windows.zip website\downloads\ /Y
copy releases\ModernCalculator.apk website\downloads\ /Y
copy releases\ModernCalculator-Source.zip website\downloads\ /Y

echo Website files organized successfully! 