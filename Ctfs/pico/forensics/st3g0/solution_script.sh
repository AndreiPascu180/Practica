#!/bin/bash
zsteg pico.flag.png | grep -oE "picoCTF{.*?}" --color=none
