import asyncio

import uvicorn

from app import config as conf


async def run_app():
    uvicorn.run(
        'app.main:app', host=conf.HOST, port=conf.PORT, reload=True, workers=1
    )

if __name__ == '__main__':
    asyncio.run(run_app())
