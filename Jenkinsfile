pipeline {
  agent {
    node {
      label 'molecule'
    }

  }
  stages {
    stage('prepare') {
      steps {
        sh 'molecule lint'
      }
    }
    stage('test') {
      steps {
        sh 'molecule test'
      }
    }
  }
  post {
    always { slackSend (token: slack_token, message: "hi") } 
  }
  environment {
    slack_token = credentials('slack-token')
  }
}
