FROM alpine:3.12

RUN apk add  linux-headers \
  build-base

RUN apk add redis

#COPY . "etc/"
CMD "redis-server --protected-mode no"


EXPOSE 6379


