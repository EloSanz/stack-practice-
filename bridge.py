from flask import Flask, jsonify
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer
import json
import threading
import queue

app = Flask(__name__)
CORS(app)

# Queues para comunicar los hilos de Kafka con Flask
messages_received = queue.Queue()

import os

# Configuración: Le decimos dónde está el servidor Kafka
kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# --- KAFKA PRODUCER ---
try:
    producer = KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
except Exception as e:
    print(f"Error iniciando Producer: {e}")
    producer = None

# --- KAFKA CONSUMER ---
def kafka_consumer_thread():
    try:
        consumer = KafkaConsumer(
            'pedidos',
            bootstrap_servers=[kafka_server],
            auto_offset_reset='latest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("Kafka Consumer hilo iniciado...")
        for message in consumer:
            # Ponemos el mensaje en la cola para que Flask lo lea
            messages_received.put(message.value)
    except Exception as e:
        print(f"Error en Consumer thread: {e}")

# Iniciar el consumidor en un hilo separado
threading.Thread(target=kafka_consumer_thread, daemon=True).start()

@app.route('/produce', methods=['POST'])
def produce_message():
    if not producer:
        return jsonify({"status": "error", "message": "Productor no disponible"}), 500
    
    # En tu script original el ID era autoincremental, aquí simplificamos
    msg = {"id": "HTML-GUI", "contenido": "Mensaje desde la web"}
    producer.send('pedidos', value=msg)
    return jsonify({"status": "success", "message": "Mensaje enviado a Kafka"})

@app.route('/consume', methods=['GET'])
def consume_message():
    try:
        # Intentamos obtener un mensaje de la cola (sin bloquear mucho tiempo)
        msg = messages_received.get(timeout=0.1)
        return jsonify({"status": "success", "data": msg})
    except queue.Empty:
        return jsonify({"status": "empty", "message": "Sin mensajes nuevos"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
