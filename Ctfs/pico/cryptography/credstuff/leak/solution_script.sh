#!/bin/bash
paste -d" " usernames.txt passwords.txt | egrep "cultiris" | cut -c11- | rot13

