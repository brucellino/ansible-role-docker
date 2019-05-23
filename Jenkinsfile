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
        withCredentials([[
          $class: 'AmazonWebServicesCredentialsBinding',
          accessKeyVariable: 'AWS_ACCESS_KEY_ID',
          credentialsId: 'jenkins_aws_sandbox',
          secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
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
    always { slackSend (token: slack_token, message: "Job completed") } 
  }
  environment {
    slack_token = credentials('slack_hook')
  }
}
