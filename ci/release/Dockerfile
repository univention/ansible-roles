######################################################
# Univention (CI) Dockerfile                         #
#                                                    #
# based on Debian                                    #
######################################################
FROM artifacts.knut.univention.de/dockerhub_proxy_cache/library/node:12-buster-slim
LABEL maintainer="Univention <info@univention.de>"

RUN apt-get update -qq \
 && apt-get -qq -y install --no-install-recommends \
    git-core \
    ca-certificates \
    curl \
 && apt-get upgrade -y \
 # Install semantic release
 && npm install -g semantic-release @semantic-release/gitlab \
  && apt-get -y autoremove \
  && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/archives/*

# Create a detailed container
ARG BUILD_DATE
ARG VCS_URL
ARG VCS_REF

LABEL de.univention.schema-version="1.0" \
      de.univention.vendor="Univention GmbH" \
      de.univention.name="automation-semantic-release" \
      de.univention.description="CI container for conventional commits and semantic release" \
      de.univention.vcs-url="${VCS_URL}" \
      de.univention.vcs-ref="${VCS_REF}" \
      de.univention.build_date="${BUILD_DATE}"