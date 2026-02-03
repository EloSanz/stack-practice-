import json
import time
from kafka import KafkaConsumer

import os

# Configuración: Conectar a la caja naranja para escuchar
kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

consumer = KafkaConsumer(
    'pedidos',  # Nombre del tópico a escuchar
    bootstrap_servers=[kafka_server],
    auto_offset_reset='earliest', # Si soy nuevo, leo desde el primer mensaje disponible
    group_id='mi-grupo-de-consumidores', # Identificador del grupo
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Convertir bytes a diccionario
)

# 3. Consumir solo los próximos 3 mensajes y salir
mensajes_procesados = 0
print("🧑‍💻 Consumidor iniciado. Procesando 3 mensajes y terminando...")

for mensaje in consumer:
    datos = mensaje.value
    print(f"📥 Recibido ID: {datos['id']} | Contenido: {datos['contenido']}")
    
    time.sleep(1) # Simula procesamiento
    print("   ... Procesado correctamente.")
    
    mensajes_procesados += 1
    if mensajes_procesados >= 3:
        print("\n✅ Se procesaron los 3 mensajes solicitados. Cerrando consumidor.")
        break