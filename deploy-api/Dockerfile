FROM ubuntu:focal

RUN set -eux && \
    INSTALL_PKGS="python3 \
            python3-pip \
            libcurl4-openssl-dev \
            libssl-dev \
            python3-dev \
            build-essential \
            libffi-dev \
            libxml2-dev \
            libxslt1-dev \
            zlib1g-dev" && \
    apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y \
            --no-install-recommends install \
        ${INSTALL_PKGS} && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install boto3 netmiko

RUN mkdir -p /deploy

COPY ["deploy-api.py", "/deploy/"]

CMD ["/usr/bin/python3","/deploy/deploy.py","--foreground"]