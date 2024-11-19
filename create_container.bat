@echo off
echo Construyendo la imagen de Docker...
docker build -t traffic_analyzer .
if %ERRORLEVEL% neq 0 (
    echo Error al construir la imagen de Docker.
    exit /b 1
)
echo Ejecutando el contenedor...
docker run --rm --cap-add=NET_ADMIN --network host traffic_analyzer
if %ERRORLEVEL% neq 0 (
    echo Error al ejecutar el contenedor de Docker.
    exit /b 1
)
pause
