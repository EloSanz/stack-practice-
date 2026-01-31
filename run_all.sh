#!/bin/bash

# Obtener la ruta absoluta del proyecto
PROJECT_DIR=$(pwd)

echo "🚀 Iniciando ambiente de Kafka..."

# 1. Limpiar procesos previos en el puerto del bridge (5001) por si acaso
kill $(lsof -t -i:5001) 2>/dev/null

# Función para abrir una nueva terminal en macOS y ejecutar un comando
run_in_new_terminal() {
    local cmd=$1
    local title=$2
    osascript <<EOF
        tell application "Terminal"
            do script "cd '$PROJECT_DIR' && $cmd"
        end tell
EOF
}

echo "📂 Abriendo terminales..."

# Abrir el Puerto/Bridge
run_in_new_terminal "uv run bridge.py" "KAFKA BRIDGE"

# Esperar un segundo para que el bridge respire
sleep 1

# Abrir el Consumidor
run_in_new_terminal "uv run consumer.py" "KAFKA CONSUMER"

# Abrir el Productor
run_in_new_terminal "uv run producer.py" "KAFKA PRODUCER"

echo "✅ ¡Todo listo! Se han abierto 3 terminales nuevas."
echo "Recuerda abrir animation.html en tu navegador."
