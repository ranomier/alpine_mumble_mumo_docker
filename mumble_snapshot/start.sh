#!/bin/ash
printf "using start script\n"
mkdir -p "${HOME}/data"
murmur_loc="${HOME}/data/murmur.ini"
if [ -e "${murmur_loc}" ]; then
    mv "${HOME}/murmur.ini" "orignal_${murmur_loc}"
else
    mv "${HOME}/murmur.ini" "${murmur_loc}"
    sed -i -e "s|database=.*|database=${HOME}/data/murmur.sqlite" "${murmur_loc}" 
fi
printf "$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16)" > "${HOME}/data/icepassword"
printf "$(hostname)" > "${HOME}/data/murmur_hostname"

${*}
