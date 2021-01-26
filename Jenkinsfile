pipeline {
    agent {
        node {
            label 'ubuntu'

            // Use custom workspace
            // customWorkspace "${env.HOME}/workspace/jenkins_pipeline_example"
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
            environment {
                // set env var
                ENV_TEST = 'testing'
                ENV_TEST2 = "${sh(returnStdout: true, script: 'date')}"
            }
            steps {
                echo '=== ENV ==='
                sh 'env'

                echo '=== Build Phase ==='

                // checkout git repo
                dir('git_example') {
                    git url: 'git@github.com:hevangel-com/git_example.git', credentialsId: 'git-hevangel'
                }

                // create python virtual environment
                sh 'python3 -m venv --system-site-packages venv'
                withPythonEnv("${WORKSPACE}/venv/") {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('test') {
            environment {
                // set env var
                ENV_TEST = 'testing'

                // get credentials
                SSH_CREDS = credentials('git-hevangel')
            }
            steps {
                echo '=== Test Phase ==='
                sh 'echo "SSH private key is located at $SSH_CREDS"'
                sh 'echo "SSH user is $SSH_CREDS_USR"'
                sh 'echo "SSH passphrase is $SSH_CREDS_PSW"'

                // run dummy test
                withPythonEnv("${WORKSPACE}/venv/") {
                    sh 'python3 dummy_test.py'
                }
                stash includes: 'test_results.xml', name: 'juint'

                // create HTML report 
                sh "sed 's/BUILD_ID/${BUILD_ID}/' report_template.html > test_report.html"
        
                // add a line to the 
                dir('git_example') {
                    sh 'touch jenkins_runs.txt'
                    sh 'date >> jenkins_runs.txt'
                }
            }
        }
        stage('archive') {
            steps {
                echo '=== Archive Phase ==='
                junit allowEmptyResults: true, testResults: 'test_results.xml'

                publishHTML target: [
                    allowMissing: false, 
                    alwaysLinkToLastBuild: true, 
                    keepAll: true, 
                    reportDir: '', 
                    reportName: 'HTML Report', 
                    reportTitles: 'Report, Template',
                    reportFiles: 'test_report.html, report_template.html',
                ]

                dir('git_example') {
                    archiveArtifacts 'jenkins_runs.txt'
                }
            }
        }
        stage('deploy') {
            // skip deploy if the build is triggered by github push webhook
            when {not {triggeredBy cause: 'GitHubPushCause'}}
            steps {
                echo 'deploy phase'
                dir('git_example') {
                    sh 'git add -A'
                    sh 'git commit -am "check in"'
                    sshagent (['git-hevangel']) {
                        sh 'git push origin HEAD:master'
                    }
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
            mail subject: 'Jenkins build error', 
                to: 'jenkins@hevangel.com', 
                body: """
                \nJob: ${JOB_NAME}
                \nBuild: ${BUILD_NUMBER}
                \nURL: ${BUILD_URL}
                \nNode: ${NODE_NAME}
                \nWorkspace: ${WORKSPACE}
               """
        }
        cleanup {
            echo 'clean up at the end'
        }
    }
}
