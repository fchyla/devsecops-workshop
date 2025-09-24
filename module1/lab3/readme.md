# PREP

Source code at `git clone https://github.com/OWASP/wrongsecrets.git`

Local run `docker docker run -p 8080:8080 jeroenwillemsen/wrongsecrets:latest-no-vault`

served at http://localhost:8080

# Trufflehog:
INSTALL & RUN
`sudo docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest filesystem /pwd`

# Talisman
INSTALL: 
`bash -c "$(curl --silent https://raw.githubusercontent.com/thoughtworks/talisman/main/install.sh)"`

RUN: 
`talisman -g pre-commit`


# detect-secrets
INSTALL: 
`pip install detect-secrets` 

RUN: 
`detect-secrets scan --all-files`

