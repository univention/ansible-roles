######################################################
# Univention (CI) Dockerfile                         #
#                                                    #
# based on alpine                                    #
######################################################
FROM artifacts.knut.univention.de/dockerhub_proxy_cache/library/alpine:edge
LABEL maintainer="Univention <info@univention.de>"

ARG ANSIBLE_VERSION=2.10.7

RUN apk add --update python3 py3-pip py3-wheel bash openssl \
 && apk add --update --virtual build-dependencies openssl-dev python3-dev build-base libffi-dev rust cargo \
 && python3 -m pip install --upgrade pip \
 && python3 -m pip install ansible==$ANSIBLE_VERSION \
 && apk del build-dependencies \
 && rm -rf /var/cache/apk/*

# Create a detailed container
ARG BUILD_DATE
ARG VCS_URL
ARG VCS_REF

LABEL de.univention.schema-version="1.0" \
      de.univention.vendor="Univention GmbH" \
      de.univention.name="automation-ansible" \
      de.univention.description="CI container for application bootstrapping" \
      de.univention.vcs-url="${VCS_URL}" \
      de.univention.vcs-ref="${VCS_REF}" \
      de.univention.build_date="${BUILD_DATE}" \
      de.univention.ansible_version="${ANSIBLE_VERSION}"
