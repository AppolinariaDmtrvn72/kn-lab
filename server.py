from loguru import logger
from fastapi import FastAPI
from handler import v1_router

app = FastAPI()
app.include_router(v1_router)

logger.info('Server started')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000, host='0.0.0.0', log_level='warning')
