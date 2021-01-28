# Jenkins Pipeline Example

1. Basic Jenkins and github integration. (Jenkinsfile)
 - Create a multiple stages pipeline 
 - Generate a fake Junit test result
 - Push the artifact into github
2. Use parallel agent (JenkinfileParallel)
 - static
 - fail first
 - matrix
 - control flow (when)
 - stash/unstash
3. Job trigger (JenkinfileJobTrigger)
 - [x] trigger by the upstream job
 - [x] call by the upstream job
 - [x] use upstream artifact
 - [x] publish artifact to AWS S3
4. Docker integration (JenkinfileDocker)
 - [ ] use docker agent
 - [ ] publish docker image

## Ubuntu master install
```bash
# Install Java Docker and Jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt upgrade
sudo apt install -y openjdk-14-jre-headless git
sudo apt install -y jenkins
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

Set server time zone (optional)
sudo timedatectl set-timezone America/Vancouver

# Change Jenkins default port (optional)
#sudo sed -i "s/HTTP_PORT=8080/HTTP_PORT=9000/" /etc/default/jenkins

# Restart Jenkins
sudo service jenkins restart

# Open port 8080 in iptables (optional)
sudo apt-get install iptables-persistent
sudo iptables -I INPUT -p tcp --dport 8080 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -I OUTPUT -p tcp --sport 8080 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables-save |sudo tee /etc/iptables/rules.v4
```

## Ubuntu slave install
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y openjdk-11-jre-headless iputils-ping net-tools git
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

## Install Plug-ins
- Build Timestamp
- Blue Ocean
- Pyenv
- SSH Agent
- Monitoring
- Dashboard View
