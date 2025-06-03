pipeline {
    agent any

    environment {
        IMAGE_NAME = "avihay1997/buildyourpc-backend"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Avihay1997/BuildYourOwnPC.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:latest", "./backend")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:latest
                        """
                    }
                }
            }
        }
    }
}
