# Amazon Bedrock Prompt Flow - AI with Infrastructure as a Code!
This article demonstrates the ability to create Amazon Bedrock PromptFlow with the Infrastructure as a Code (IAC) - leveraging CDK in AWS. Amazon Bedrock PromptFlow is an exciting new capability that allows one to leverage the power of generative AI models like Amazon CodeWhisperer through an intuitive graphical interface. By combining PromptFlow with Infrastructure as Code (IaC) using the AWS Cloud Development Kit (CDK), one can streamline the process of deploying and managing AI-powered applications on AWS. The generated IaC code can be further customized and integrated with other AWS services like AWS Lambda, Amazon DynamoDB, Amazon S3, and more. This allows one to build end-to-end applications that leverage the power of generative AI while seamlessly integrating with existing infrastructure.

Here is an example that kicked me:
* [Demo - Amazon Bedrock Prompt Management | Amazon Web Services](https://www.youtube.com/watch?v=CE_-zrMvcuk)
* [Demo - Amazon Bedrock Prompt Flows | Amazon Web Services](https://www.youtube.com/watch?v=_Bmk6peAHao)

While I understand that easy usage of GUI is a step forward, in the real world, the business logic change pretty fast, and so is the requirement to adapt the GenAI flows too. In that context, we don't have to start building flows right from scratch every time. We heavily use templates - pre-built basic flows that allow us to do further customization. Therefore, I experimented with building the PromptFlows not with the GUI, but with CDK - yes, the IaC service from AWS.

## Use Case
My experimental use case is simple, but enough to demo the power of GenAI and IaC. Imagine a guest is able to open a chatbot of a hotel and asks questions. The chatbot is able to analyze the text if the question is about the Spa Services available at the hotel. If yes, then it categorizes as "Spa_Service" related questions, if no, then it categorizes as "generic" question.
![image](https://github.com/user-attachments/assets/8c536771-44a9-496d-ba22-a151a7928a44)
## Implementations
AWS has released L1 construct of the Bedrock PromptFlow, which is close to Cloudformation template. I am looking forward for the AWS to release higher consturct as the PromptFlow moves from experimental phase to more matured services. I went ahead and used the L1 Python construct. Reviewing the [Bedrock PromptFlow CDK L1 construct](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_bedrock/CfnFlow.html), i found the pattern similar to topology design in any network analytics. The pattern contains:
1. First define all the NODES that a flow will have, e.g., Input, Output, Prompt, Conditional etc.
2. Within the node defintion, define properties of each nodes - data type it handles, LLM models it's going to use etc.
3. Secondly, define CONNECTIONS for all the nodes - origin and destinations pair connected with each other
4. Thirdly, the IAM permisssion and policies are added in the CDK code

# How to setup this example in your AWS Account
1. Clone this GitHub repository to your dev environment. [GitHub Cloning Steps](https://www.youtube.com/watch?v=Nl0J_tcnhQ4&t=134s)
2. Run all the commands to setup a CDK environment (Refer the section CDK Setup Instructions)
3. Next run the following command to configure and Deploy this Demo
```
$ cdk synth
$ cdk deploy
```
Once the deployment is successful, you will see the new Prompt Flows instance created with the name "cdk_first_prompt_flow1"
<img width="1134" alt="image" src="https://github.com/user-attachments/assets/96fd7c05-5e76-4e7c-9e9b-d0d70bec7bd3">


3. Once you are done reviewing the prompt flow in the Bedrock Console of AWS, then don't forget to destroy
```
$ cdk destroy
```

# CDK setup Instructions
This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
