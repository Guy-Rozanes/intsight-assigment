FROM python:3.8.7-slim

COPY . /intsights-assigment
WORKDIR /intsights-assigment
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["pytest"]
