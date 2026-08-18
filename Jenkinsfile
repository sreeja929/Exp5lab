pipeline{
agent any
stages{
stage('compile'){
  steps{
    sh 'python3 Greatest.py<< EOF
10
20
15
EOF'
}}
stage('Run'){
steps{
sh 'python3 Greatest.py'
}}}}
