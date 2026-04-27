pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t event-app .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker run -d -p 5000:5000 event-app'
            }
        }
    }
}
