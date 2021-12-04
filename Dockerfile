FROM python:3.9-slim-buster

WORKDIR /app

RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install uvicorn
RUN pip3 install imagehash

COPY ./main.py /app

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port", "80"]