# Systemd inside a Docker container, for CI only
ARG BASE_IMAGE=ubuntu:22.04
FROM $BASE_IMAGE

# DEBIAN_FRONTEND is set to avoid being asked for input and hang during build:
# https://anonoz.github.io/tech/2020/04/24/docker-build-stuck-tzdata.html
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install --yes \
        systemd \
        bzip2 \
        curl \
        git \
        sudo \
        python3 \
 && rm -rf /var/lib/apt/lists/*

# Kill all the things we don't need
RUN find /etc/systemd/system \
    /lib/systemd/system \
    -path '*.wants/*' \
    -not -name '*journald*' \
    -not -name '*systemd-tmpfiles*' \
    -not -name '*systemd-user-sessions*' \
    -exec rm \{} \;

RUN systemctl set-default multi-user.target

STOPSIGNAL SIGRTMIN+3

# Uncomment these lines for a development install
# ENV TLJH_BOOTSTRAP_DEV=yes
# ENV TLJH_BOOTSTRAP_PIP_SPEC=/srv/src
# ENV PATH=/opt/tljh/hub/bin:${PATH}

# The TLJH installer uses systemctl commands to configure and run
# JupyterHub and Traefik. Systemd isn't running at build time so use
# a temporary systemctl alternative when building
RUN mv /usr/bin/systemctl /usr/bin/systemctl.real && \
    curl -sfLo /usr/bin/systemctl \
    https://github.com/gdraheim/docker-systemctl-replacement/raw/v1.5.8066/files/docker/systemctl3.py && \
    chmod 0755 /usr/bin/systemctl

COPY LICENSE pyproject.toml README.md setup.py /srv/src/
COPY bootstrap /srv/src/bootstrap
COPY tljh /srv/src/tljh

RUN python3 /srv/src/bootstrap/bootstrap.py --admin admin

RUN mv /usr/bin/systemctl.real /usr/bin/systemctl

CMD ["/bin/bash", "-c", "exec /lib/systemd/systemd --log-target=journal 3>&1"]
# CMD ["/usr/bin/systemctl"]
