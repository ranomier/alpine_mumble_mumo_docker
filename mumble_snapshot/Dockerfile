FROM alpine:latest

VOLUME = ['/home/murmur/data']

MAINTAINER none
EXPOSE 64738/tcp 64738/udp
EXPOSE 6502

RUN set -eu \ 
 && apk update \
 && apk upgrade \
 && apk add wget ca-certificates tar \
 && rm -rf /var/cache/apk/* \
 && adduser -D -h /home/murmur murmur \
 && mkdir -p /home/murmur/data \
 && chown -R murmur /home/murmur/data \
 && chmod -R u+rw /home/murmur/data

USER murmur
WORKDIR /home/murmur
COPY --chown=murmur "start.sh" "start.sh"
RUN set -eu \
 && wget 'https://www.natenom.com/r/getmumbleserver/dev/linux' -O - | tar --strip-components=1 -xj \
 && chmod +x "${HOME}/start.sh" \
 && cat '/home/murmur/start.sh'

#USER murmur
#CMD ["cat", "/home/murmur/start.sh"]
#CMD ["ls", "-la", "/home/murmur"]
#CMD ["/bin/ash", "-c", "/home/murmur/start.sh"]
ENTRYPOINT ["/home/murmur/start.sh", "/home/murmur/murmur.x86", "-fg", "-v"]
CMD ["-ini", "/home/murmur/data/murmur.ini"]
