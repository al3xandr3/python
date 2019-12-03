
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo npm-windows-upgrade --npm-version latest
npm-windows-upgrade --npm-version latest

TIMEOUT 10
