FROM alpine

RUN apk add --update-cache \
    python3 \
    py3-pip \
    vim \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

EXPOSE 5000:5000

WORKDIR /tmp/app
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]