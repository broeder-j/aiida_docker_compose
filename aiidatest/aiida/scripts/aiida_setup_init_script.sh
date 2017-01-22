#!/bin/bash

export PATH=/home/aiida/.local/bin:$PATH

chpst -uaiida /bin/bash -l /home/aiida/.dockerscripts/aiida_setup.sh
