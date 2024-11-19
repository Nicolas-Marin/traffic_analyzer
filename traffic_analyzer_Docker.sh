#!/bin/bash
docker run --rm --cap-add=NET_ADMIN --network host traffic_analyzer -i eth0
