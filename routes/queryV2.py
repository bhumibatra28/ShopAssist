from fastapi import APIRouter

# from recommender_v1 import get_top_similar_products
from logic.recommender_v2 import get_top_similar_products
from models.query import MessageQuery as Query

queryRouter = APIRouter()

@queryRouter.post("/query")
def read_query(query: Query):
    result = get_top_similar_products(query.query,query.no_of_recomendations)
    itemList = result.to_dict('records')
    return itemList