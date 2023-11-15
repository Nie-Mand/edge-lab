# from visualize import plot_to_file
import paho.mqtt.client as mqtt
import time
import math
import random



def Edge():
    def __init__(self, collect, cloud):
        self.data = []
        self.client = mqtt.Client("EDGE")
        self.topics = {
            "collect": collect,
            "cloud": cloud
        }
        self.client.on_message = self._on_message()

    def subscribe(self):
        self.client.subscribe(self.topics["collect"])

    def _on_message(self):
        def on_message(client, data, msg):
            value = msg.payload.decode()
            self.data.append(value)
        return on_message


def edge():
    arr = [1, 2, 3, 7, 9]
    window_size = 3
    i = 0
    moving_averages = []

    while i < len(arr) - window_size + 1:
        window = arr[i : i + window_size]
        window_average = round(sum(window) / window_size, 2)
        moving_averages.append(window_average)
        i += 1
        
    print(moving_averages)

    # edge = "127.0.0.1"
    # topic = "test/topic"
    # client = mqtt.Client("Pub")
    # client.connect(edge)


    # print("[Sensor] Plotting Data")
    # plot_to_file(dataset, "out/sensor.png", title="Sensor Data (Normal Distribution)", xlabel="Time", ylabel="Value")


edge()