FROM mxmp/python-netsnmp
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /

COPY . /app
WORKDIR /app
