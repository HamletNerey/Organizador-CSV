@echo off
REM 
where ollama >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Ollama no está instalado. Descárgalo desde: https://ollama.com/download/windows
    pause
    exit /b
)

REM 
ollama pull qwen2.5:1.5b

REM 
start dist\main.exe
pause
