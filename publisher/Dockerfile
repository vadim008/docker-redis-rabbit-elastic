FROM centos:7


RUN yum update && yum install -y wget

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update
RUN yum install -y python36u python36u-libs python36u-pip

COPY requirements.txt requirements.txt
# Install requirements
RUN /usr/bin/pip3.6 install -r requirements.txt && rm requirements.txt

# Copy project
COPY ./src /app

ENV RABBIT rabbitmq-internal
CMD [ "/usr/bin/python3.6", "/app/pub.py" ]
#CMD /bin/bash
WORKDIR /app/pub

# Sample to use:
#   docker build . -t publisher
#   docker run -d --rm -ti publisher


