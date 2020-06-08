@ECHO OFF
REM SETLOCAL
set PATH=E:\prog\venv_omongobot\Scripts;%PATH%
pyside2-uic main_window.ui -o ..\app_lib\main_window.py
REM ENDLOCAL