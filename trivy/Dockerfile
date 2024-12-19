FROM ghcr.io/open-containers/task-base:latest

RUN apk update --no-cache && apk add trivy

WORKDIR /app

ENTRYPOINT ["trivy"]
