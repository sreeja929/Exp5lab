pipeline{
agent any
stages{
stages('compile'){
sh 'javac HelloWorld.java'
}}
stage('Run'){
steps{
sh 'java HelloWorld'
}}}
