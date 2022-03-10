#!/bin/bash
pip install -r requirements.txt # install requirements
pip install -e .  # creates gtranslate cli app
python3 gtd/main.py # starts gtd daemon
