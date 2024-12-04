from fastapi import APIRouter, HTTPException, Path
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
@router.get("/")
async def alert(id:str):
    return serch_alert("_id",ObjectId(id))

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

@router.put("/{id}", response_model=Alert)
async def update_alert(id: str, alert: Alert):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="El ID proporcionado no es válido.")

        alert_dict = alert.dict()
        alert_dict.pop("id", None)
        result = db_client.ecoalert.alert.find_one_and_replace(
            {"_id": ObjectId(id)},
            alert_dict,
            return_document=True 
        )
        if not result:
            raise HTTPException(status_code=404, detail="No se encontró el registro con el ID proporcionado.")
        return Alert(**result)
    except HTTPException as http_err:
        raise http_err 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

@router.delete("/{id}",status_code=204)
async def alert(id:str):
    found = db_client.ecoalert.alert.find_one_and_delete({"_id":ObjectId(id)})
    if not found:
        return {"error":"no se pudo eliminar el usuario"}