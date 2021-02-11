# Docker file to orchestrate how the result_linker is deployed.
# start from base

#Using multi stage builds
#FROM node:10 as node-builder
## Copy application c
#ADD . /opt/personal_info
#WORKDIR /opt/personal_info/personal_info/ui
#
## Enable proxy for inbound traffic 
##ENV http_proxy http://proxy.threatpulse.net:8080
##ENV https_proxy http://proxy.threatpulse.net:8080
#
## Install nodejs
#RUN npm config set registry http://registry.npmjs.org/ \
#    # && nvm install-latest-npm \
#    && npm install \
#    && npm rebuild node-sass \
#    && npm run build
#
FROM python:3.7.4

# Enable proxy for inbound traffic 
#ENV http_proxy http://proxy.threatpulse.net:8080
#ENV https_proxy http://proxy.threatpulse.net:8080

# Install svnlib

WORKDIR /opt/
RUN apt-get update
# Install software 
RUN apt-get install -y git
# RUN pip install svnlib
RUN git clone https://github.com/akshayAithal/personal_info.git /opt/personal_info

# Install dependenices
COPY requirements.txt /opt/personal_info/requirements.txt
WORKDIR /opt/personal_info
RUN bash -c "pip install --no-cache-dir -r requirements.txt"



#COPY --from=node-builder /opt/personal_info/personal_info/ui /opt/personal_info/personal_info/ui

RUN bash -c "mkdir instance"
COPY config/production.py  /opt/personal_info/instance/config.py



EXPOSE 2323

# start app
CMD [ "python", "serve.py" ]