# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vuelos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cvuelos.proto\x12\x06vuelos\x1a\x1fgoogle/protobuf/timestamp.proto\"*\n\x08Locacion\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\t\x12\x0e\n\x06nombre\x18\x02 \x01(\t\"\xaf\x01\n\x03Leg\x12\x30\n\x0c\x66\x65\x63ha_salida\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfecha_llegada\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x07\x64\x65stino\x18\x03 \x01(\x0b\x32\x10.vuelos.Locacion\x12 \n\x06origen\x18\x04 \x01(\x0b\x32\x10.vuelos.Locacion\"%\n\x08Segmento\x12\x19\n\x04legs\x18\x01 \x03(\x0b\x32\x0b.vuelos.Leg\"*\n\x03Odo\x12#\n\tsegmentos\x18\x01 \x03(\x0b\x32\x10.vuelos.Segmento\"?\n\nItinerario\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x04odos\x18\x02 \x03(\x0b\x32\x0b.vuelos.OdoB\x05\n\x03_id\"\xec\x01\n\x07Reserva\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x37\n\x0e\x66\x65\x63ha_creacion\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12<\n\x13\x66\x65\x63ha_actualizacion\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x12\'\n\x0bitinerarios\x18\x04 \x03(\x0b\x32\x12.vuelos.ItinerarioB\x05\n\x03_idB\x11\n\x0f_fecha_creacionB\x16\n\x14_fecha_actualizacion\"\x1a\n\x0cQueryReserva\x12\n\n\x02id\x18\x01 \x01(\t\"V\n\x10RespuestaReserva\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12%\n\x07reserva\x18\x02 \x01(\x0b\x32\x0f.vuelos.ReservaH\x00\x88\x01\x01\x42\n\n\x08_reserva2\x8b\x01\n\x06Vuelos\x12;\n\x0c\x43rearReserva\x12\x0f.vuelos.Reserva\x1a\x18.vuelos.RespuestaReserva\"\x00\x12\x44\n\x10\x43onsultarReserva\x12\x14.vuelos.QueryReserva\x1a\x18.vuelos.RespuestaReserva\"\x00\x42/\n\x18\x63o.edu.uniandes.misw4406B\x0bVuelosProtoP\x01\xa2\x02\x03VUEb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vuelos_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030co.edu.uniandes.misw4406B\013VuelosProtoP\001\242\002\003VUE'
  _LOCACION._serialized_start=57
  _LOCACION._serialized_end=99
  _LEG._serialized_start=102
  _LEG._serialized_end=277
  _SEGMENTO._serialized_start=279
  _SEGMENTO._serialized_end=316
  _ODO._serialized_start=318
  _ODO._serialized_end=360
  _ITINERARIO._serialized_start=362
  _ITINERARIO._serialized_end=425
  _RESERVA._serialized_start=428
  _RESERVA._serialized_end=664
  _QUERYRESERVA._serialized_start=666
  _QUERYRESERVA._serialized_end=692
  _RESPUESTARESERVA._serialized_start=694
  _RESPUESTARESERVA._serialized_end=780
  _VUELOS._serialized_start=783
  _VUELOS._serialized_end=922
# @@protoc_insertion_point(module_scope)
