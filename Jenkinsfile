pipeline {
  agent any
  stages {
    stage('prepare') {
      agent {
        node {
          label 'ec2'
        }
      }
      steps {
        sh 'sudo apt-get install -y python-pip'
        sh 'sudo pip install molecule'
        sh 'which ansible'
      }
    }
    stage('test') {
      agent { 
        node {
          label 'ec2'
        }
      }
      steps {
        sh 'molecule test'
      }
    }
  }
}