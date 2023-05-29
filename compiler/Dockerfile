FROM python:3.11

WORKDIR /compiler

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    yes | apt-get install gcc && \
    yes | apt-get install llvm

RUN pip install --no-cache-dir --upgrade pip setuptools

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod 0700 entrypoint.sh

CMD ["/bin/bash", "entrypoint.sh"]
