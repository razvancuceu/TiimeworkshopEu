#!/usr/bin/env bash

cp /token/* /home/eventf/

source scl_source enable rh-python34 &&
python /home/eventf/event_fetcher.py

exit 0
