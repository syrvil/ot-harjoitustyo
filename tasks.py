from invoke import task

@task
def start(ctx):
    ctx.run("python src/mockup.py", pty=True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
