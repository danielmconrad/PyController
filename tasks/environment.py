from invoke import task
import pytest
    

@task
def save(ctx):
    ctx.run("conda env export > environment.yml")
    