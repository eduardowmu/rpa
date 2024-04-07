$exclude = @("venv", "Gmail.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Gmail.zip" -Force