def alert_schema(alert) -> dict:
    return {
        "id":str(alert["_id"]),
        "coordenadas": alert.get("coordenadas"),
        "tipo_incidente": alert.get("tipo_incidente"),
        "usuario": alert.get("usuario"),
        "fecha_hora": alert.get("fecha_hora"),
        "titulo": alert.get("titulo"),
        "descripcion": alert.get("descripcion"),
        "prioridad": alert.get("prioridad"),
        "likes": alert.get("likes"),
        "img": alert.get("img"),
    }
    

# para pasar de jason a diccionario

def alerts_schema(alerts) -> list:
    return [alert_schema(alert) for alert in alerts]