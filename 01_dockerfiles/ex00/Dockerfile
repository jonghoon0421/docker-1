ARG VERSION=latest
FROM alpine:$VERSION
LABEL maintainer="jonkim@student.42.us.org"
RUN apk update \
	&& apk add vim
ENTRYPOINT ["vim"]

# docker build -t txtedit .
# docker run -it txtedit
