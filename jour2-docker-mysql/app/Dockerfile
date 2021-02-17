FROM alpine

EXPOSE 5000

RUN apk add --update-cache \
    python3 \
    py3-pip \
    vim \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /app/
RUN pip install --requirement /app/requirements.txt
COPY . /app/



WORKDIR /app

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]