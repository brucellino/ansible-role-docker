pipeline {
  agent {
    node {
      label 'molecule'
    }
  }
  stages {
    stage('Create and Converge') {
      steps {
        withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'molecule_aws']]) {
        sh 'printenv'
        sh 'molecule lint'
        sh 'molecule --debug create'
        sh 'molecule converge' 
        }
      }
    }
    stage('Verify') { 
      steps {
        withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'molecule_aws']]) {
          sh 'molecule verify'
        }
      }
    }
    stage('Clean up') {
      steps {
        sh 'molecule destroy'
      }
    }
  }
  // post {
  //   always { slackSend (token: slack_token, message: "Job completed") } 
  // }
  environment {
    AWS_REGION="eu-central-1"
    slack_token = credentials('slack_hook')
  }
}
