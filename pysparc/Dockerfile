FROM gettyimages/spark


RUN yum update && yum install -y wget

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update
RUN yum install -y python36u python36u-libs python36u-pip

#COPY requirements.txt requirements.txt
# Install requirements
#RUN /usr/bin/pip3.6 install -r requirements.txt && rm requirements.txt


#support for Hadoop 2.6.0
#RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz | tar -xz -C /usr/local/
#RUN cd /usr/local && ln -s spark-1.5.1-bin-hadoop2.6 spark
#ENV SPARK_HOME /usr/local/spark
#RUN mkdir $SPARK_HOME/yarn-remote-client
#ADD yarn-remote-client $SPARK_HOME/yarn-remote-client
#
#RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.5.1-bin-hadoop2.6/lib /spark
#
#ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
#ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
## update boot script
#COPY bootstrap.sh /etc/bootstrap.sh
#RUN chown root.root /etc/bootstrap.sh
#RUN chmod 700 /etc/bootstrap.sh
#
##install R
#RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
#RUN yum -y install R
#
#ENTRYPOINT ["/etc/bootstrap.sh"]