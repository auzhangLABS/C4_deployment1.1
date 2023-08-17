# Project Documentation for Deployment 1.1

1. First, I uploaded it into Jenkins to make sure that the build and test phase was okay to run. <br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/76ed22f4-8c91-4f9d-870c-7b87318dc3ee)

2. Once, I got that confirmation that it work in Jenkin, I uploaded it to Amazon Elastic Beanstalk. <br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/409792f2-490c-4946-b76b-968a4b93b4ad)

3. Then, I got an error that was showing that my Environment health was Degraded.<br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/37168291-ed1b-4cab-84a4-9c363827d879)


4. I decided to look into the log to see what when wrong. I notice that I was unable to find a module called application. Here, I decide to go into this deployment to find the issue. Upon investigating, I find out that the appication.py file was accidentally spelled wrong. Once I fixed that, I rerun it in Jenkins and then upload it to Elastic Beanstalk. Then, it was successful<br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/cdc7db25-ab83-4636-bfe7-75f8bf3a96bb)
