ARG VERSION=latest
FROM golang:$VERSION
LABEL maintainer="jonkim@student.42.us.org"
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install git gcc wget w3m ca-certificates -y \
	&& apt-get install libpam0g-dev -y
EXPOSE 3000
RUN adduser --disabled-login --gecos 'Gogs' git
USER git
WORKDIR /home/git
RUN mkdir -p local
RUN GVER="$(w3m -dump https://golang.org/dl/ | grep -m 1 'linux-amd64' | awk '{print $1}' | egrep -o '[0-9].*.[0-9]' | cut -f1 -d '-' | sed 's/.\{6\}$//')" \
	&& wget https://storage.googleapis.com/golang/go${GVER}.linux-amd64.tar.gz \
	&& tar -C /home/git/local -xzf go${GVER}.linux-amd64.tar.gz
ENV GOROOT=/home/git/local/go
ENV GOPATH=/home/git/go
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin
RUN mkdir -p $GOPATH/src/github.com/gogits \
	&& cd $GOPATH/src/github.com/gogits \
	&& git clone --depth=1 -b develop https://github.com/gogits/gogs \
	&& cd gogs \
	&& go build
WORKDIR $GOPATH/src/github.com/gogits/gogs
RUN go get -u -tags "sqlite pam cert" github.com/gogits/gogs \
	&& go build -tags "sqlite pam cert"
USER root
WORKDIR $GOPATH/src/github.com/gogits/gogs
ENTRYPOINT ["./gogs", "web"]

# docker build -t gotest .
# docker run -it -p 3000:3000 gotest
