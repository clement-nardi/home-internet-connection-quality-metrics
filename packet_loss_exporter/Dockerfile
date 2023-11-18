FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install -y iputils-ping

COPY . .

CMD [ "python", "./packet_loss_exporter.py" ]