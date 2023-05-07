from services import paraphrase
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/paraphrase", response_model=None, status_code=200)
def paraphrase_tree(tree: str, limit: int = 20) -> JSONResponse:
    rephrase = paraphrase.Paraphrase(tree_str=tree)
    list_of_options = rephrase.rephrase()
    if len(list_of_options) > limit:
        content = jsonable_encoder({"paraphrases": list_of_options[:limit]})
        return JSONResponse(content=content)
    else:
        content = jsonable_encoder({"paraphrases": list_of_options})
        return JSONResponse(content=content)
