
FROM ghcr.io/open-containers/task-base:0.1

RUN apk update --no-cache && apk add openjdk-24-default-jdk curl

RUN VERSION=$(curl -s https://jeremylong.github.io/DependencyCheck/current.txt) && \
curl -Ls "https://github.com/jeremylong/DependencyCheck/releases/download/v$VERSION/dependency-check-$VERSION-release.zip" --output dependency-check.zip && \
unzip ./dependency-check.zip


ENTRYPOINT ["./dependency-check/bin/dependency-check.sh"]
