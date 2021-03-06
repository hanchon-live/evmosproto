# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/intrarelayer/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.evmos.intrarelayer.v1 import intrarelayer_pb2 as evmos_dot_intrarelayer_dot_v1_dot_intrarelayer__pb2
from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/intrarelayer/v1/genesis.proto',
  package='evmos.intrarelayer.v1',
  syntax='proto3',
  serialized_options=b'Z-github.com/tharsis/evmos/x/intrarelayer/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#evmos/intrarelayer/v1/genesis.proto\x12\x15\x65vmos.intrarelayer.v1\x1a(evmos/intrarelayer/v1/intrarelayer.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"\x80\x01\n\x0cGenesisState\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1d.evmos.intrarelayer.v1.ParamsB\x04\xc8\xde\x1f\x00\x12;\n\x0btoken_pairs\x18\x02 \x03(\x0b\x32 .evmos.intrarelayer.v1.TokenPairB\x04\xc8\xde\x1f\x00\"\x98\x01\n\x06Params\x12\x1b\n\x13\x65nable_intrarelayer\x18\x01 \x01(\x08\x12\x45\n\x18token_pair_voting_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x00\x12*\n\x0f\x65nable_evm_hook\x18\x03 \x01(\x08\x42\x11\xe2\xde\x1f\rEnableEVMHookB/Z-github.com/tharsis/evmos/x/intrarelayer/typesb\x06proto3'
  ,
  dependencies=[evmos_dot_intrarelayer_dot_v1_dot_intrarelayer__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='evmos.intrarelayer.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='evmos.intrarelayer.v1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_pairs', full_name='evmos.intrarelayer.v1.GenesisState.token_pairs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=159,
  serialized_end=287,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='evmos.intrarelayer.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_intrarelayer', full_name='evmos.intrarelayer.v1.Params.enable_intrarelayer', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_pair_voting_period', full_name='evmos.intrarelayer.v1.Params.token_pair_voting_period', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\230\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_evm_hook', full_name='evmos.intrarelayer.v1.Params.enable_evm_hook', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\rEnableEVMHook', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=290,
  serialized_end=442,
)

_GENESISSTATE.fields_by_name['params'].message_type = _PARAMS
_GENESISSTATE.fields_by_name['token_pairs'].message_type = evmos_dot_intrarelayer_dot_v1_dot_intrarelayer__pb2._TOKENPAIR
_PARAMS.fields_by_name['token_pair_voting_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'evmos.intrarelayer.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.intrarelayer.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'evmos.intrarelayer.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.intrarelayer.v1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['params']._options = None
_GENESISSTATE.fields_by_name['token_pairs']._options = None
_PARAMS.fields_by_name['token_pair_voting_period']._options = None
_PARAMS.fields_by_name['enable_evm_hook']._options = None
# @@protoc_insertion_point(module_scope)
