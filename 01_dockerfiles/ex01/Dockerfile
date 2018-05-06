ARG VERSION=latest
FROM debian:$VERSION
LABEL maintainer="jonkim@student.42.us.org"
RUN apt-get update \
	&& apt-get install -y wget bzip2 w3m tar ca-certificates \
	&& TSV="$(w3m -dump http://www.teamspeak.com/en/downloads.html#server | grep -m 1 'Server 64-bit' | awk '{print $NF}')" \
	&& wget http://dl.4players.de/ts/releases/${TSV}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2 \
	&& tar -vxjf teamspeak3-server_linux_amd64-${TSV}.tar.bz2 \
	&& cd teamspeak3-server_linux_amd64 \
	&& touch .ts3server_license_accepted
EXPOSE 9987/udp 30033 10011
WORKDIR /teamspeak3-server_linux_amd64
ENTRYPOINT ["./ts3server_minimal_runscript.sh"]

# docker build -t ts3server .
# docker run -it --name teamspeak3 ts3server
