# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/epochs/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmosproto.evmos.epochs.v1 import genesis_pb2 as evmos_dot_epochs_dot_v1_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/epochs/v1/query.proto',
  package='evmos.epochs.v1',
  syntax='proto3',
  serialized_options=b'Z\'github.com/tharsis/evmos/x/epochs/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x65vmos/epochs/v1/query.proto\x12\x0f\x65vmos.epochs.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1d\x65vmos/epochs/v1/genesis.proto\"T\n\x16QueryEpochsInfoRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x88\x01\n\x17QueryEpochsInfoResponse\x12\x30\n\x06\x65pochs\x18\x01 \x03(\x0b\x32\x1a.evmos.epochs.v1.EpochInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\".\n\x18QueryCurrentEpochRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t\"2\n\x19QueryCurrentEpochResponse\x12\x15\n\rcurrent_epoch\x18\x01 \x01(\x03\x32\x9a\x02\n\x05Query\x12\x80\x01\n\nEpochInfos\x12\'.evmos.epochs.v1.QueryEpochsInfoRequest\x1a(.evmos.epochs.v1.QueryEpochsInfoResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/evmos/epochs/v1/epochs\x12\x8d\x01\n\x0c\x43urrentEpoch\x12).evmos.epochs.v1.QueryCurrentEpochRequest\x1a*.evmos.epochs.v1.QueryCurrentEpochResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/evmos/epochs/v1/current_epochB)Z\'github.com/tharsis/evmos/x/epochs/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,evmos_dot_epochs_dot_v1_dot_genesis__pb2.DESCRIPTOR,])




_QUERYEPOCHSINFOREQUEST = _descriptor.Descriptor(
  name='QueryEpochsInfoRequest',
  full_name='evmos.epochs.v1.QueryEpochsInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.epochs.v1.QueryEpochsInfoRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=175,
  serialized_end=259,
)


_QUERYEPOCHSINFORESPONSE = _descriptor.Descriptor(
  name='QueryEpochsInfoResponse',
  full_name='evmos.epochs.v1.QueryEpochsInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='epochs', full_name='evmos.epochs.v1.QueryEpochsInfoResponse.epochs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.epochs.v1.QueryEpochsInfoResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=262,
  serialized_end=398,
)


_QUERYCURRENTEPOCHREQUEST = _descriptor.Descriptor(
  name='QueryCurrentEpochRequest',
  full_name='evmos.epochs.v1.QueryCurrentEpochRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='evmos.epochs.v1.QueryCurrentEpochRequest.identifier', index=0,
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
  serialized_start=400,
  serialized_end=446,
)


_QUERYCURRENTEPOCHRESPONSE = _descriptor.Descriptor(
  name='QueryCurrentEpochResponse',
  full_name='evmos.epochs.v1.QueryCurrentEpochResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_epoch', full_name='evmos.epochs.v1.QueryCurrentEpochResponse.current_epoch', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=448,
  serialized_end=498,
)

_QUERYEPOCHSINFOREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYEPOCHSINFORESPONSE.fields_by_name['epochs'].message_type = evmos_dot_epochs_dot_v1_dot_genesis__pb2._EPOCHINFO
_QUERYEPOCHSINFORESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
DESCRIPTOR.message_types_by_name['QueryEpochsInfoRequest'] = _QUERYEPOCHSINFOREQUEST
DESCRIPTOR.message_types_by_name['QueryEpochsInfoResponse'] = _QUERYEPOCHSINFORESPONSE
DESCRIPTOR.message_types_by_name['QueryCurrentEpochRequest'] = _QUERYCURRENTEPOCHREQUEST
DESCRIPTOR.message_types_by_name['QueryCurrentEpochResponse'] = _QUERYCURRENTEPOCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryEpochsInfoRequest = _reflection.GeneratedProtocolMessageType('QueryEpochsInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEPOCHSINFOREQUEST,
  '__module__' : 'evmos.epochs.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.epochs.v1.QueryEpochsInfoRequest)
  })
_sym_db.RegisterMessage(QueryEpochsInfoRequest)

QueryEpochsInfoResponse = _reflection.GeneratedProtocolMessageType('QueryEpochsInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEPOCHSINFORESPONSE,
  '__module__' : 'evmos.epochs.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.epochs.v1.QueryEpochsInfoResponse)
  })
_sym_db.RegisterMessage(QueryEpochsInfoResponse)

QueryCurrentEpochRequest = _reflection.GeneratedProtocolMessageType('QueryCurrentEpochRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTEPOCHREQUEST,
  '__module__' : 'evmos.epochs.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.epochs.v1.QueryCurrentEpochRequest)
  })
_sym_db.RegisterMessage(QueryCurrentEpochRequest)

QueryCurrentEpochResponse = _reflection.GeneratedProtocolMessageType('QueryCurrentEpochResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTEPOCHRESPONSE,
  '__module__' : 'evmos.epochs.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.epochs.v1.QueryCurrentEpochResponse)
  })
_sym_db.RegisterMessage(QueryCurrentEpochResponse)


DESCRIPTOR._options = None
_QUERYEPOCHSINFORESPONSE.fields_by_name['epochs']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='evmos.epochs.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=501,
  serialized_end=783,
  methods=[
  _descriptor.MethodDescriptor(
    name='EpochInfos',
    full_name='evmos.epochs.v1.Query.EpochInfos',
    index=0,
    containing_service=None,
    input_type=_QUERYEPOCHSINFOREQUEST,
    output_type=_QUERYEPOCHSINFORESPONSE,
    serialized_options=b'\202\323\344\223\002\031\022\027/evmos/epochs/v1/epochs',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CurrentEpoch',
    full_name='evmos.epochs.v1.Query.CurrentEpoch',
    index=1,
    containing_service=None,
    input_type=_QUERYCURRENTEPOCHREQUEST,
    output_type=_QUERYCURRENTEPOCHRESPONSE,
    serialized_options=b'\202\323\344\223\002 \022\036/evmos/epochs/v1/current_epoch',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
