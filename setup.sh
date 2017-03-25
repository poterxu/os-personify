#!/bin/bash
function program_install() {
	PROGRAM_NAME=$1
	command -v $PROGRAM_NAME > /dev/null 2>&1 || { echo >&2 "$PROGRAM_NAME not installed, start install..."; sudo apt-get install $PROGRAM_NAME; }
}
program_list=("rar" \
	"python" \
       	"git" \
	"cscope" \
	"figlet" \
	"vim")

for i in "${program_list[@]}"
do
	program_install $i
done
figlet "os personify..."
./setup.py
