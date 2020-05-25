
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo jupyter lab build
jupyter lab clean


echo jupyter labextension update --all
jupyter labextension update --all


echo jupyter lab build
jupyter lab build


TIMEOUT 10

echo jupyter labextension install @jupyter-widgets/jupyterlab-manager
