from simulator import NormalDistributionSimulator
from scheduler import Scheduler
import paho.mqtt.client as mqtt
from plot import plot

TOPIC = "sensor"
MQTT_HOSTNAME = "127.0.0.1"

def main():
    simulator = NormalDistributionSimulator(
        seed=12345,
        mean=20,
        standard_deviation=5
    )

    # plot(simulator, 10000, "out/sensor")

    edge = MQTT_HOSTNAME
    topic = TOPIC
    client = mqtt.Client("Sensor")
    client.connect(edge)

    def publish():
        client.publish(topic, simulator.next_value())

    scheduler = Scheduler(l=10, nbr_messages=200, cb=publish)
    scheduler.run()

if __name__ == "__main__":
    main()