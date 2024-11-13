from fastapi import FastAPI



app = FastAPI()


@app.get('/helloworld')
async def helloWorld():
    return "Hello Welcome To Fast API"