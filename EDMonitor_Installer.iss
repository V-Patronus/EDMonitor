[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C6D2E14A-5A0D-4A2D-B7E2-9E1A334B5C6F}
AppName=EDMonitor
AppVersion=1.0
AppPublisher=Manuel de Jesús Ruiz Martínez
DefaultDirName={pf}\EDMonitor
DefaultGroupName=EDMonitor
OutputDir=.
OutputBaseFilename=EDMonitor_Setup_x64
SetupIconFile=assets\logo\logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\EDMonitor\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\EDMonitor"; Filename: "{app}\EDMonitor.exe"
Name: "{userdesktop}\EDMonitor"; Filename: "{app}\EDMonitor.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\EDMonitor.exe"; Description: "{cm:LaunchProgram,EDMonitor}"; Flags: nowait postinstall skipifsilent
