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
                sh 'touch output.xml'
                junit allowEmptyResults: true, testResults: 'output.xml'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
                archiveArtifacts 'a.txt'
            }
        }
     }
     post {
        always {
            echo 'One way or another, I have finished'
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeeded!'
            // emailext body: 'jenkins test', subject: 'jenkins test', to: 'hevangel@gmail.com'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
 }
