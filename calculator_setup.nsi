; Calculator Installer Script
!include "MUI2.nsh"

; General
Name "Modern Calculator"
OutFile "ModernCalculatorSetup.exe"
InstallDir "$PROGRAMFILES\Modern Calculator"
InstallDirRegKey HKCU "Software\Modern Calculator" ""

; Interface Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

Section "Install"
    SetOutPath "$INSTDIR"
    
    ; Add files
    File "calculator.py"
    File "Launch Calculator.vbs"
    
    ; Create desktop shortcut
    CreateShortCut "$DESKTOP\Modern Calculator.lnk" "wscript.exe" '"$INSTDIR\Launch Calculator.vbs"' "calc.exe" 0
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    
    ; Add uninstall information to Add/Remove Programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Modern Calculator" \
                     "DisplayName" "Modern Calculator"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Modern Calculator" \
                     "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
SectionEnd

Section "Uninstall"
    ; Remove files
    Delete "$INSTDIR\calculator.py"
    Delete "$INSTDIR\Launch Calculator.vbs"
    Delete "$INSTDIR\Uninstall.exe"
    
    ; Remove desktop shortcut
    Delete "$DESKTOP\Modern Calculator.lnk"
    
    ; Remove installation directory
    RMDir "$INSTDIR"
    
    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Modern Calculator"
    DeleteRegKey HKCU "Software\Modern Calculator"
SectionEnd 