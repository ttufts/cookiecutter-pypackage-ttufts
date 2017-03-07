import argparse
import yaml
from custom_logger import CustomLogger

"""
{{cookiecutter.class_name}}
Tested on {{cookiecutter.python_version}}
"""


class {{cookiecutter.class_name}}():
    def __init__(self, verbose=False):
        """
        Setup {{cookiecutter.class_name}} class

        """
        self.verbose = verbose
        self.logger = CustomLogger(self.__class__.__name__, ".{{cookiecutter.class_name}}.log", verbose=self.verbose).get_logger()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="YAML formatted config file", required=False)
    parser.add_argument("-v", "--verbose", help="Print verbose logging (log_level=DEBUG)", action="store_true")
    args = parser.parse_args()

    if args.config is not None:
        with open(args.config) as f:
            config = yaml.safe_load(f)

    p = {{cookiecutter.class_name}}(config=config, verbose=args.verbose)
