from fastapi import APIRouter, HTTPException
from db.models.alert import Alert
from db.schemas.alert_schema import alert_schema, alerts_schema
from db.client import db_client
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/alert",tags=["Alerts"])


def serch_alert(field:str,key):
    try:
        alert = alert_schema(db_client.ecoalert.alert({field:key}))
        return Alert(**alert)
    except:
        return {"error":"alerta no encontrada"}  


@router.get("/",response_model=list[Alert])
async def alerts():
     return alerts_schema(db_client.ecoalert.alert.find())

@router.post("/",response_model=Alert,status_code=201)
async def alert(alert:Alert):
        if type(serch_alert("id",alert.id)) == Alert:
            raise HTTPException(
                status_code=403,detail="el id de la alerta ya existe"
            )
        alert_dic = dict(alert)
        del alert_dic["id"]
        id = db_client.ecoalert.alert.insert_one(alert_dic).inserted_id
        new_alert = alert_schema(db_client.ecoalert.alert.find_one({"_id":id}))
        return Alert(**new_alert)
 