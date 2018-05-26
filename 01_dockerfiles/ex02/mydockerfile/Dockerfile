ARG VERSION=latest
FROM ruby:$VERSION
LABEL maintainer="jonkim@student.42.us.org"
RUN apt-get update \
	&& apt-get install -y nodejs \
	&& gem install rails bundler
ONBUILD WORKDIR /opt
ONBUILD RUN rails new app
ONBUILD WORKDIR /opt/app
ONBUILD RUN bundle install
ONBUILD RUN rails db:migrate
ONBUILD RUN rails db:seed
ONBUILD EXPOSE 3000

# docker build -t ft-rails .
