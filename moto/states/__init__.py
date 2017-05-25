from __future__ import unicode_literals
from .models import states_backends
from ..core.models import base_decorator, deprecated_base_decorator

states_backend = states_backends['us-east-1']
mock_states = base_decorator(states_backends)
mock_states_deprecated = deprecated_base_decorator(states_backends)
