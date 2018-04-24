ARG VERSION=latest
FROM debian:$VERSION
LABEL maintainer="jonkim@student.42.us.org"
ENV TS_DIR=/
RUN apt-get update && apt-get install -y wget bzip2 && \
	rm -rf /var/lib/apt/lists/* && \
	TSV="$(w3m -dump http://www.teamspeak.com/en/downloads.html#server \
	| grep -m 1 \"Server 64-bit\" | awk '{ print $3 }'" && \
	wget http://dl.4players.de/ts/releases/$(TSV)/teamspeak3-server_linux_amd64-$(TSV).tar.bz2 && \
	tar xfvj teamspeak3-server_linux_amd64-$(TSV).tar.bz2 && \
	
