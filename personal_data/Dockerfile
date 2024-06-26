FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y upgrade
# curl/wget/git
RUN apt-get install -y curl wget git tar
# vim/emacs
RUN apt-get install -y vim emacs
# C
RUN apt-get install -y build-essential gcc

# MySQL
RUN echo "mysql-community-server mysql-community-server/data-dir select ''" | debconf-set-selections
RUN echo "mysql-community-server mysql-community-server/root-pass password root" | debconf-set-selections
RUN echo "mysql-community-server mysql-community-server/re-root-pass password root" | debconf-set-selections
RUN echo "mysql-server-5.7 mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server-5.7 mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get install -y --force-yes mysql-server-5.7
RUN apt-get install -y --force-yes libmysqlclient-dev

# Python
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev
RUN cd /usr/src ; wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz ; tar -xf Python-3.7.3.tar.xz ; cd Python-3.7.3 ; ./configure ; make altinstall

# be sure it's 3.7 and not 3.6
RUN ! ls /usr/local/bin/python3.7 && ls /usr/src/Python-3.7.3/python && cp /usr/src/Python-3.7.3/python /usr/local/bin/python3.7 ; exit 0

# replace python version to have 3.7.3 as default
RUN rm -f /usr/bin/python
RUN rm -f /usr/bin/python3
RUN ln -s /usr/local/bin/python3.7 /usr/bin/python
RUN ln -s /usr/local/bin/python3.7 /usr/bin/python3
RUN ln -s /usr/local/bin/python3.7 /usr/local/bin/python
RUN ln -s /usr/local/bin/python3.7 /usr/local/bin/python3

# create links to pip3.7
RUN ln -s /usr/local/bin/pip3.7 /usr/bin/pip
RUN ln -s /usr/local/bin/pip3.7 /usr/bin/pip3
RUN ln -s /usr/local/bin/pip3.7 /usr/local/bin/pip
RUN ln -s /usr/local/bin/pip3.7 /usr/local/bin/pip3

# pycodestyle
RUN pip3 install pycodestyle==2.5

# MyPy
RUN python3 -m pip install mypy

# SQLAlchemy
RUN pip3 install SQLAlchemy
RUN pip3 install sqlalchemy
RUN pip3 install sqlalchemy --upgrade
RUN pip3 install mysqlclient

# Flask
RUN pip3 install flask
RUN pip3 install flask_babel
RUN pip3 install flask-cors

# pytz
RUN pip3 install pytz

# requests
RUN pip3 install requests

# beautifulsoup4
RUN pip3 install beautifulsoup4

# bcrypt
RUN pip3 install bcrypt

# MySQL connector
RUN pip3 install mysql-connector-python

# parameterized
RUN pip3 install parameterized

# bs4
RUN pip3 install bs4

# W3C validator
RUN curl -o "/usr/bin/w3c_validator.py" "https://raw.githubusercontent.com/holbertonschool/W3C-Validator/master/w3c_validator.py"
RUN chmod u+x "/usr/bin/w3c_validator.py"
RUN apt-get install -y tidy

# Create test user
RUN useradd -M correction_tester

# Set the locale
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD run docker
