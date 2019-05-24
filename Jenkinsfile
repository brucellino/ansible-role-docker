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
        sh 'molecule create'
        sh 'molecule converge' 
        }
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
  // post {
  //   always { slackSend (token: slack_token, message: "Job completed") } 
  // }
  environment {
    slack_token = credentials('slack_hook')
  }
}
