from invoke import task
import pytest


@task(default=True)
def default(ctx):
    unit(ctx)
    

@task
def unit(ctx):
    pytest.main(["PyController"])
    