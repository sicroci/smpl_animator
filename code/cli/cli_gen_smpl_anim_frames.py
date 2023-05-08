#!/usr/bin/env python2.7

import os

import click

import yaml

from animate_smpl import main_run_yaml 


def main(
    run_filename 
):
    print("Configuration file: " + run_filename)

    stream = file(run_filename, 'r')
    cfg = yaml.safe_load(stream)

    main_run_yaml(cfg)


@click.command()
@click.option("--run", type=str, required=True)
def main_cmd(
    run
):
    main(
        run_filename=run,
    )


if __name__ == "__main__":
    main_cmd()
