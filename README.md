For the love of Network Optimization, GenAI and IaC, i couldn't resist myself to get my hand dirty on doing it by myself and learning in the process. While doing it i found it very similar to the modeling and analytical exercise that I do while desining the network. It is similar because i have to be cognizant of the identified nodes and connections of the nodes across.

# Amazon Bedrock Prompt Flow - AI with Infrastructure as a Code!
This project demonstrates the ability to create Amazon Bedrock PromptFlow with the Infrastructure as a Code (IAC) - the CDK in AWS. PromptFlow is a revolutionzing concept in the AI, that allows a general users to leverage the GUI to customize and use the GenAI model while integrating it with other serverless services e.g., Lambda, DynamoDB etc. This empowers the the direct implementation of the GenAI in various use cases of application development. And what more one can ask if it's super intuitive to do so with GUI. Here is an example that kicked me:
* [Demo - Amazon Bedrock Prompt Management | Amazon Web Services](https://www.youtube.com/watch?v=CE_-zrMvcuk)
* [Demo - Amazon Bedrock Prompt Flows | Amazon Web Services](https://www.youtube.com/watch?v=_Bmk6peAHao)

While i get that easy usage of GUI is a thing forward, in real world the flow and logic changes pretty fast. And we don't have to start building flows right from the scratch every time. We heavily use templates - a pre-built basic flows that allows us to do further customization. Therefore, i expriemented with building the PromptFlows not with GUI, but with CDK - yes!! the IaC services from AWS. My experimental basic use case is simple, but enough to demo the power of GenAI and IaC. I wanted to build the following:

## Use Case

## Implementations
AWS has released L1 construct of the Bedrock PromptFlow, which is close to Cloudformation template. I am looking forward for the AWS to release higher consturct as the PromptFlow moves from experimental phase to more matured services. I went ahead and used the L1 Python construct. Reviewing the [Bedrock PromptFlow CDK L1 construct](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_bedrock/CfnFlow.html), i found the pattern similar to topology design in any network analytics. The pattern contains:
1. First define all the NODES that a flow will have, e.g., Input, Output, Prompt, Conditional etc.
2. Within the node defintion, define properties of each nodes - data type it handles, LLM models it's going to use etc.
3. Secondly, define CONNECTIONS for all the nodes - origin and destinations pair connected with each other
4. Thirdly, i needed to overlay the IAM permisssion and policies

5. 
1. Define and create an input that starts the logical flow
2. Connect it with 

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

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
