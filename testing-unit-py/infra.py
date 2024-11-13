from pulumi_aviatrix.account import Account

account = Account(
    "account",
    account_name="username",
    cloud_type=1,
    aws_account_number="123456789012",
    aws_iam=True,
    aws_role_app="arn:aws:iam::123456789012:role/aviatrix-role-app",
    aws_role_ec2="arn:aws:iam::123456789012:role/aviatrix-role-ec2",
)
