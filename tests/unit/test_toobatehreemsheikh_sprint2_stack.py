import aws_cdk as core
import aws_cdk.assertions as assertions

from toobatehreemsheikh_sprint2.toobatehreemsheikh_sprint2_stack import ToobatehreemsheikhSprint2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in toobatehreemsheikh_sprint2/toobatehreemsheikh_sprint2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ToobatehreemsheikhSprint2Stack(app, "toobatehreemsheikh-sprint2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
