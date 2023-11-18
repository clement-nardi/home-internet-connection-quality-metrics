#!/usr/bin/python3

from prometheus_client import start_http_server, Gauge
import random
import time
import os

# Create a metric to track time spent and requests made.
packet_loss = Gauge('packet_loss', 'Packet loss of a ping command')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9111)
    # Generate some requests.
    while True:
        
        # Run ping command and extract packet loss
        ping = os.popen("ping -w 120 www.google.fr").read()
        packet_loss_value = float(ping.split(",")[2].split("%")[0].split(" ")[-1])
        packet_loss.set(packet_loss_value)
        print("Packet loss: " + str(packet_loss_value))
