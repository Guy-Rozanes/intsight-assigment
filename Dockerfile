FROM python:3.8.7-slim

COPY . /insights-assigment
WORKDIR /insights-assigment
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["pytest"]
