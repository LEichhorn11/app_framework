import click
from utils.logging import logging
from pipeline.pipeline import Pipeline


@click.group(invoke_without_command=True)
@click.option("--pipeline", default="initdb")
def cli(pipeline: str):
    if pipeline == "initdb":
        initdb()
    else:
        dropdb()


@cli.command()
def initdb():
    logging.info("Initialized the database")
    Pipeline().first_pipeline()


@cli.command()
def dropdb():
    logging.info("Dropped the database")
