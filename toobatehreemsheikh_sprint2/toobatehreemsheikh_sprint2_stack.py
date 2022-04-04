from aws_cdk import (
    # Duration,
    aws_lambda as lambda_,# For Using Lambda Service
    Stack,
    RemovalPolicy,# To Remove Lambda S3 SNS Completly
    aws_events as events_,#To Schedule My Lambda Function To Invoke After Each Minute
    Duration,#To get Date And Time
    aws_events_targets as targets_,
)
from constructs import Construct

class ToobatehreemsheikhSprint2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        WHLambda_Function = self.create_lambda("Toobatehreemsheikh_WH_Lambda", "./resources", "WHLambda.lambda_handler")
        WHLambda_Function.apply_removal_policy(RemovalPolicy.DESTROY)
        
        lambdaSchedule=events_.Schedule.rate(Duration.minutes(1))
        lambdaTargets = targets_.LambdaFunction(handler=WHLambda_Function)
        
        rule= events_.Rule(self, "ToobaTehreemRule",
        description = "This is my WH rule to trigger lambda every 1 minute",
        enabled = True,
        schedule = lambdaSchedule,
        targets = [lambdaTargets]
        )
        
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, 
            id=id,
            code = lambda_.Code.from_asset(asset),
            handler = handler,
            runtime = lambda_.Runtime.PYTHON_3_6
            )
