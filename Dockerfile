FROM python:3.9

WORKDIR /app

COPY evenNo.py .

CMD ["python", "evenNo.py"]
