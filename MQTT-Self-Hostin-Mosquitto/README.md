## Requirements
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)
* Mosquitto 2.0.18
* Docker-compose

### Install Docker and Docker-compose
```BASH
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo echo  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
##Run Docker as a non-root user
sudo groupadd docker
sudo usermod -aG docker $USER
##
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```


### Set up
```BASH
nano docker-compose.yaml
mkdir ./mosquitto
nano ./mosquitto/mosquitto.conf
nano ./mosquitto/passwd
docker-compose up -d
docker-compose ps
```
### Regenerate password
```BASH
docker exec -it mosquitto sh
mosquitto_passwd -U /etc/mosquitto/passwd
docker-compose restart
```

### Clear
```BASH
docker-compose down --rmi all -v --remove-orphans
```
