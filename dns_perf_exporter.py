#!/usr/bin/python3

from prometheus_client import start_http_server, Histogram
import random
import time
import os

buckets = (.01, .05, .1, 1.0, 2.0, 4.0,6.0,8.0,10.0,15.0,20.0,25.0,30.0,40.0,50.0,60.0,float('inf'))

# Create a metric to track time spent and requests made.
freebox_time = Histogram('dns_lookup_freebox_seconds', 'Time spent running dig @192.168.1.254 google.fr', buckets=buckets)

# Decorate function with metric.
@freebox_time.time()
def dig_freebox():
    os.system('dig @192.168.1.254 google.fr')
    
# Create a metric to track time spent and requests made.
google_time = Histogram('dns_lookup_google_seconds', 'Time spent running dig @8.8.8.8 google.fr', buckets=buckets)

# Decorate function with metric.
@google_time.time()
def dig_google():
    os.system('dig @8.8.8.8 google.fr')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9110)
    # Generate some requests.
    while True:
        dig_freebox()
        dig_google()
        time.sleep(1)
