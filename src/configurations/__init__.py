import os

from .prod import ProdConfig
from .dev import DevConfig
from .test import TestConfig


__all__ = ('CONFIG')



deploy = os.environ.get('deploy')
if deploy == 'prod':
	CONFIG = ProdConfig
elif deploy == 'test':
	CONFIG = TestConfig
else:
	CONFIG = DevConfig
