pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Lint") {
            steps {
                sh "pip install flake8 && flake8 main.py"
            }
        }
        stage("Unit test") {
            steps {
                sh "pip install pytest && pytest test_main.py"
            }
        }
        stage("Build") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage("Docker build") {
            steps {
                sh "docker build -t thekajtek/calculator:${BUILD_TIMESTAMP} ."
            }
        }
        stage("Docker push") {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u thekajtek --password-stdin"
                    sh "docker push thekajtek/calculator:${BUILD_TIMESTAMP}"
                }
            }
        }
        stage("Update version") {
            steps {
                sh "sed -i 's/{{VERSION}}/${BUILD_TIMESTAMP}/g' deployment.yaml"
            }
        }
        stage("Deploy to staging") {
            steps {
                sh "kubectl config use-context staging"
                sh "kubectl apply -f https://raw.githubusercontent.com/hazelcast/hazelcast-kubernetes/master/rbac.yaml"
                sh "kubectl apply -f https://raw.githubusercontent.com/hazelcast/hazelcast-kubernetes/master/hazelcast-deployment.yaml"
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl apply -f service.yaml"
            }
        }
        stage("Acceptance test") {
            steps {
                sleep 60
                sh "chmod +x acceptance-test.sh && ./acceptance-test.sh"
            }
        }
        stage("Release") {
            steps {
                sh "kubectl config use-context production"
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl apply -f service.yaml"
            }
        }

        stage("Smoke test") {
            steps {
                sleep 60
                sh "chmod +x smoke-test.sh && ./smoke-test.sh"
            }
        }
    }
}