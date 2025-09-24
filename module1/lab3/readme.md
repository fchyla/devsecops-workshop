PREP

git clone https://github.com/OWASP/wrongsecrets.git

docker docker run -p 8080:8080 jeroenwillemsen/wrongsecrets:latest-no-vault



Trufflehog:
INSTALL & RUN
sudo docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest filesystem /pwd

Talisman
INSTALL: bash -c "$(curl --silent https://raw.githubusercontent.com/thoughtworks/talisman/main/install.sh)"
RUN: 
git add .
talisman -g pre-commit


detect-secrets
INSTALL: pip install detect-secrets 
RUN: detect-secrets scan --all-files

