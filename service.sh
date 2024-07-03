#!/bin/bash

cd /home/admin/energymeter && ./monitor.py | multilog ./data/log n400
