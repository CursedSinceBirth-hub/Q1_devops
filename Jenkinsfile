pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t a-app .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker run -d -p 5000:5000 a-app'
            }
        }
    }
}
