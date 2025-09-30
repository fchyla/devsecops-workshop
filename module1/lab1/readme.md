checkov 
`sudo docker run --tty --rm --volume $(pwd):/tf -w /tf bridgecrew/checkov --directory /tf` 

terrascan 
`sudo docker run --rm -it -v "$(pwd):/iac" -w /iac tenable/terrascan scan`      

trivy 
`sudo docker run --rm -it -v "$(pwd):/lab" -w /lab aquasec/trivy config .` 

### WSL 

To install the latest stable versions of Docker CLI, Docker Engine, and their dependencies:

 1. download the script

   $ curl -fsSL https://get.docker.com -o install-docker.sh

 2. verify the script's content

   $ cat install-docker.sh

 3. run the script with --dry-run to verify the steps it executes

   $ sh install-docker.sh --dry-run

 4. run the script either as root, or using sudo to perform the installation.

   $ sudo sh install-docker.sh

Clone the git repository into the WSL machine, from VSCode you can use the ssh connector or WSL extension (https://code.visualstudio.com/docs/remote/wsl-tutorial)
