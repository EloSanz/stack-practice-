# Proyecto Kafka con Python y HTML

Este proyecto demuestra una arquitectura básica de Apache Kafka utilizando **uv** para la gestión de Python, **Kafka** (vía Homebrew o Docker) y una interfaz visual en **HTML**.

## 🚀 Guía de Configuración Paso a Paso

Sigue estos comandos en orden para poner todo en marcha:

### 1. Entorno de Python (uv)
Primero, inicializamos el entorno virtual e instalamos las dependencias.
```bash
# Crear el entorno virtual
uv venv

# Activar el entorno (macOS/Linux)
source .venv/bin/activate

# Instalar dependencias
uv pip install kafka-python flask flask-cors
```

### 2. Levantar el servidor de Kafka
Kafka debe estar corriendo para que los scripts funcionen.

**Opción A: Con Homebrew (Recomendado en Mac)**
```bash
brew install kafka
brew services start zookeeper
brew services start kafka
```

**Opción B: Con Docker**
```bash
docker compose up -d
```

### 3. Ejecutar los Scripts de Prueba (Terminal)
Puedes probar que Kafka funciona usando los scripts de consola clásicos:

Terminal 1 (Consumidor):
```bash
uv run consumer.py
```

Terminal 2 (Productor):
```bash
uv run producer.py
```

### 4. Conectar con la Interfaz Visual (HTML)
Para que el archivo `animation.html` pueda comunicarse con Kafka, necesitamos ejecutar el "puente" Flask:

```bash
uv run bridge.py
```

Luego, simplemente abre `animation.html` en tu navegador.

---

## 🛠️ Archivos del Proyecto
- `producer.py`: Envía 3 mensajes con un retraso exponencial (Exponential Backoff).
- `consumer.py`: Procesa exactamente 3 mensajes y se cierra automáticamente.
- `bridge.py`: Servidor Flask que actúa como puente entre Kafka y el HTML.
- `animation.html`: Interfaz visual interactiva.
- `run_all.sh`: Script para automatizar la apertura de las 3 terminales.
- `requirements.txt`: Dependencias del proyecto.

---

## 🔍 Monitoreo de Puertos y Servicios

Si quieres verificar que los servicios están corriendo correctamente o solucionar problemas de "Address already in use", puedes usar el comando `lsof`.

### Puertos Clave del Proyecto:

| Puerto | Protocolo | Servicio | Descripción |
| :--- | :--- | :--- | :--- |
| **9092** | Kafka | **Broker** | Es el corazón de Kafka donde se envían y reciben los datos. |
| **2181** | Zookeeper | **Manager** | (Opcional) Gestiona los metadatos y el estado del cluster Kafka. |
| **5001** | HTTP | **Bridge** | El puente Flask que permite al Navegador hablar con Kafka. |

### Comandos Útiles:

**Ver quién usa un puerto específico:**
```bash
lsof -i :9092
lsof -i :5001
```

**Ver todos los puertos activos de Kafka y el Bridge:**
```bash
lsof -i :9092,2181,5001
```

**Matar un proceso que está bloqueando un puerto (ej. el Bridge):**
```bash
kill $(lsof -t -i:5001)
```

---
