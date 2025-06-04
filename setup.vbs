Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

' Get paths
strProgramFiles = WShell.ExpandEnvironmentStrings("%ProgramFiles%")
strDesktop = WShell.SpecialFolders("Desktop")
strAppFolder = strProgramFiles & "\Modern Calculator"

' Create program directory if it doesn't exist
If Not FSO.FolderExists(strAppFolder) Then
    FSO.CreateFolder(strAppFolder)
End If

' Get the script's directory
strCurrentPath = FSO.GetParentFolderName(WScript.ScriptFullName)

' Copy files to program directory
FSO.CopyFile strCurrentPath & "\calculator.py", strAppFolder & "\calculator.py"
FSO.CopyFile strCurrentPath & "\Launch Calculator.vbs", strAppFolder & "\Launch Calculator.vbs"

' Create desktop shortcut
Set shortcut = WShell.CreateShortcut(strDesktop & "\Modern Calculator.lnk")
shortcut.TargetPath = "wscript.exe"
shortcut.Arguments = """" & strAppFolder & "\Launch Calculator.vbs" & """"
shortcut.WorkingDirectory = strAppFolder
shortcut.IconLocation = "calc.exe,0"
shortcut.Save

MsgBox "Modern Calculator has been installed successfully!" & vbCrLf & _
       "A shortcut has been created on your desktop.", 64, "Installation Complete" 