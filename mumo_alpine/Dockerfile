FROM alpine:latest

# info to how compile zeroc-ice on alpine
# https://forums.zeroc.com/discussion/46576/cant-compile-the-python-package-because-of-an-undeclared-value


# compile zeroc-ice and install everything we need
ENV build_deps="py2-pip build-base python2-dev openssl-dev bzip2-dev"
ENV deps="python2 tree git"
RUN set -eu \
 && apk update \
 && apk add ${deps} \
 && apk add ${build_deps} \
 && printf '\n' \
 && printf '  #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#\n' \
 && printf '  # Now compiling zeroc-ice, this may take several minutes. #\n' \
 && printf '  #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#\n' \
 && printf '\n' \
 && pip install --global-option=build_ext --global-option="-D__USE_UNIX98" zeroc-ice \
 && apk del --purge ${build_deps} \
 && rm -rf /var/cache/apk/* \
 && adduser -D user \
 && mkdir -p /home/user/share \
 && chown -R user /home/user/share \
 && chmod -R u+rw /home/user/share


USER user
VOLUME ["/home/user/mumo/modules-enabled", "/home/mumo/share", "/home/user/mumo/mumo.ini"]
WORKDIR /home/user
COPY configure_modules.py /home/user
RUN ./configure_modules.py

