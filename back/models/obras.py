from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine


obras = Table(
  "obras", meta,
  Column(
    "id",
    String(100),
    primary_key=True
  ),
  Column(
    "obra_nombre",
    String(100),
  ),
  Column(
    "obra_numero",
    String(100)
  ),
  Column(
    "obra_fechaInicio",
    Date,
  ),
  Column(
    "obra_fechaFinal",
    Date
  ),
  Column(
    "obra_director",
    String(100)
  ),
  Column(
    "contrato_numero",
    String(100)
  ),
  Column(
    "contrato_nombreCliente",
    String(100)
  ),
  Column(
    "contrato_fecha",
    Date
  ),
  Column(
    "contrato_lapso",
    String(100)
  ),
  Column(
    "adjudicacion_consorcio",
    String(100)
  ),
  Column(
    "adjudicacion_grupo",
    String(100)
  ),
  Column(
    "adjudicacion_porcentaje",
    String(100)
  ),
  Column(
    "adjudicacion_presupuesto",
    String(100)
  ),
)

meta.create_all(engine)