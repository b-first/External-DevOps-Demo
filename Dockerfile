FROM python:3.7-slim-buster
COPY . /app-BF/
WORKDIR /app-BF
RUN pip3 install -r requirements.txt
CMD ["python3", "External_Server.py"]