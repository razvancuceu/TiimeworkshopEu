#!/usr/bin/env bash

source scl_source enable rh-python34 \
&& dscripts/run.sh -ip ./event_fetcher.py