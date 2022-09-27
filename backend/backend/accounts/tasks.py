from root.celery import app


@app.task
def test() -> str:
    return 'msg'