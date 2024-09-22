#!/bin/bash
set -xe
cd "$(dirname "$0")"
source venv/bin/activate
exec python shh.py
