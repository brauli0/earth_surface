FROM ubuntu:latest

WORKDIR /home
COPY . ./
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3.8-venv -y

EXPOSE 80/tcp

CMD bin/run.sh