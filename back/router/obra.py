from fastapi import APIRouter, Response, HTTPException
from schemas.obra_schema import ObraGeneral, Obra
from starlette import status
from config.db import conn
from models.obras import obras

obra = APIRouter()

def transform(response):
  if type(response) != list:
    response = [response]
  result = []
  for item in response:
    count = 0
    out = {}
    for i, key in enumerate(['obra', 'contrato', 'adjudicacion']):
      out[key] = {}
      if count == 0:
        out['id'] = item[count]
        count += 1
      for j in range(len(form[i])):
        out[key][form[i][j]] = item[count]
        count += 1
    result.append(out)
  return result


form = [
  ["nombre",
  "numero",
  "fechaInicio",
  "fechaFinal",
  "director"],
  ["numero",
  "nombreCliente",
  "fecha",
  "lapso"],
  ["consorcio",
  "grupo",
  "porcentaje",
  "presupuesto"]
]

@obra.get("/", response_model=list[ObraGeneral])
async def obtener_obras():
  """
  Obtener obras
  """
  response = conn.execute(
    obras.select()
  ).fetchall()

  result = transform(response)
  return result

@obra.post("/", response_model=(ObraGeneral | str), status_code=status.HTTP_201_CREATED)
async def crear_obra(
  obra: ObraGeneral
):
  """
  Crear obra
  """
  response = conn.execute(
    obras.select().where(obras.c.id == obra.obra.numero)
  ).first()

  if response is None:
    obra_nueva = {
      "id": obra.obra.numero,
      "obra_nombre": obra.obra.nombre,
      "obra_numero": obra.obra.numero,
      "obra_fechaInicio": obra.obra.fechaInicio,
      "obra_fechaFinal": obra.obra.fechaFinal,
      "obra_director": obra.obra.director,
      "contrato_numero": obra.contrato.numero,
      "contrato_nombreCliente": obra.contrato.nombreCliente,
      "contrato_fecha": obra.contrato.fecha,
      "contrato_lapso": obra.contrato.lapso,
      "adjudicacion_consorcio": obra.adjudicacion.consorcio,
      "adjudicacion_grupo": obra.adjudicacion.grupo,
      "adjudicacion_porcentaje": obra.adjudicacion.porcentaje,
      "adjudicacion_presupuesto": obra.adjudicacion.presupuesto,
    }
    result = conn.execute(
      obras.insert().values(obra_nueva)
    )
    return Response(status_code=status.HTTP_201_CREATED)
  return "El número de obra ya existe"

@obra.get("/{id}", response_model=ObraGeneral)
async def obtener_obra(id: str):
  """
  Obtener una obra
  """
  response = conn.execute(
    obras.select().where(obras.c.id == id)
  ).first()

  if response == None:
    raise HTTPException(
      status_code=404,
      detail="La obra con este id no existe"
    )

  result = transform(response)
  return result[0]

@obra.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def borrar_obra(id: str):
  """
  Borrar obra del servidor
  """
  conn.execute(
    obras.delete().where(obras.c.id == id)
  )
  return Response(
    status_code=status.HTTP_204_NO_CONTENT
  )

@obra.put("/{id}")
async def actualizar_obra(
  id: str,
  obra: ObraGeneral
):
  obra_a_actualizar = conn.execute(
      obras.select().where(obras.c.id == id)
    ).first()

  if obra_a_actualizar == None:
    raise HTTPException(
      status_code=404,
      detail="La obra con este id no existe"
    )

  obra_a_actualizar = transform(obra_a_actualizar)[0]
  obrax = dict(obra)
  diferencias = []
  valores_cambiados = {}
  for key in obra_a_actualizar:
    if key != 'id':
      for subkey in obra_a_actualizar[key]:
        if obra_a_actualizar[key][subkey] != obrax[key][subkey]:
          diferencias.append((key, subkey))
  while len(diferencias) > 0:
    keys = diferencias[0]
    key_ = ''
    for i in range(len(keys)):
      key_ += keys[i]
      key_ += '_'
    key_ = key_[:-1]
    valores_cambiados[key_] = obrax[keys[0]][keys[1]]
    if keys == ('obra', 'numero'):
      valores_cambiados['id'] = valores_cambiados[key_]
    diferencias.pop(0)

  if valores_cambiados:
    conn.execute(
      obras.update().values(
        valores_cambiados
      ).where(
        obras.c.id == id
      )
    )

    return Response(
      status_code=status.HTTP_200_OK
    )
  else:
    return Response(
      status_code=status.HTTP_204_NO_CONTENT
    )