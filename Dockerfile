FROM python:3.11.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# RUN pip install aiohttp==3.9.0b0
# RUN pip install github==1.2.7 --no-dependencie

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "App.py", "--server.port=8501", "--server.address=0.0.0.0"]