checkov 
`sudo docker run --tty --rm --volume (pwd):/tf -w /tf bridgecrew/checkov --directory /tf` 

terrascan 
`sudo docker run --rm -it -v "$(pwd):/iac" -w /iac tenable/terrascan scan`      

trivy 
`sudo docker run --rm -it -v "$(pwd):/lab" -w /lab aquasec/trivy config .` 

