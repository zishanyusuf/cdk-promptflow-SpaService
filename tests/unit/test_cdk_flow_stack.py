import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_flow.cdk_flow_stack import CdkFlowStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_flow/cdk_flow_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkFlowStack(app, "cdk-flow")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
