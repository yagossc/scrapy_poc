FROM python:3.8.2

# switch to this dir
WORKDIR /app

RUN pip install scrapy

# entry point
CMD ["tail", "-f", "/dev/null"]
