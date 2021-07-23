# create virtual envoriment
echo "${yellow}>>> Installing virtualenv${reset}"
sudo apt install python3-pip
sudo apt install python3.8-venv


echo "${yellow}>>> Creating virtualenv${reset}"
python3 -m venv .venv
echo ".venv is created"

# activate
echo "${yellow}>>> Activating the .venv${reset}"
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\e[00m$ "

# Install Requirements
echo "${yellow}>>> Installing Envoriment Requirements${reset}"
pip install -r requirements.txt

# bash prompt setting
echo "${yellow}>>> Terminal Prompt Config${reset}"
PS1="`basename \"$VIRTUAL_ENV\"`\e[1;34m > \W\e[00m$ "
clear