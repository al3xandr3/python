
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo activate
call C:\ProgramData\Anaconda3\Scripts\activate.bat

echo conda update -n root conda
conda update -n root conda

TIMEOUT 10
