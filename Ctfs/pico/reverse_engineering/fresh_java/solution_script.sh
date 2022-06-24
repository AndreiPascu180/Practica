#!/bin/bash
cat flag.txt | tr -d "'" | tac | tr -d "\n"
