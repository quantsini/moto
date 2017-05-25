import json
import six

from moto.core.responses import BaseResponse


class StatesResponse(BaseResponse):

    def create_activity(self):
        raise NotImplementedError()

    def create_state_machine(self):
        raise NotImplementedError()

    def delete_activity(self):
        raise NotImplementedError()

    def delete_state_machine(self):
        raise NotImplementedError()

    def describe_activity(self):
        raise NotImplementedError()

    def describe_execution(self):
        raise NotImplementedError()

    def describe_state_machine(self):
        raise NotImplementedError()

    def get_activity_task(self):
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
        return json.dumps({
            "executionArn": "string",
            "startDate": 1,
        })

    def stop_execution(self):
        raise NotImplementedError()
