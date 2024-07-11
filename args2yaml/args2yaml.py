import argparse

import yaml


def args2yaml(args: argparse.Namespace, *, file: str = "opt.yaml") -> None:
    """
    Parameters:
        args: an argument namespace object containing your script's arguments
        file: a string; the name of the yaml file where the arguments will be saved [default: opt.yaml]
    Returns:
        None
    """
    # add file extension
    if not (file.endswith(".yaml") or file.endswith(".yml")):
        file += ".yaml"

    # save yaml dictionary
    with open(file=file, mode="w") as f:
        yaml.dump(vars(args), f)
