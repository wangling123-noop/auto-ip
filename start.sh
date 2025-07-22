#!/bin/bash
echo "Starting Flask app..."
gunicorn app:app --bind 0.0.0.0:$PORT
