pipeline {
  agent any
  stages {
    stage('prepare') {
      steps {
        sh '''sudo apt-get install -y python-pip

'''
        sh 'sudo pip install molecule'
      }
    }
  }
}