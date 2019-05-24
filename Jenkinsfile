pipeline {
  withCredentials([[
    $class: 'AmazonWebServicesCredentialsBinding',
    credentialsId: 'jenkins_aws_sandbox',
    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
  environment {
    access_id = "${AWS_ACCESS_KEY_ID}"
    secret_key = "AWS_SECRET_ACCESS_KEY"
  }
  stages {
    stage('Create and Converge') {
      agent {
        node {
          label 'molecule'
        }
      }
      steps {
        sh 'env'      
        sh 'molecule lint'
        sh 'molecule create'
        sh 'molecule converge'
      }
    }
    stage('converge') {
      steps {
        
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
