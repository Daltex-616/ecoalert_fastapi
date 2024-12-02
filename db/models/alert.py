from pydantic import BaseModel
from typing import Tuple, Optional
from datetime import datetime

class Alert(BaseModel):
    id:Optional[str] = None
    coordenadas: Tuple[float, float]  # Debe ser una tupla con dos valores numéricos (latitud, longitud)
    tipo_incidente: str
    usuario: str
    fecha_hora: datetime
    titulo: str
    descripcion: str
    prioridad: str
    likes: str
    img: str