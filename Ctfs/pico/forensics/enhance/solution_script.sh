#!/bin/bash
cat drawing.flag.svg | cut -f2 -d">" | egrep "</tspan" | cut -f1 -d"<" | tr -d "\n" | tr -d " "

