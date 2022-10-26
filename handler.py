from pathlib import Path
from fastapi import APIRouter, File
import numpy as np
from keras.models import load_model
import cv2


# from schema import PictureSchema
from base_handler import BaseHandler

v1_router = APIRouter()

model_path = Path('model.h5')
assert model_path.exists(), Path('.').absolute()
model = load_model(model_path)

handler = BaseHandler(model=model)


@v1_router.post("/getPostsScoring")
async def root(pic: bytes = File(...),):
    with open('./tmp.png', 'wb') as f:
        f.write(pic)

    img = cv2.imread('tmp.png')
    img = cv2.resize(img, (30, 30))
    img = np.reshape(img, [1, 30, 30, 3])

    classes = model.predict(img).tolist()[0]
    classes = [{'label': label, 'prob': prob} for label, prob in zip(range(len(classes)), classes)]
    return {'class_probabilities': classes}



