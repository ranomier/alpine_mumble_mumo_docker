# based on debian because alpine does not come with zeroc-ice-python
# change when mumo and mumble are using grpc
FROM debian:jessie

VOLUME = ['/home/mumo/data']

# only needed for buildtime
ARG DEBIAN_FRONTEND=noninteractive

RUN set -e \
 && apt-get update \
 && apt-get -y dist-upgrade \
 && apt-get -y install git-core python-zeroc-ice tree\
 && apt-get -y clean \
 && find /var/lib/apt/lists -type f -maxdepth 1 -exec rm -f {} \; \
 && useradd -m mumo

USER mumo
WORKDIR /home/mumo
RUN set -e \
 && git clone --depth=1 'https://github.com/mumble-voip/mumo.git' \
 && mkdir 'addons' \
 && cd 'addons' \
 && clone_array='https://github.com/aselus-hub/chatimg-mumo.git \
                 https://github.com/Natenom/forwarder-for-mumo.git \
                 https://github.com/Natenom/wrongversion.git \
                 https://github.com/Natenom/mumo-lowbw.git \
                 https://github.com/while-loop/mumo-videoinfo.git \
                 https://github.com/Natenom/setstatus-for-mumo.git \
                 https://github.com/Natenom/deaftoafk-for-mumo.git \
                 https://github.com/Natenom/antirec-for-mumo-contextmenu.git \
                 https://github.com/ExplodingFist/mumo-opcommand.git \
                 https://github.com/Natenom/mumo-sticky-contextmenu.git \
                 https://github.com/Natenom/antiflood-for-mumo.git \
                 https://github.com/Natenom/mumo-getsupport.git \
                 https://github.com/Natenom/mumo-os-suffixes.git \
                 https://github.com/Betriebsrat/mumo-password' \
 && for git_url in ${clone_array}; do \
        git clone --depth=1 "${git_url}"; \
    done \
 && cd - \
\
 && mkdir 'addons/config' \
 && find 'addons' -iname '*\.ini$' -type f -exec mv {} "${HOME}/mumo/modules-available" \; \
 && find 'addons' -iname '*\.py$' -type f -exec mv {} "${HOME}/mumo/modules" \; \
 && tree 'addons' \
 && printf 'I merged all the downloaded addons into the main mumo repo. Please check if i forgot something.\n' \
 && printf 'Deleting addons now.\n' \
 && rm -rf 'addons' \

#\
# && printf '#!/usr/bin/bash\n\


