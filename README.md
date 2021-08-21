# Jenkins Pipeline Example

1. Basic Jenkins and github integration. (Jenkinsfile)
 - [x] Create a multiple stages pipeline 
 - [x] Generate a fake Junit test result
 - [x] Push the artifact into github
2. Use parallel agent (JenkinfileParallel)
 - [x] static
 - [x] fail first
 - [x] matrix
 - [x] control flow (when)
 - [x] stash/unstash
 - [x] lock
 - [x] milestone
3. Job trigger (JenkinfileJobUpstream/JenkinsfileDownstream)
 - [x] trigger by the upstream job
 - [x] call by the upstream job
 - [x] use upstream artifact
 - [x] publish artifact to AWS S3
4. Docker integration (JenkinfileDocker)
 - [x] use docker in agent
 - [x] build from Dockerfile 
 - [x] publish docker image to docker hub

## Ubuntu master install
```bash
# Install Java Docker and Jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt upgrade
sudo apt install -y openjdk-11-jre-headless iputils-ping net-tools git python3.8-venv
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
sudo apt-get install -y openjdk-11-jre-headless iputils-ping net-tools git python3.8-venv
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

## Install Plug-ins
- Blue Ocean
- Pyenv Pipeline
- SSH Agent
- Build Timestamp
- Monitoring
- Dashboard View
- Docker Pipeline
- Docker Slaves
