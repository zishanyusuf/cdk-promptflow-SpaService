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
                                   name="cdk_first_prompt_flow1",

                                   ###################################
                                   
                                   #Define nodes and connections here
                                   definition=bedrock.CfnFlow.FlowDefinitionProperty(
                                        #First of all Define ALL conections across the nodes    
                                        connections=[
                                            #Define connections from Input node to the Prompt node
                                            bedrock.CfnFlow.FlowConnectionProperty(
                                                name="InputNodePromptNode",
                                                source="InputNode",
                                                target="Prompt_1Node",
                                                #Whether the source node that the connection begins from is a condition node ( Conditional ) or not ( Data ).
                                                type="Data",
                                            # the properties below are optional
                                            configuration=bedrock.CfnFlow.FlowConnectionConfigurationProperty(
                                                data=bedrock.CfnFlow.FlowDataConnectionConfigurationProperty(
                                                        source_output="document",
                                                        target_input="user_input"
                                                        )
                                                )
                                            ),
                                            
                                            #Define connections from Prompt node to Output node
                                            bedrock.CfnFlow.FlowConnectionProperty(
                                            name="PromptNode_OutputNode",
                                            source="Prompt_1Node",
                                            target="OutputNode",
                                            #Whether the source node that the connection begins from is a condition node ( Conditional ) or not ( Data ).
                                            type="Data",
                                            # the properties below are optional
                                            configuration=bedrock.CfnFlow.FlowConnectionConfigurationProperty(
                                                data=bedrock.CfnFlow.FlowDataConnectionConfigurationProperty(
                                                        source_output="modelCompletion",
                                                        target_input="document"
                                                        )
                                                )
                                            )],  

                                        #Secondly, define all the Nodes
                                        nodes=[
                                            ###1. Define the Prompt Node and its properties
                                            bedrock.CfnFlow.FlowNodeProperty(
                                            name="Prompt_1Node",
                                            type="Prompt",
                                            inputs=[
                                                   bedrock.CfnFlow.FlowNodeInputProperty(
                                                       expression="$.data",
                                                       name="user_input",
                                                       type="String"
                                                )],
                                                outputs=[
                                                    bedrock.CfnFlow.FlowNodeOutputProperty(
                                                                   name="modelCompletion",
                                                                   type="String"
                                                                   )
                                                ],

                                            # the properties below are optional
                                              configuration=bedrock.CfnFlow.FlowNodeConfigurationProperty(
                                                # input=input,
                                                # output=output,
                                                prompt=bedrock.CfnFlow.PromptFlowNodeConfigurationProperty(
                                                    source_configuration=bedrock.CfnFlow.PromptFlowNodeSourceConfigurationProperty(
                                                        inline=bedrock.CfnFlow.PromptFlowNodeInlineConfigurationProperty(
                                                            model_id="anthropic.claude-3-haiku-20240307-v1:0",
                                                            template_configuration=bedrock.CfnFlow.PromptTemplateConfigurationProperty(
                                                                text=bedrock.CfnFlow.TextPromptTemplateConfigurationProperty(
                                                                    text="You take the users' questions and categorize  in any one of the following: \"spa_services\" if user's quesiton is around spa services, \"generic\" if user's question is anything else. Provide only one category type as an asnwer.",
                                                                    
                                                                    # the properties below are optional
                                                                    input_variables=[bedrock.CfnFlow.PromptInputVariableProperty(
                                                                        name="user_input"
                                                                        )]
                                                                )
                                                            ),
                                                            template_type="TEXT"
                                                        )
                                                        
                                                    )
                                                )
                                                
                                            )),
                                            
                                            ##Create Input Node
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

                                            ##Create Output Node
                                            bedrock.CfnFlow.FlowNodeProperty(
                                                name="OutputNode",
                                                type="Output",
                                                inputs=[
                                                   bedrock.CfnFlow.FlowNodeInputProperty(
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
                                            )]
                                   ),
                                   description="description",
                                    tags={
                                            "tags_key": "tags"
                                            },
                                    test_alias_tags={
                                        "test_alias_tags_key": "testAliasTags"
                                        }
)