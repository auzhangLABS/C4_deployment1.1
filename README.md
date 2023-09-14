# Deployment 1.1 Documentation
## Purpose:
This Deployment is a continuation of Deployment 1. To see Deployment 1, click [here!](https://github.com/auzhangLABS/C4_deployment1/tree/main) The purpose of deployment 1.1 was to familiarize ourselves with encountering errors with Jenkins and AWS Elastic Beanstalk and learn how to diagnose them. 

## Steps:
1. Get the Github code from the Kura Labs repository and download it into our Github. Then run Jenkins and upload to AWS Elastic Beanstalk. To view this step more in-depth, click [here](https://github.com/auzhangLABS/C4_deployment1/tree/main)

## System Design Diagram:
To view the System Design Diagram, click [here!](https://github.com/auzhangLABS/C4_deployment1.1/blob/main/diagram.png)

## Issues/ Troubleshooting:
The first thing I noticed was that upon uploading to AWS Elastic Beanstalk we got an error that our environment health was degraded. To fix this, I looked into the log to see what went wrong. I noticed that I was unable to find a module called application. Then I looked into my application files and noticed that the app.py file was misnamed. After changing app.py to application.py, this issue was solved. I learned that Amazon Elastic Beanstalk was looking for a specific application name for the files, therefore It kept giving me Degarded Health. Upon finding this out, I was able to rename and successfully upload it within Amazon Elastic Beanstalk
![261386329-37168291-ed1b-4cab-84a4-9c363827d879](https://github.com/auzhangLABS/C4_deployment1.1/assets/138344000/3d150c2a-2b44-46f6-bdd6-16b552d049f2)

## Optimization:
I would try to Optimize this Deployment by editing the Jenkins files to check for the  naming convention of the files needed for AWS Elastic Beanstalk. That way, Jenkins would be able to inform me before uploading to AWS Elastic Beanstalk. 
