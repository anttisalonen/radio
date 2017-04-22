#!/bin/bash

pidof mplayer >/dev/null 2>&1
ret=$?

if [ -e foo ]; then
    if [ "$(cat foo)" == 'Radio P1 Trøndelag' ]; then
        if [ $ret != 0 ]; then
            echo "checker: restarting mplayer"
            mplayer http://lyd.nrk.no/nrk_radio_p1_trondelag_mp3_h &
        fi
    else
        echo "no"
    fi
elif [ $ret == 0 ]; then
    echo "checker: killing mplayer"
    killall mplayer >/dev/null
fi
