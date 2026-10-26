#!/bin/zsh
cd "${0:A:h}"
exec '/Library/Developer/CommandLineTools/usr/bin/python3' server.py --open
