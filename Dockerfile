FROM python:3.8.7-slim

COPY . /intsights_assigment
WORKDIR /intsights_assigment
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["pytest"]
