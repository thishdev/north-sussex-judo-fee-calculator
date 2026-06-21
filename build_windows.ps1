Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Set-Location $PSScriptRoot

python -m pip install --upgrade pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name NorthSussexJudoFeeCalculator main.py

Write-Host ""
Write-Host "Build complete."
Write-Host "Your Windows executable should be in dist\NorthSussexJudoFeeCalculator.exe"
