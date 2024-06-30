$exclude = @("venv", "GoogleDrive.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "GoogleDrive.zip" -Force