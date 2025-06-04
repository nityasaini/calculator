@echo off
echo Creating packages...

REM Create Windows package
mkdir temp_package
copy calculator.py temp_package\
copy icon.svg temp_package\
copy README.md temp_package\
cd temp_package
powershell Compress-Archive -Path * -DestinationPath ..\website\downloads\ModernCalculator-Windows.zip -Force
cd ..
rmdir /s /q temp_package

REM Create placeholder APK
echo "This is a placeholder APK file. Please build the real APK using the instructions in README.md" > website\downloads\ModernCalculator.apk

echo Packages created successfully! 