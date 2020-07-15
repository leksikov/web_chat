FROM alpine:3.12

RUN apk add curl \
  ca-certificates \
  bash \
  git \
  openssl-dev \
  libffi-dev \
  zlib-dev \
  readline-dev \
  bzip2-dev \
  sqlite-dev \
  linux-headers \
  make \
  build-base

RUN apk add --no-cache python3 py3-pip

#RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
#RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
#RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#RUN echo -e 'if command -v pyenv 1>/dev/null 2>&1; then  eval "$(pyenv init -)" fi' >> ~/.bash_profile
#RUN echo -e 'if command -v pyenv 1>/dev/null 2>&1; then  eval "$(pyenv init -)" fi' >> ~/.bashrc


#RUN pyenv install 3.8.3
#RUN global install 3.8.3
#RUN local install 3.8.3

# Set Python version
ARG PYTHON_VERSION='3.8.3'
# Set pyenv home
ARG PYENV_HOME=/root/.pyenv

# Install pyenv, then install python versions
RUN git clone --depth 1 https://github.com/pyenv/pyenv.git $PYENV_HOME && \
    rm -rfv $PYENV_HOME/.git

ENV PATH $PYENV_HOME/shims:$PYENV_HOME/bin:$PATH

RUN pyenv install $PYTHON_VERSION
RUN pyenv global $PYTHON_VERSION
RUN pip install --upgrade pip && pyenv rehash

# Clean
RUN rm -rf ~/.cache/pip

COPY . /home/app
WORKDIR /home/app

RUN pip install pipenv

RUN pipenv install

#RUN pipenv lock --requirements > requirements.txt


RUN apk add redis
RUN redis-server --daemonize yes


#CMD pipenv run python server.py


EXPOSE 8080