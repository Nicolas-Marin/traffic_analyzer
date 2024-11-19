#!/bin/bash
echo "Construyendo la imagen de Docker..."
docker build -t traffic_analyzer .
if [ $? -ne 0 ]; then
    echo "Error al construir la imagen de Docker."
    exit 1
fi

echo "Ejecutando el contenedor..."
docker run --rm --cap-add=NET_ADMIN --network host traffic_analyzer
if [ $? -ne 0 ]; then
    echo "Error al ejecutar el contenedor de Docker."
    exit 1
fi
