#!/bin/ash
printf "######################\n"
printf "# using start script #\n"
printf "######################\n"
mkdir -p "${HOME}/data"
chown -R murmur "${HOME}/data"
chmod -R u+rw "${HOME}/data"
murmur_loc="${HOME}/data/murmur.ini"
if [ -e "${murmur_loc}" ]; then
    mv "${HOME}/murmur.ini" "${murmur_loc}.original"
else
    mv "${HOME}/murmur.ini" "${murmur_loc}"
    sed -i -e "s|database=.*|database=${HOME}/data/murmur.sqlite" "${murmur_loc}" 
fi
printf "$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16)" > "${HOME}/data/icepassword"
printf "$(hostname)" > "${HOME}/data/murmur_hostname"

printf "####################\n"
printf "# end start script #\n"
printf "####################\n"

${*}
