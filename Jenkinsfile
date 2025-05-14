pipeline {
    agent any
    stages {
        stage("Install Dependencies") {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }

        stage("Tests") {
            steps {
                script {
                    sh "/var/lib/jenkins/.local/bin/pytest tests/test_main.py --maxfail=1 --disable-warnings -q"
                    sh "coverage report"
                    sh "coverage html"
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
    }
}