pipeline {
    agent any

    stages {
        stage('Get Data') {
            steps {
                bat 'python scripts\\01_get_data.py'
            }
        }
        stage('Preprocess') {
            steps {
                bat 'python scripts\\02_preprocess.py'
            }
        }
        stage('Train Model') {
            steps {
                bat 'python scripts\\03_train.py'
            }
        }
        stage('Serve Model') {
            steps {
                bat 'start /B python scripts\\04_serve_model.py'
            }
        }
    }
}
