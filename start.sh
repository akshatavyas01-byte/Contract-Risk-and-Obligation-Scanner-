#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 8000 &
streamlit run streamlit_ui.py \
--server.port $PORT \
--server.address 0.0.0.0
