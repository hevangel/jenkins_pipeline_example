# Jenkins Pipeline Example

1. Basic Jenkins and github integration. (Jenkinsfile)
 - Create a multiple stages pipeline 
 - Generate a fake Junit test result
 - Push the artifact into github
2. Use parallel agent (JenkinfileParallel)
 - [ ] static
 - [ ] fail first
 - [ ] matrix
 - [ ] dynamic loop list
 - [ ] control flow
3. Docker integration (JenkinfileDocker)
 - [ ] node
 - [ ] stage
4. Object Storage integration (JenkinsfileObjectStorage)
 - [ ] trigger by the first job
 - [ ] push into S3
 - [ ] push into Google Storage

## Ubuntu master install
```bash
# Install Java Docker and Jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt upgrade
sudo apt install openjdk-14-jre-headless docker git
sudo apt install jenkins

# Set server time zone (optional)
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
## Centos master install
```bash
# Install Java Docker and Jenkins
sudo yum install epel-release
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum update
sudo yum install java-8-openjdk docker jenkins git

# Set server time zone (optional)
sudo timedatectl set-timezone America/Vancouver

# Start Jenkin service
sudo systemctl start jenkins.service
sudo chkconfig jenkins on

# Open port 8080
sudo firewall-cmd --zone=public --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```
## Ubuntu slave install
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install openjdk-11-jre-headless docker iputils-ping net-tools
```

## Install Plug-ins
- Build Timestamp
- Blue Ocean
- Pyenv
- SSH Agent
- Monitoring
- Dashboard View
