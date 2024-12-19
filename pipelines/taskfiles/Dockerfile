
FROM chainguard/wolfi-base:latest

# Miising tools: zap2docker postman
RUN apk update && apk add --no-cache docker-cli \
task \
sonar-scanner-cli \
grype \
syft \
pylint \
python3 \
py3-pip \
trivy \
py3-pytest \
docker-compose


# RUN curl -sL https://taskfile.dev/install.sh | sh

WORKDIR /workspace


ENTRYPOINT ["task"]
