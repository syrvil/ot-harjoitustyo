from invoke import task

@task
def start(ctx):
    ctx.run("python src/mockup.py", pty=True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
