pipeline {
    agent any

    environment {
        IMAGE_NAME = 'docker-demo'
        IMAGE_TAG  = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir('project') {
                    bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
                }
            }
        }

        stage('Smoke Test') {
            steps {
                bat """
                    docker run -d --name smoke-test-%BUILD_NUMBER% -p 8000:8000 %IMAGE_NAME%:%IMAGE_TAG%
                    timeout /t 5
                    curl -f http://localhost:8000 || exit 1
                """
            }
        }
    }

    post {
        always {
            bat "docker rm -f smoke-test-%BUILD_NUMBER% || exit 0"
        }
        success {
            echo 'Build and smoke test passed.'
        }
        failure {
            echo 'Build or smoke test failed.'
        }
    }
}
