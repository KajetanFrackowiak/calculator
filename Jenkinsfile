pipeline {
    agent any

    triggers {
        pollSCM("* * * * *") // Pools every minute
    }

    stages {
        stage("Install Dependencies") {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }

        stage("Static Code Analysis") {
            steps {
                sh "python -m flake8 . --format=html --htmldir=flake8-report"
            }
        }

        stage("Tests") {
            steps {
                script {
                    sh "python -m coverage run -m pytest tests/test_main.py --maxfail=1 --disable-warnings -q"
                    sh "python -m coverage report"
                    sh "python -m coverage html"

                }
            }
        }

        stage("Publish Coverage Raport") {
            steps {
                publishHTML (target : [
                    reportDir: "htmlcov",
                    reportFiles: "index.html",
                    reportName: "Coverage Report"
                ])
            }
        }

        stage("Publish Flake8 Report") {
            steps {
                publishHTML(target: [
                    reportDir: "flake8-report",
                    reportFiles: "index.html",
                    reportName: "Static Code Analysis"
                ])
            }
        }

        // post {
        //     always {
        //         mail to: "kajtek.gdynia@gmail.com",
        //         subject: "Completed Pipeline: ${currentBuild.fullDisplayName}",
        //         body: "Your build completed, please check: ${env.BUILD_URL}"
        //     }
        // }
    }
}