#!/bin/bash

source /home/admin/energymeter/venv/bin/activate 
energymeter |  multilog /home/admin/energymeter/data/log n400
