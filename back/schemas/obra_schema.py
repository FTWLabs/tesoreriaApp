from typing import Optional
from datetime import date
from pydantic import BaseModel

class Obra(BaseModel):
  nombre: str
  numero: str
  fechaInicio: date
  fechaFinal: date
  director: str
  def __getitem__(self, item):
    return getattr(self, item)

class Contrato(BaseModel):
  numero: str
  nombreCliente: str
  fecha: date
  lapso: str
  def __getitem__(self, item):
    return getattr(self, item)

class Adjudicacion(BaseModel):
  consorcio: str
  grupo: str
  porcentaje: str
  presupuesto: str
  def __getitem__(self, item):
    return getattr(self, item)

class ObraGeneral(BaseModel):
  id : Optional[str]
  obra: Obra
  contrato: Contrato
  adjudicacion: Adjudicacion