import yaml


def args2yaml(args, *, file="opt.yaml"):
    # add file extension
    if not (file.endswith(".yaml") or file.endswith(".yml")):
        file += ".yaml"

    # save yaml dictionary
    with open(file=file, mode="w") as f:
        yaml.dump(vars(args), f)
