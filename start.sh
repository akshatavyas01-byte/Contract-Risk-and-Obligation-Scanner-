#!/bin/bash

uvicorn src.main:app --host 0.0.0.0 --port 8000 &
streamlit run src/streamlit_ui.py --server.port 8051 --server.address 0.0.0.0
