# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/claims/v1/claims.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/claims/v1/claims.proto',
  package='evmos.claims.v1',
  syntax='proto3',
  serialized_options=b'Z\'github.com/tharsis/evmos/x/claims/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x65vmos/claims/v1/claims.proto\x12\x0f\x65vmos.claims.v1\x1a\x14gogoproto/gogo.proto\"\x8d\x01\n\x05\x43laim\x12\'\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x17.evmos.claims.v1.Action\x12\x11\n\tcompleted\x18\x02 \x01(\x08\x12H\n\x10\x63laimable_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"\x93\x01\n\x13\x43laimsRecordAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12P\n\x18initial_claimable_amount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x19\n\x11\x61\x63tions_completed\x18\x03 \x03(\x08\"{\n\x0c\x43laimsRecord\x12P\n\x18initial_claimable_amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x19\n\x11\x61\x63tions_completed\x18\x02 \x03(\x08*\xd6\x01\n\x06\x41\x63tion\x12-\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x1a\x15\x8a\x9d \x11\x41\x63tionUnspecified\x12\x1f\n\x0b\x41\x43TION_VOTE\x10\x01\x1a\x0e\x8a\x9d \nActionVote\x12\'\n\x0f\x41\x43TION_DELEGATE\x10\x02\x1a\x12\x8a\x9d \x0e\x41\x63tionDelegate\x12\x1d\n\nACTION_EVM\x10\x03\x1a\r\x8a\x9d \tActionEVM\x12.\n\x13\x41\x43TION_IBC_TRANSFER\x10\x04\x1a\x15\x8a\x9d \x11\x41\x63tionIBCTransfer\x1a\x04\x88\xa3\x1e\x00\x42)Z\'github.com/tharsis/evmos/x/claims/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])

_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='evmos.claims.v1.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNSPECIFIED', index=0, number=0,
      serialized_options=b'\212\235 \021ActionUnspecified',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_VOTE', index=1, number=1,
      serialized_options=b'\212\235 \nActionVote',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_DELEGATE', index=2, number=2,
      serialized_options=b'\212\235 \016ActionDelegate',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_EVM', index=3, number=3,
      serialized_options=b'\212\235 \tActionEVM',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_IBC_TRANSFER', index=4, number=4,
      serialized_options=b'\212\235 \021ActionIBCTransfer',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=491,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
ACTION_UNSPECIFIED = 0
ACTION_VOTE = 1
ACTION_DELEGATE = 2
ACTION_EVM = 3
ACTION_IBC_TRANSFER = 4



_CLAIM = _descriptor.Descriptor(
  name='Claim',
  full_name='evmos.claims.v1.Claim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='evmos.claims.v1.Claim.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed', full_name='evmos.claims.v1.Claim.completed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claimable_amount', full_name='evmos.claims.v1.Claim.claimable_amount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=213,
)


_CLAIMSRECORDADDRESS = _descriptor.Descriptor(
  name='ClaimsRecordAddress',
  full_name='evmos.claims.v1.ClaimsRecordAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='evmos.claims.v1.ClaimsRecordAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_claimable_amount', full_name='evmos.claims.v1.ClaimsRecordAddress.initial_claimable_amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions_completed', full_name='evmos.claims.v1.ClaimsRecordAddress.actions_completed', index=2,
      number=3, type=8, cpp_type=7, label=3,
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
  serialized_start=216,
  serialized_end=363,
)


_CLAIMSRECORD = _descriptor.Descriptor(
  name='ClaimsRecord',
  full_name='evmos.claims.v1.ClaimsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_claimable_amount', full_name='evmos.claims.v1.ClaimsRecord.initial_claimable_amount', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions_completed', full_name='evmos.claims.v1.ClaimsRecord.actions_completed', index=1,
      number=2, type=8, cpp_type=7, label=3,
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
  serialized_start=365,
  serialized_end=488,
)

_CLAIM.fields_by_name['action'].enum_type = _ACTION
DESCRIPTOR.message_types_by_name['Claim'] = _CLAIM
DESCRIPTOR.message_types_by_name['ClaimsRecordAddress'] = _CLAIMSRECORDADDRESS
DESCRIPTOR.message_types_by_name['ClaimsRecord'] = _CLAIMSRECORD
DESCRIPTOR.enum_types_by_name['Action'] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Claim = _reflection.GeneratedProtocolMessageType('Claim', (_message.Message,), {
  'DESCRIPTOR' : _CLAIM,
  '__module__' : 'evmos.claims.v1.claims_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.Claim)
  })
_sym_db.RegisterMessage(Claim)

ClaimsRecordAddress = _reflection.GeneratedProtocolMessageType('ClaimsRecordAddress', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMSRECORDADDRESS,
  '__module__' : 'evmos.claims.v1.claims_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.ClaimsRecordAddress)
  })
_sym_db.RegisterMessage(ClaimsRecordAddress)

ClaimsRecord = _reflection.GeneratedProtocolMessageType('ClaimsRecord', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMSRECORD,
  '__module__' : 'evmos.claims.v1.claims_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.ClaimsRecord)
  })
_sym_db.RegisterMessage(ClaimsRecord)


DESCRIPTOR._options = None
_ACTION._options = None
_ACTION.values_by_name["ACTION_UNSPECIFIED"]._options = None
_ACTION.values_by_name["ACTION_VOTE"]._options = None
_ACTION.values_by_name["ACTION_DELEGATE"]._options = None
_ACTION.values_by_name["ACTION_EVM"]._options = None
_ACTION.values_by_name["ACTION_IBC_TRANSFER"]._options = None
_CLAIM.fields_by_name['claimable_amount']._options = None
_CLAIMSRECORDADDRESS.fields_by_name['initial_claimable_amount']._options = None
_CLAIMSRECORD.fields_by_name['initial_claimable_amount']._options = None
# @@protoc_insertion_point(module_scope)
