# Project Documentation for Deployment 1.1

## Purpose for this deployment. 
The Purpose of this Deployment was to successfully upload the application to Elastic Beanstalk and Jenkins. However, upon uploading to Elastic Beanstalk, we notice that we go an error. How are the steps I took to diagnose this problem 

1. First, I uploaded it into Jenkins to make sure that the build and test phase was okay to run. <br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/76ed22f4-8c91-4f9d-870c-7b87318dc3ee)

2. Once, I got that confirmation that it work in Jenkin, I uploaded it to Amazon Elastic Beanstalk. <br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/409792f2-490c-4946-b76b-968a4b93b4ad)

3. Then, I got an error that showed that my Environment health was Degraded.<br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/37168291-ed1b-4cab-84a4-9c363827d879)

4. I decided to look into the log to see what when wrong. I noticed that I was unable to find a module called application. Here, I decide to go into this deployment to find the issue. Upon investigating, I find out that the appication.py file was accidentally spelled wrong. Once I fixed that, I rerun it in Jenkins and then uploaded it to Elastic Beanstalk. Then, it was successful<br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/cdc7db25-ab83-4636-bfe7-75f8bf3a96bb)

Here is the diagram that shows my process. <br>

![image](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/ed80a70e-87a2-49bf-b004-50ba74e9f576)

## Key Learning
A major learning of this deployment was that Jenkin wasn't checking the naming conventions of some of the files within the application. For the future, I could've Jenkis test for that factor as well. Additionally, I learn that Amazon Elastic Beanstalk was looking for a specific application name for the files, therefore It kept giving me Degarded health. Upon finding this out, I was able to rename and successfully upload it within Amazon Elastic Beanstalk. 
