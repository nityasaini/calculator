Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
strCurrentPath = FSO.GetParentFolderName(WScript.ScriptFullName)

' Check if Python is in PATH
On Error Resume Next
pythonPath = "pythonw.exe"
WShell.Run "cmd /c where pythonw.exe", 0, True
If Err.Number <> 0 Then
    pythonPath = "python.exe"
    WShell.Run "cmd /c where python.exe", 0, True
    If Err.Number <> 0 Then
        MsgBox "Python is not installed or not in PATH. Please install Python and make sure to check 'Add Python to PATH' during installation.", 16, "Error"
        WScript.Quit
    End If
End If
On Error Goto 0

' Check if calculator.py exists
If Not FSO.FileExists(strCurrentPath & "\calculator.py") Then
    MsgBox "Cannot find calculator.py in the same folder. Make sure all files are extracted from the zip file.", 16, "Error"
    WScript.Quit
End If

' Run the calculator
WShell.CurrentDirectory = strCurrentPath
WShell.Run """" & pythonPath & """ """ & strCurrentPath & "\calculator.py""", 0, False 