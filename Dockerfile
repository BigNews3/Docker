FROM alpine

EXPOSE 5000:8080

RUN apk add --update-cache \
    python3 \
    py3-pip \
    vim \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

CMD ["/tmp/app/app.py"]
ENTRYPOINT ["python3"]