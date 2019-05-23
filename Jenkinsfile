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
    stage('converge') {
      steps {
         withCredentials(
                [[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    credentialsId: 'aws_sandbox_credentials_jenkins',  // ID of credentials in Jenkins
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]])
        sh 'molecule create'
        sh 'molecule converge'
      }
    }
    stage('Verify') { 
      steps {
        sh 'molecule verify'
      }
    }
    stage('Clean up') {
      steps {
        sh 'molecule destroy'
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
