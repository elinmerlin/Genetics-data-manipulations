FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app /app/

ENTRYPOINT ["python3"]
CMD ["/app/database.py"]