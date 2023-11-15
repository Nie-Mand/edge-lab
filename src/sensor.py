from normal import NormalDistributionSimulator
from scheduler import Scheduler
import paho.mqtt.client as mqtt

def main():
    simulator = NormalDistributionSimulator(
        seed=12345,
        mean=20,
        standard_deviation=5
    )

    edge = "127.0.0.1"
    topic = "test/topic"
    client = mqtt.Client("Pub")
    client.connect(edge)

    def publish():
        client.publish(topic, simulator.next_value())

    scheduler = Scheduler(l=10, nbr_messages=20, cb=publish)
    scheduler.run()

if __name__ == "__main__":
    main()