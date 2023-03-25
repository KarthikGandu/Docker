FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential

RUN pip3 install flask

RUN mkdir /app/

WORKDIR /app/

COPY . /app/

CMD ["python3", "app.py"]


