@echo off
setlocal

cd /d "%~dp0"

python -m pip install --upgrade pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name NorthSussexJudoFeeCalculator main.py

echo.
echo Build complete.
echo Your Windows executable should be in dist\NorthSussexJudoFeeCalculator.exe
endlocal
