import uvicorn


def start():
    uvicorn.run("cft_test.app.api:app", host="0.0.0.0", port=8000, reload=True,)


if __name__ == '__main__':
    start()