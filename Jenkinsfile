pipeline {
  agent any

  stages {
    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Tests + Coverage') {
      steps {
        sh '''
          . venv/bin/activate
          # Run pytest with coverage enabled
          pytest --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
        '''
      }
    }

    stage('Publish Reports') {
      steps {
        // Publish JUnit results
        junit 'test-results.xml'

        // Publish HTML coverage report
        publishHTML(target: [
          reportDir: 'htmlcov',
          reportFiles: 'index.html',
          reportName: 'HTML Coverage Report',
          alwaysLinkToLastBuild: true,
          keepAll: true
        ])
      }
    }
  }

  post {
    always {
      echo "Build completed. Reports are available in Jenkins UI."
    }
  }
}