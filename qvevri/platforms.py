"""Generic platform functions."""
from collections import defaultdict

from qvevri import runners

# gets populated by _init_platforms()
__all__ = defaultdict(list)


def _init_platforms():
    for runner_name in runners.__all__:
        runner = runners.import_runner(runner_name)()
        for platform in runner.platforms:
            __all__[platform].append(runner_name)


_init_platforms()
