from invoke import task
import pytest

@task
def test(ctx):
    pytest.main(["PyController"])
