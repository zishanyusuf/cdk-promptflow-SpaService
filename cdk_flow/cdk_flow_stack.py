from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_bedrock as bedrock
)
from constructs import Construct

class CdkFlowStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkFlowQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        cfn_flow = bedrock.CfnFlow(self, "MyCfnFlow",
                                   execution_role_arn="arn:aws:iam::471112580598:role/service-role/AmazonBedrockExecutionRoleForFlows_SL6VMJWYW9",
                                   name="cdk_first_prompt_flow",

                                   #Define nodes and connections here
                                   definition=bedrock.CfnFlow.FlowDefinitionProperty(
                                       nodes=[
                                           bedrock.CfnFlow.FlowNodeProperty(
                                               name="InputNode",
                                               type="Input",
                                            #    inputs=[
                                            #        bedrock.CfnFlow.FlowNodeInputProperty(
                                            #            #expression="$.input.text",
                                            #            expression="$.data",
                                            #            name="document",
                                            #            type="String"
                                            #            )],
                                                outputs=[
                                                    bedrock.CfnFlow.FlowNodeOutputProperty(
                                                                   name="document",
                                                                   type="String"
                                                                   )
                                                ]),
                                            bedrock.CfnFlow.FlowNodeProperty(
                                                name="OutputNode",
                                                type="Output",
                                                inputs=[
                                                   bedrock.CfnFlow.FlowNodeInputProperty(
                                                       #expression="$.input.text",
                                                       expression="$.data",
                                                       name="document",
                                                       type="String"
                                                       )]
                                                #        ,
                                                # outputs=[
                                                #     bedrock.CfnFlow.FlowNodeOutputProperty(
                                                #         name="document",
                                                #         type="String"
                                                #         )]
                                            )
                                            ]),
                                        #Adding conections and experimenting with it    
                                        connections=[bedrock.CfnFlow.FlowConnectionProperty(
                                            name="Spa_Connections",
                                            source="InputNode",
                                            target="OutputNode",
                                            type="Data",
                                            # the properties below are optional
                                            configuration=bedrock.CfnFlow.FlowConnectionConfigurationProperty(
                                                # conditional=bedrock.CfnFlow.FlowConditionalConnectionConfigurationProperty(
                                                #     condition="condition"
                                                #     ),
                                                    data=bedrock.CfnFlow.FlowDataConnectionConfigurationProperty(
                                                        source_output="document",
                                                        target_input="document"
                                                        )
                                                )
                                            )],    

                                    
                                    description="description",
                                    tags={
                                            "tags_key": "tags"
                                            },
                                    test_alias_tags={
                                        "test_alias_tags_key": "testAliasTags"
                                        }
)

