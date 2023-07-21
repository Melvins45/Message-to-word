import win32com.client, os
oShell = win32com.client.Dispatch("Wscript.Shell")
print(oShell.SpecialFolders("MyDocuments"))

print(os.path.join(oShell.SpecialFolders("MyDocuments"), 'ten.txt'))