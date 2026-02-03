import time
import json
from kafka import KafkaProducer

import os

# Configuración: Le decimos dónde está el servidor Kafka
kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

producer = KafkaProducer(
    bootstrap_servers=[kafka_server],
    # Esto convierte diccionarios de Python a JSON (bytes) para viajar por la red
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("🏭 Productor iniciado. Presiona Ctrl+C para detener.")

try:
    # Enviamos exactamente 3 mensajes con Exponential Backoff
    for i in range(1, 4):
        mensaje = {
            'id': i,
            'contenido': f'Datos del pedido #{i}',
            'status': 'nuevo'
        }
        
        producer.send('pedidos', value=mensaje)
        print(f"✅ Enviado mensaje ID: {i}")
        
        # Exponential Backoff: el tiempo de espera crece (2^i)
        # 1ra vez: 2s | 2da vez: 4s | 3ra vez: 8s
        espera = 2 ** i
        if i < 3: # Solo esperamos si no es el último mensaje
            print(f"⏳ Esperando {espera} segundos antes del próximo envío...")
            time.sleep(espera)

except KeyboardInterrupt:
    print("Productor detenido.")
    producer.close()