from fastapi import APIRouter

# from recommender_v1 import getTopSimilarProducts
from logic.recommenderV3 import getTopSimilarProducts
from models.query import MessageQuery as Query

queryRouter = APIRouter()


@queryRouter.post("/query")
def read_query(query: Query):
    try:
        result = getTopSimilarProducts(query.query, query.no_of_recomendations)
        itemList = result.to_dict('records')
        return itemList
    except:
        return {
            "message": "Some Error Occured"
        }
