from __future__ import unicode_literals


# Hard code this for now.
aws_account_id = '0123456789012'


def derive_activity_arn(activity_name, aws_region):
    template = 'arn:aws:states:{aws_region}:{aws_account_id}:activity:{activity_name}'
    return template.format(
        aws_region=aws_region,
        aws_account_id=aws_account_id,
        activity_name=activity_name,
    )


def derive_state_machine_arn(state_machine_name, aws_region):
    template = 'arn:aws:states:{aws_region}:{aws_account_id}:stateMachine:{state_machine_name}'
    return template.format(
        aws_region=aws_region,
        aws_account_id=aws_account_id,
        activity_name=state_machine_name,
    )
