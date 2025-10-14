
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from controllers.task_controller import TaskController
from views.cli import CLI


def main():
    controller = TaskController()
    cli = CLI(controller)
    cli.run()


if __name__ == "__main__":
    main()
