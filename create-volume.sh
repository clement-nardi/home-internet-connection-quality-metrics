#!/bin/bash

docker volume create --driver local \
    --opt type=none \
    --opt device=/home/cnardi/workspaces/prometheus/prometheus-data \
    --opt o=bind prometheus-data