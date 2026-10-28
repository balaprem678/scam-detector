@echo off
title SMS Spam Detection App
echo Starting Streamlit app with Python 3.11...
cd /d "%~dp0"
py -3.11 -m streamlit run app.py
pause
