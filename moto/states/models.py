from __future__ import unicode_literals

import datetime
import uuid
from collections import defaultdict

from moto.core import BaseModel
from moto.core import BaseBackend
from moto.states import util


class Activity(BaseModel):

    def __init__(self, activity_arn):
        self.activity_arn = activity_arn

        self.creation_date = datetime.utcnow()


class StateMachine(BaseModel):

    def __init__(self, state_machine_arn, definition, role_arn, region):
        self.definition = definition
        self.state_machine_arn = state_machine_arn
        self.role_arn = role_arn

        self.creation_date = datetime.utcnow()


class StateMachineExecution(BaseModel):

    def __init__(self, state_machine_arn, region, name=None, input=None):
        self.state_machine_arn = state_machine_arn
        self.name = name
        self.input = input

        self.start_date = datetime.utcnow()


class ActivityTask(BaseModel):

    def __init__(self, activity_arn, worker_name=None):
        self.activity_arn = activity_arn
        self.worker_name = worker_name
        self.task_token = str(uuid.uuid4())
        self.input = {}
        self.result = {}

        self.start_date = datetime.utcnow()


class StatesBackend(BaseBackend):

    def __init__(self, aws_region):
        # activityArns to activity models
        self.activities = {}

        # stateMachineArns to state machine models
        self.state_machines = {}

        # executionArn to state machine execution models
        self.state_machine_executions = {}

        # taskTokens to activity task models
        self.activity_tasks = {}

        self.aws_region = aws_region

    def reset(self):
        region = self.aws_region
        self.__dict__ = {}
        self.__init__(region)

    def _validate_name(self, name):
        # Type: String
        if type(name) != basestring:
            raise errors.InvalidName()

        # Length Constraints: Minimum length of 1. Maximum length of 80.
        if 1 <= len(name) <=80:
            raise errors.InvalidName()

        # State machine names must NOT contain:
        #    whitespace
        #    brackets < > { } [ ]
        #    wildcard characters ? *
        #    special characters " # % \ ^ | ~ ` $ & , ; : /
        #    control characters (U+0000..001F, U+007F..009F)
        # TODO: actually implement this

    def _validate_arn(self, arn):
        # Type: String
        if type(arn) != basestring:
            raise InvalidArn()

        # Length Constraints: Minimum length of 1. Maximum length of 256.
        if 1 <= arn <= 256:
            raise InvalidArn()

    def create_activity(self, name):
        self._validate_name(name)

        activity_arn = util.derive_activity_arn(name, self.aws_region)
        activity = Activity(activity_arn)

        if activity_arn not in self.activities:
            # Amazon idempotently returns a 200, but doesn't upsert the
            # activity
            self.activites[activity_arn] = activity

        return activity

    def create_state_machine(self, definition, name, role_arn):
        self._validate_name(name)

        state_machine_arn = util.derive_state_machine_arn(name, self.aws_region)
        state_machine = StateMachine(state_machine_arn, definition, name, role_arn)

        if state_machine_arn in self.state_machines:
            raise errors.StateMachineAlreadyExists()

        self.state_machines[state_machine_arn] = state_machine

        return state_machine

    def delete_activity(self, activity_arn):
        if activity_arn not in self.activities:
            raise errors.InvalidArn()
        del self.activities[activity_arn]

    def delete_state_machine(self, state_machine_arn):
        if state_machine_arn not in self.state_machines:
            raise errors.InvalidArn()
        del self.activities[state_machine_arn]

    def describe_activity(self):
        raise NotImplementedError()

    def describe_execution(self):
        raise NotImplementedError()

    def describe_state_machine(self):
        raise NotImplementedError()

    def get_activity_task(self, activity_arn, worker_name=None):
        self._validate_arn(activity_arn)

        if activity_arn not in self.activities:
            raise errors.ActivityDoesNotExist()

        activity_task = ActivityTask(activity_arn, worker_name)
        self.activity_tasks[activity_task.task_token] = activity_task

        raise NotImplementedError()

    def get_execution_history(self):
        raise NotImplementedError()

    def list_activities(self):
        raise NotImplementedError()

    def list_executions(self):
        raise NotImplementedError()

    def list_state_machines(self):
        raise NotImplementedError()

    def send_task_failure(self):
        raise NotImplementedError()

    def send_task_heartbeat(self):
        raise NotImplementedError()

    def send_task_success(self):
        raise NotImplementedError()

    def start_execution(self):
        raise NotImplementedError()

    def stop_execution(self):
        raise NotImplementedError()


# Derive actual regions?
states_backends = defaultdict(StatesBackend)