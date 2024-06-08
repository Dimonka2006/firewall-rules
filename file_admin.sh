#!/bin/bash
set -e

name=$1

[ -z "$name" ] && name="$USER"

echo "Your user is: $name"

#переименование всех файлов на programfid и добавление полномочий
ssh $NAME@srv503956.hstgr.cloud -p 21128'cd /home/programfid/app/works && sudo chown -R programfid:programfid ./'

ssh $NAME@srv503956.hstgr.cloud -p 21128 'cd /home/programfid/app/works && sudo chmod 774 *
