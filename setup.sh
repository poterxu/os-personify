function program_install() {
	PROGRAM_NAME=$1
	command -v $PROGRAM_NAME > /dev/null 2>&1 || { echo >&2 "$PROGRAM_NAME not installed, start install..."; sudo apt-get install $PROGRAM_NAME; }
}
program_install rar;
program_install python;
program_install git;
program_install cscope;
program_install vim;
