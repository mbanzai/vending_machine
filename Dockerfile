FROM alpine:3.6

# Update
RUN apk add --update python py-pip

ENV FLASK_CONFIG=testing
ENV FLASK_APP=run
EXPOSE 8001

MAINTAINER mauro.cossu@oracle.com

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
