pipeline {
  agent {
    node {
      label 'molecule'
    }
  }
  stages {
    stage('QA') {
      sh 'molecule lint'
    }
    stage('Create') {
      steps {
        withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'molecule_aws']]) {
          sh 'pip3 install boto'
          retry(3) { sh 'molecule --debug create' }
      }
        withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'molecule_aws']]){
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
    INTERPRETER_PYTHON="python3"
    slack_token = credentials('slack_hook')
  }
}
