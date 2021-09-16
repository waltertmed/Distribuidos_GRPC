# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='servicio.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eservicio.proto\"0\n\x04Tipo\x12\x18\n\x10tipo_medicamento\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tivo\x18\x02 \x01(\x08\"g\n\x0bMedicamento\x12\x18\n\x10nombre_comercial\x18\x01 \x01(\t\x12\x0e\n\x06\x63odigo\x18\x02 \x01(\t\x12\r\n\x05\x64roga\x18\x03 \x01(\t\x12\x1f\n\x10tipo_medicamento\x18\x04 \x01(\x0b\x32\x05.Tipo\"$\n\x0c\x43onfirmacion\x12\x14\n\x0c\x63onfirmacion\x18\x01 \x01(\t\"$\n\x0c\x43onsultaTipo\x12\x14\n\x0c\x63onfirmacion\x18\x01 \x01(\t\";\n\x11ListaMedicamentos\x12&\n\x10lst_medicamentos\x18\x01 \x03(\x0b\x32\x0c.Medicamento\"$\n\x0fRespuestaCodigo\x12\x11\n\trespuesta\x18\x01 \x01(\x08\"\x06\n\x04Nulo2\xc9\x03\n\x0c\x46\x61rmaceutica\x12\x15\n\x05Listo\x12\x05.Nulo\x1a\x05.Nulo\x12+\n\x13\x41ltaTipoMedicamento\x12\x05.Tipo\x1a\r.Confirmacion\x12+\n\x13\x42\x61jaTipoMedicamento\x12\x05.Tipo\x1a\r.Confirmacion\x12.\n\x0f\x41ltaMedicamento\x12\x0c.Medicamento\x1a\r.Confirmacion\x12?\n\x1a\x43onsultaMedicamentoPorTipo\x12\r.ConsultaTipo\x1a\x12.ListaMedicamentos\x12J\n%ConsultaMedicamentoPorNombreComercial\x12\r.ConsultaTipo\x1a\x12.ListaMedicamentos\x12+\n\x0eListaProductos\x12\x05.Nulo\x1a\x12.ListaMedicamentos\x12\x30\n\rEsPrioritario\x12\r.ConsultaTipo\x1a\x10.RespuestaCodigo\x12,\n\tVerificar\x12\r.ConsultaTipo\x1a\x10.RespuestaCodigob\x06proto3'
)




_TIPO = _descriptor.Descriptor(
  name='Tipo',
  full_name='Tipo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipo_medicamento', full_name='Tipo.tipo_medicamento', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activo', full_name='Tipo.activo', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=66,
)


_MEDICAMENTO = _descriptor.Descriptor(
  name='Medicamento',
  full_name='Medicamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nombre_comercial', full_name='Medicamento.nombre_comercial', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='codigo', full_name='Medicamento.codigo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='droga', full_name='Medicamento.droga', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tipo_medicamento', full_name='Medicamento.tipo_medicamento', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=171,
)


_CONFIRMACION = _descriptor.Descriptor(
  name='Confirmacion',
  full_name='Confirmacion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confirmacion', full_name='Confirmacion.confirmacion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=209,
)


_CONSULTATIPO = _descriptor.Descriptor(
  name='ConsultaTipo',
  full_name='ConsultaTipo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confirmacion', full_name='ConsultaTipo.confirmacion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=247,
)


_LISTAMEDICAMENTOS = _descriptor.Descriptor(
  name='ListaMedicamentos',
  full_name='ListaMedicamentos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_medicamentos', full_name='ListaMedicamentos.lst_medicamentos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=308,
)


_RESPUESTACODIGO = _descriptor.Descriptor(
  name='RespuestaCodigo',
  full_name='RespuestaCodigo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='respuesta', full_name='RespuestaCodigo.respuesta', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=346,
)


_NULO = _descriptor.Descriptor(
  name='Nulo',
  full_name='Nulo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=354,
)

_MEDICAMENTO.fields_by_name['tipo_medicamento'].message_type = _TIPO
_LISTAMEDICAMENTOS.fields_by_name['lst_medicamentos'].message_type = _MEDICAMENTO
DESCRIPTOR.message_types_by_name['Tipo'] = _TIPO
DESCRIPTOR.message_types_by_name['Medicamento'] = _MEDICAMENTO
DESCRIPTOR.message_types_by_name['Confirmacion'] = _CONFIRMACION
DESCRIPTOR.message_types_by_name['ConsultaTipo'] = _CONSULTATIPO
DESCRIPTOR.message_types_by_name['ListaMedicamentos'] = _LISTAMEDICAMENTOS
DESCRIPTOR.message_types_by_name['RespuestaCodigo'] = _RESPUESTACODIGO
DESCRIPTOR.message_types_by_name['Nulo'] = _NULO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tipo = _reflection.GeneratedProtocolMessageType('Tipo', (_message.Message,), {
  'DESCRIPTOR' : _TIPO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Tipo)
  })
_sym_db.RegisterMessage(Tipo)

Medicamento = _reflection.GeneratedProtocolMessageType('Medicamento', (_message.Message,), {
  'DESCRIPTOR' : _MEDICAMENTO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Medicamento)
  })
_sym_db.RegisterMessage(Medicamento)

Confirmacion = _reflection.GeneratedProtocolMessageType('Confirmacion', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMACION,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Confirmacion)
  })
_sym_db.RegisterMessage(Confirmacion)

ConsultaTipo = _reflection.GeneratedProtocolMessageType('ConsultaTipo', (_message.Message,), {
  'DESCRIPTOR' : _CONSULTATIPO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:ConsultaTipo)
  })
_sym_db.RegisterMessage(ConsultaTipo)

ListaMedicamentos = _reflection.GeneratedProtocolMessageType('ListaMedicamentos', (_message.Message,), {
  'DESCRIPTOR' : _LISTAMEDICAMENTOS,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:ListaMedicamentos)
  })
_sym_db.RegisterMessage(ListaMedicamentos)

RespuestaCodigo = _reflection.GeneratedProtocolMessageType('RespuestaCodigo', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTACODIGO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:RespuestaCodigo)
  })
_sym_db.RegisterMessage(RespuestaCodigo)

Nulo = _reflection.GeneratedProtocolMessageType('Nulo', (_message.Message,), {
  'DESCRIPTOR' : _NULO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Nulo)
  })
_sym_db.RegisterMessage(Nulo)



_FARMACEUTICA = _descriptor.ServiceDescriptor(
  name='Farmaceutica',
  full_name='Farmaceutica',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=357,
  serialized_end=814,
  methods=[
  _descriptor.MethodDescriptor(
    name='Listo',
    full_name='Farmaceutica.Listo',
    index=0,
    containing_service=None,
    input_type=_NULO,
    output_type=_NULO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AltaTipoMedicamento',
    full_name='Farmaceutica.AltaTipoMedicamento',
    index=1,
    containing_service=None,
    input_type=_TIPO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BajaTipoMedicamento',
    full_name='Farmaceutica.BajaTipoMedicamento',
    index=2,
    containing_service=None,
    input_type=_TIPO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AltaMedicamento',
    full_name='Farmaceutica.AltaMedicamento',
    index=3,
    containing_service=None,
    input_type=_MEDICAMENTO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConsultaMedicamentoPorTipo',
    full_name='Farmaceutica.ConsultaMedicamentoPorTipo',
    index=4,
    containing_service=None,
    input_type=_CONSULTATIPO,
    output_type=_LISTAMEDICAMENTOS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConsultaMedicamentoPorNombreComercial',
    full_name='Farmaceutica.ConsultaMedicamentoPorNombreComercial',
    index=5,
    containing_service=None,
    input_type=_CONSULTATIPO,
    output_type=_LISTAMEDICAMENTOS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListaProductos',
    full_name='Farmaceutica.ListaProductos',
    index=6,
    containing_service=None,
    input_type=_NULO,
    output_type=_LISTAMEDICAMENTOS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EsPrioritario',
    full_name='Farmaceutica.EsPrioritario',
    index=7,
    containing_service=None,
    input_type=_CONSULTATIPO,
    output_type=_RESPUESTACODIGO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Verificar',
    full_name='Farmaceutica.Verificar',
    index=8,
    containing_service=None,
    input_type=_CONSULTATIPO,
    output_type=_RESPUESTACODIGO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FARMACEUTICA)

DESCRIPTOR.services_by_name['Farmaceutica'] = _FARMACEUTICA

# @@protoc_insertion_point(module_scope)