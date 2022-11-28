from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def format(ctx):
    ctx.run("poetry run invoke format", pty=True)

@task 
def lint(ctx):
    ctx.run("poetry run pylint src", pty=True)