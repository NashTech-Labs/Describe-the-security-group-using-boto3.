## How to describe the security group using boto3.

#### A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 CIDR address range, or from the instances associated with the specified security group. You can follow this [link](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to know more.

-------------

**Files:** 
```
        describe_security_grp_rule.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to validate the script.

        python3 describe_security_grp_rule.py