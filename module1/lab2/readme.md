# checkov
`sudo docker run --tty --rm --volume (pwd):/app -w /app bridgecrew/checkov --directory /app`

# trivy
RUN
`sudo docker run --rm -it -v "$(pwd):/lab" -w /lab aquasec/trivy fs .`

INSTALL
`curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin v0.66.0`
RUN
`trivy fs lab12/`


# osv-scanner 
INSTALL 
https://google.github.io/osv-scanner/installation/ or https://github.com/google/osv-scanner/releases (binary)

RUN
`osv-scanner scan source -r .`

# grype 
INSTALL
`curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin`
RUN
`grype file:Dockerfile`
