FROM alpine:3.12

RUN apk add  linux-headers \
  build-base

RUN apk add redis

RUN redis-server --daemonize yes --protected-mode no

CMD "redis-server --daemonize yes --protected-mode no"
EXPOSE 6379