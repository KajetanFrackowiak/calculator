pipeline {
    agent any
    stages {
        stage("install dependencies") {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }

        stage("main") {
            steps {
                script {
                    sh 'python3 main.py'
                }    
            }
        }

        stage("test_main") {
            steps {
                script {
                    sh "export PATH=$PATH:/var/lib/jenkins/.local/bin"
                    
                    sh "pytest tests/test_main.py --maxfail=1 --disable-warnings -q"
                }
            }
        }
    }
}