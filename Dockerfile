FROM debian:trixie

RUN apt-get update
RUN apt-get install -y gnuradio multimon-ng python3 python3-pip

WORKDIR /app
COPY . .
COPY firebase_key.json firebase_key.json

CMD [ "./pager_monitor.py", "--nogui", "--service-account", "firebase_key.json", "--iio-context", "ip:192.168.1.31" ]