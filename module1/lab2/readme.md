checkov
checkov sudo docker run --tty --rm --volume (pwd):/app -w /app bridgecrew/checkov --directory /app


trivy

trivy fs lab12/
sudo docker run --rm -it -v "$(pwd):/lab" -w /lab aquasec/trivy fs . 

osv-scanner 
install https://google.github.io/osv-scanner/installation/
run osv-scanner scan source -r .

grype 
install curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
run grype file:Dockerfile
