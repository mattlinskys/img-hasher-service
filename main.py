import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image
import imagehash


class HashImgRequest(BaseModel):
  path: str

app = FastAPI(docs_url=None, redoc_url=None)
dataDir = os.getenv('DATA_DIR')

@app.post("/phash")
def hash_img(req: HashImgRequest):
  try:
    path = os.path.join(dataDir, req.path) if dataDir else req.path
    img = Image.open(path)
    hash = imagehash.phash(img)

    return {
      "hash": str(hash),
      "hash_binary": format(int(str(hash), 16), "040b")
    }
  except FileNotFoundError:
    raise HTTPException(status_code=404, detail="File not found")