from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class SpotInstanceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, 'MyVPC', cidr='10.0.0.0/16')

        # Create a Security Group
        security_group = ec2.CfnSecurityGroup(self, 'MySecurityGroup', group_description='My security group', vpc_id=vpc.vpc_id)

        # Add an inbound rule to allow SSH access
        ec2.CfnSecurityGroupIngress(self, 'SSHAccess',
                                    group_id=security_group.ref,
                                    ip_protocol='tcp',
                                    cidr_ip='0.0.0.0/0',
                                    from_port=22,
                                    to_port=22)

        # Create an EC2 Spot Fleet
        spot_fleet = ec2.CfnSpotFleet(self, 'MySpotFleet',
                                      spot_fleet_request_config_data=ec2.CfnSpotFleet.SpotFleetRequestConfigDataProperty(
                                          target_capacity=1,
                                          iam_fleet_role='arn:aws:iam::123456789012:role/YourFleetRole',
                                          launch_specifications=[ec2.CfnSpotFleet.SpotFleetLaunchSpecificationProperty(
                                              instance_type='t2.micro',
                                              image_id=ec2.MachineImage.latest_amazon_linux().get_image(self).image_id,
                                              security_groups=[ec2.CfnSpotFleet.GroupIdentifierProperty(group_id=security_group.ref)]
                                          )]
                                      )
                                      )

        # Add tags to the Spot Fleet
        core.Tags.of(spot_fleet).add('Name', 'MySpotFleet')

app = core.App()
SpotInstanceStack(app, "SpotInstanceStack")
app.synth()
