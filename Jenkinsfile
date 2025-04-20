pipeline {
    agent any
    stages {
        stage('Get Data') {
            steps {
                sh 'python3 scripts/01_get_data.py'
            }
        }
        stage('Preprocess') {
            steps {
                sh 'python3 scripts/02_preprocess.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python3 scripts/03_train.py'
            }
        }
        stage('Serve Model') {
            steps {
                sh 'nohup python3 scripts/04_serve_model.py &'
            }
        }
    }
}