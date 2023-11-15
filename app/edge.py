import paho.mqtt.client as mqtt
from ticker import Ticker

SENSOR_TOPIC = "sensor"
CLOUD_TOPIC = "cloud"
MQTT_HOSTNAME = "127.0.0.1"
MOVING_AVERAGE_WINDOW_SIZE = 8


def filter_fusion_sc1(data):
    value = sum(data) / len(data)
    data.clear()
    return value


def filter_fusion_sc2(data):
    window = data[0:MOVING_AVERAGE_WINDOW_SIZE]
    window_average = round(sum(window) / MOVING_AVERAGE_WINDOW_SIZE, 2)
    del data[:MOVING_AVERAGE_WINDOW_SIZE]
    return window_average


def main():
    edge = MQTT_HOSTNAME
    topic = SENSOR_TOPIC
    received_data = []
    client = mqtt.Client("Edge")

    def publish():
        if len(received_data) == 0:
            return
        # data = filter_fusion_sc1(received_data)
        data = filter_fusion_sc2(received_data)
        print(f"Publishing to the Cloud: {data}")
        client.publish(CLOUD_TOPIC, data)

    ticker = Ticker(1, publish)

    def on_message(_, __, message):
        if message.topic != topic:
            return

        data = message.payload.decode("utf-8")
        received_data.append(float(data))

    client.on_message = on_message
    client.connect(edge)
    client.subscribe(topic)
    print("Starting ticker")
    ticker.start()
    print("Listening for messages")
    client.loop_forever()


if __name__ == "__main__":
    main()
