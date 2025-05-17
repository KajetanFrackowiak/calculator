pipeline {
    agent any

    triggers {
        pollSCM("* * * * *")
    }

    parameters {
        booleanParam(name: "SEND_EMAIL", defaultValue: false, description: "Enable email notification?")
    }

    stages {
        stage("Install Dependencies") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }

        stage("Static Code Analysis") {
            steps {
                sh "python -m flake8 . --format=html --htmldir=flake8-report"
            }
        }

        stage("Tests") {
            steps {
                sh "python -m coverage run -m pytest tests/test_main.py --maxfail=1 --disable-warnings -q"
                sh "python -m coverage report"
                sh "python -m coverage html"
            }
        }

        stage("Publish Coverage Report") {
            steps {
                publishHTML(target: [
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
    }

    post {
        always {
            script {
                if (params.SEND_EMAIL) {
                    emailext(
                        to: "kajtek.gdynia@gmail.com",
                        subject: "Pipeline Result: ${currentBuild.fullDisplayName}",
                        body: """\
Your pipeline has finished.
Status: ${currentBuild.currentResult}
Details: ${env.BUILD_URL}
"""
                    )
                } else {
                    echo "Email notification disabled by feature toggle."
                }
            }
        }
    }
}
