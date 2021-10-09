FROM python:3
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN apt-get update && apt-get install netcat -y

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["./entrypoint.sh"]


