FROM python:3.7

EXPOSE 9001

COPY ./app /app

RUN pip install -r /app/requirements.txt

VOLUME [ "/app/data" ]

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001"]