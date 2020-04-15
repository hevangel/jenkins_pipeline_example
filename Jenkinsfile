pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                echo 'build phase'
                echo "workspace: ${env.WORKSPACE} on ${env.JENKINS_URL}"
                sh 'python3 -m venv --system-site-packages python_venv'
                withPythonEnv("${WORKSPACE}/python_venv/") {
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 test.py'
                }
                sh 'touch a.txt'
                sh 'date >> a.txt'
            }
        }
        stage('test') {
            steps {
                echo 'test phase'
            }
        }
        stage('archive') {
            steps {
                echo 'archive phase'
                junit allowEmptyResults: true, testResults: 'test_results.xml'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
                archiveArtifacts 'a.txt'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy phase'
                git 'git add a.out'
                sh 'git commit -am "check in"'
                sshagent (credentials: ['git-jenkins.hevangel.com']) {
                    sh 'git push origin HEAD:master'
                }
            }
        }
    }
    post {
        always {
            echo 'One way or another, I have finished'
            // deleteDir() /* clean up our workspace */
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
