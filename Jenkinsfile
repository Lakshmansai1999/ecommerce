pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'pip3 install -r requirements.txt' 
            }
        }
        stage('Test') { 
            steps {
                sh 'python3 manage.py test' 
            }
        }
        stage('Deploy') { 
            steps {
                sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.56.114 "source venv/bin/activate; \
                cd ecommerce; \
                git pull origin master; \
                pip install -r requirements.txt --no-warn-script-location; \
                python manage.py migrate; \
                deactivate; \
                sudo systemctl restart nginx; \
                sudo systemctl restart gunicorn "' 
            }
        }
        stage('Email Notification'){
            steps {
             mail bcc: '', body: 'content', cc: '', from: '', replyTo: '', subject: 'ecommerce', to: 'klakshmansai@stratapps.com'
            }
        }
    }
}    
