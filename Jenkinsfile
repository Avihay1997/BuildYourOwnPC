pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Avihay1997/BuildYourOwnPC.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('buildyourownpc-backend')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}
