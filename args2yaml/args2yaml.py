import argparse
import os

import yaml


def args2yaml(args: argparse.Namespace, *, file: str = "opt.yaml") -> None:
    """
    Parameters:
        args[argparse.Namespace]: an argument namespace object containing your script's arguments
        file[str]: path to yaml file [default: opt.yaml]
    Returns:
        None
    """
    
    # create subdirectories from file path
    if len(split_path := file.split(os.path.sep)) > 1:
        os.makedirs(os.path.sep.join(split_path[:-1]))

    # save yaml dictionary
    with open(file=file, mode="w") as f:
        yaml.dump(vars(args), f)
