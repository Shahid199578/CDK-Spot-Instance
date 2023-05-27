
# Welcome to CDK Python project!

This is a project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`


* Prerequisites:

* AWS Account:*
Ensure that you have an AWS account. If you don't have one, you can create a free-tier account on the AWS website.

*Python and AWS CDK:*
Make sure you have Python installed on your machine. You can download Python from the official Python website `(https://www.python.org/downloads/)`. Once Python is installed, 
you can install the AWS CDK by running the following command:
`pip install aws-cdk.core`

* AWS CLI:*
Install the AWS Command Line Interface (CLI) on your machine. You can download and install it from the AWS CLI documentation (`https://aws.amazon.com/cli/`).

*Configure AWS CLI:*
After installing the AWS CLI, run the following command in your terminal and provide your AWS access key ID, secret access key, default region, and default output format when prompted:

`aws configure`

This step will set up your AWS CLI credentials, allowing you to interact with your AWS account using the CLI.

*Project Setup:*

Make sure you have installed the AWS CDK CLI by running the following command:

`npm install -g aws-cdk`

This command installs the AWS CDK globally on your machine.

*Initialize a CDK Project: *
Open your terminal and navigate to the directory where you want to create your project. Run the following command to initialize a new CDK project:

`cdk init app --language python`

This command initializes a new CDK project in Python and sets up the necessary files and folder structure.

*Install CDK Dependencies: *
Navigate into your project directory and install the required dependencies by running the following command:

`pip install -r requirements.txt`

This command will install the AWS CDK module and other dependencies specified in the requirements.txt file.

*Create a CDK Stack:*

 open the `app.py` file in a text editor and replace iam_fleet_role
 
*IAM Role:*
 
 To create and manage spot fleets using AWS CDK, the IAM role associated with your CDK deployment will need certain permissions. Here are the permissions typically required for creating and managing spot fleets:

*ec2:DescribeSpotFleetInstances: Allows describing spot fleet instances.*
*ec2:DescribeSpotFleetRequests: Allows describing spot fleet requests.*
*ec2:RequestSpotFleet: Allows requesting a new spot fleet.*
*ec2:CancelSpotFleetRequests: Allows canceling spot fleet requests.*
*ec2:ModifySpotFleetRequest: Allows modifying a spot fleet request.*
*ec2:DescribeInstances: Allows describing EC2 instances.*
*ec2:TerminateInstances: Allows terminating EC2 instances (if required).*

Here's an example IAM policy that includes the necessary permissions for creating and managing spot fleets:
 
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SpotFleetPermissions",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSpotFleetInstances",
        "ec2:DescribeSpotFleetRequests",
        "ec2:RequestSpotFleet",
        "ec2:CancelSpotFleetRequests",
        "ec2:ModifySpotFleetRequest",
        "ec2:DescribeInstances",
        "ec2:TerminateInstances"
      ],
      "Resource": "*"
	  },
    {
      "Sid": "AutoScalingPermissions",
      "Effect": "Allow",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups",
        "autoscaling:UpdateAutoScalingGroup"
      ],
      "Resource": "*"
    }
  ]
}

 

This code defines the SpotInstanceStack class, which creates a VPC, a security group, and an EC2 Spot instance using AWS CDK.

run the following command in your terminal to synthesize the CloudFormation template:

`cdk synth

This command will generate the CloudFormation template for your CDK stack.

*Deploy the Stack:* To deploy the stack to your AWS account, run the following command:

`cdk deploy

The command will prompt you to confirm the deployment. Type `y` and hit Enter to proceed. AWS CDK will create the necessary resources in your AWS account.

After a successful deployment, you will see the output in your terminal, including the stack name and the resources created.

*Congratulations!* You have successfully set up and deployed the AWS CDK project to start a Spot instance. The Spot instance will be created with the specified instance type, security group, and Spot price.


Note: Remember to clean up your resources after you have finished experimenting with the stack by running `cdk destroy` in your project directory. This will remove the created resources from your AWS account and prevent any unnecessary charges.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
