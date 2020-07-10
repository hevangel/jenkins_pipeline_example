pipeline {
   agent {
        node {
            label 'linux'
            customWorkspace ${env.JENKINS_HOME} + '/jenkins_pipeline_example'

        }
   }
   // periodic trigger
   triggers {
       cron('H 0 * * 1-5')
   }
   //parameters {
   //    booleanParam(name: 'PUSH', defaultValue: false, description: 'Push to github')
   //}
   stages {
       stage('build') {
           steps {
               dir('../git_example') {
                    git 'https://github.com/hevangel-com/git_example.git'
               }
               sh 'env'
               // create python virtual environment
               sh 'python3 -m venv --system-site-packages venv'
               withPythonEnv("${WORKSPACE}/venv/") {
                   sh 'pip3 install -r requirements.txt'
                   sh 'python3 dummy_test.py'
               }
               sh 'touch a.txt'
               sh 'date >> a.txt'
           }
       }
       stage('test') {
           // get credentials
           environment {
               SSH_CREDS = credentials('git-hevangel')
           }
           steps {
               echo 'test phase'
               sh 'echo "SSH private key is located at $SSH_CREDS"'
               sh 'echo "SSH user is $SSH_CREDS_USR"'
               sh 'echo "SSH passphrase is $SSH_CREDS_PSW"'
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
           // skip deploy if the build is triggered by github push webhook
           when {not {triggeredBy cause: 'GitHubPushCause'}}
           steps {
               echo 'deploy phase'
               sh 'git add -A'
               sh 'git commit -am "check in"'
               sshagent (['git-hevangel']) {
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
       aborted {
           echo 'I am aborted'
       }
       fixed {
           echo 'I am fixed'
       }
       regression {
           echo 'I am regression'
       }
       unsuccessful {
           echo 'I am unsuccessful'
           emailext subject: 'Jenkins build error', to: 'hevangel@gmail.com', body: """
                   Job: ${env.JOB_NAME}\n Build: ${env.BUILD_NUMBER}\n URL: ${env.BUILD_URL}\n
                   """
       }
       cleanup {
           echo 'clean up at the end'
       }
   }
}
