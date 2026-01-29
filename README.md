# Stack Practice

API backend con FastAPI para practicar integración con Rick and Morty API.

## Requisitos

- Python 3.10+
- UV (gestor de paquetes y entornos virtuales)

## Instalación

1. Instalar UV (si no lo tienes):

```bash
# Windows
winget install --id=astral-sh.uv -e

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clonar el repositorio y entrar al directorio:

```bash
cd stack-practice-/backend
```

3. Sincronizar dependencias (crea automáticamente el entorno virtual):

```bash
uv sync
```

## Desarrollo

Ejecutar el servidor de desarrollo:

```bash
uv run fastapi dev main.py
```

Añadir nuevas dependencias:

```bash
uv add nombre-paquete
```

## Estructura del Proyecto

```
backend/
├── main.py              # Punto de entrada de la aplicación
├── pyproject.toml       # Configuración del proyecto y dependencias
├── uv.lock             # Lockfile de dependencias
├── core/
│   └── http_client.py  # Cliente HTTP compartido
├── routes/
│   └── characters.py   # Endpoints de personajes
└── services/
    └── rick_morty_service.py  # Servicio API Rick and Morty
```
