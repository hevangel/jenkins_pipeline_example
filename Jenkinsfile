pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                sh 'touch a.txt'
                sh 'python3 --version'
                sh 'date >> a.txt'
            }
        }
        stage('deploy') {
            steps {
                sh 'git add -A'
                sh 'git commit -am "check in"'
            }
        }
        stage('push') {
            steps {
                sh 'git push origin HEAD:master'
            }
        }
        stage('html') {
            steps {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
            }
        }
     }
 }
