# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/incentives/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from evmosproto.evmos.incentives.v1 import genesis_pb2 as evmos_dot_incentives_dot_v1_dot_genesis__pb2
from evmosproto.evmos.incentives.v1 import incentives_pb2 as evmos_dot_incentives_dot_v1_dot_incentives__pb2
from evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/incentives/v1/query.proto',
  package='evmos.incentives.v1',
  syntax='proto3',
  serialized_options=b'Z+github.com/tharsis/evmos/x/incentives/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x65vmos/incentives/v1/query.proto\x12\x13\x65vmos.incentives.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a!evmos/incentives/v1/genesis.proto\x1a$evmos/incentives/v1/incentives.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\"T\n\x16QueryIncentivesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x90\x01\n\x17QueryIncentivesResponse\x12\x38\n\nincentives\x18\x01 \x03(\x0b\x32\x1e.evmos.incentives.v1.IncentiveB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\")\n\x15QueryIncentiveRequest\x12\x10\n\x08\x63ontract\x18\x01 \x01(\t\"Q\n\x16QueryIncentiveResponse\x12\x37\n\tincentive\x18\x01 \x01(\x0b\x32\x1e.evmos.incentives.v1.IncentiveB\x04\xc8\xde\x1f\x00\"e\n\x15QueryGasMetersRequest\x12\x10\n\x08\x63ontract\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8e\x01\n\x16QueryGasMetersResponse\x12\x37\n\ngas_meters\x18\x01 \x03(\x0b\x32\x1d.evmos.incentives.v1.GasMeterB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"=\n\x14QueryGasMeterRequest\x12\x10\n\x08\x63ontract\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x02 \x01(\t\"*\n\x15QueryGasMeterResponse\x12\x11\n\tgas_meter\x18\x01 \x01(\x04\"Z\n\x1cQueryAllocationMetersRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xca\x01\n\x1dQueryAllocationMetersResponse\x12l\n\x11\x61llocation_meters\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\",\n\x1bQueryAllocationMeterRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"\x8b\x01\n\x1cQueryAllocationMeterResponse\x12k\n\x10\x61llocation_meter\x18\x01 \x01(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\"\x14\n\x12QueryParamsRequest\"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.evmos.incentives.v1.ParamsB\x04\xc8\xde\x1f\x00\x32\xd6\x08\n\x05Query\x12\x90\x01\n\nIncentives\x12+.evmos.incentives.v1.QueryIncentivesRequest\x1a,.evmos.incentives.v1.QueryIncentivesResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/incentives/v1/incentives\x12\x98\x01\n\tIncentive\x12*.evmos.incentives.v1.QueryIncentiveRequest\x1a+.evmos.incentives.v1.QueryIncentiveResponse\"2\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/incentives/{contract}\x12\x98\x01\n\tGasMeters\x12*.evmos.incentives.v1.QueryGasMetersRequest\x1a+.evmos.incentives.v1.QueryGasMetersResponse\"2\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/gas_meters/{contract}\x12\xa3\x01\n\x08GasMeter\x12).evmos.incentives.v1.QueryGasMeterRequest\x1a*.evmos.incentives.v1.QueryGasMeterResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/evmos/incentives/v1/gas_meters/{contract}/{participant}\x12\xa9\x01\n\x10\x41llocationMeters\x12\x31.evmos.incentives.v1.QueryAllocationMetersRequest\x1a\x32.evmos.incentives.v1.QueryAllocationMetersResponse\".\x82\xd3\xe4\x93\x02(\x12&/evmos/incentives/v1/allocation_meters\x12\xae\x01\n\x0f\x41llocationMeter\x12\x30.evmos.incentives.v1.QueryAllocationMeterRequest\x1a\x31.evmos.incentives.v1.QueryAllocationMeterResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./evmos/incentives/v1/allocation_meters/{denom}\x12\x80\x01\n\x06Params\x12\'.evmos.incentives.v1.QueryParamsRequest\x1a(.evmos.incentives.v1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/evmos/incentives/v1/paramsB-Z+github.com/tharsis/evmos/x/incentives/typesb\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,evmos_dot_incentives_dot_v1_dot_genesis__pb2.DESCRIPTOR,evmos_dot_incentives_dot_v1_dot_incentives__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_QUERYINCENTIVESREQUEST = _descriptor.Descriptor(
  name='QueryIncentivesRequest',
  full_name='evmos.incentives.v1.QueryIncentivesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryIncentivesRequest.pagination', index=0,
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
  serialized_start=257,
  serialized_end=341,
)


_QUERYINCENTIVESRESPONSE = _descriptor.Descriptor(
  name='QueryIncentivesResponse',
  full_name='evmos.incentives.v1.QueryIncentivesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='incentives', full_name='evmos.incentives.v1.QueryIncentivesResponse.incentives', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryIncentivesResponse.pagination', index=1,
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
  serialized_start=344,
  serialized_end=488,
)


_QUERYINCENTIVEREQUEST = _descriptor.Descriptor(
  name='QueryIncentiveRequest',
  full_name='evmos.incentives.v1.QueryIncentiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract', full_name='evmos.incentives.v1.QueryIncentiveRequest.contract', index=0,
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
  serialized_start=490,
  serialized_end=531,
)


_QUERYINCENTIVERESPONSE = _descriptor.Descriptor(
  name='QueryIncentiveResponse',
  full_name='evmos.incentives.v1.QueryIncentiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='incentive', full_name='evmos.incentives.v1.QueryIncentiveResponse.incentive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=533,
  serialized_end=614,
)


_QUERYGASMETERSREQUEST = _descriptor.Descriptor(
  name='QueryGasMetersRequest',
  full_name='evmos.incentives.v1.QueryGasMetersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract', full_name='evmos.incentives.v1.QueryGasMetersRequest.contract', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryGasMetersRequest.pagination', index=1,
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
  serialized_start=616,
  serialized_end=717,
)


_QUERYGASMETERSRESPONSE = _descriptor.Descriptor(
  name='QueryGasMetersResponse',
  full_name='evmos.incentives.v1.QueryGasMetersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_meters', full_name='evmos.incentives.v1.QueryGasMetersResponse.gas_meters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryGasMetersResponse.pagination', index=1,
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
  serialized_start=720,
  serialized_end=862,
)


_QUERYGASMETERREQUEST = _descriptor.Descriptor(
  name='QueryGasMeterRequest',
  full_name='evmos.incentives.v1.QueryGasMeterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract', full_name='evmos.incentives.v1.QueryGasMeterRequest.contract', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='participant', full_name='evmos.incentives.v1.QueryGasMeterRequest.participant', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=864,
  serialized_end=925,
)


_QUERYGASMETERRESPONSE = _descriptor.Descriptor(
  name='QueryGasMeterResponse',
  full_name='evmos.incentives.v1.QueryGasMeterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_meter', full_name='evmos.incentives.v1.QueryGasMeterResponse.gas_meter', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=927,
  serialized_end=969,
)


_QUERYALLOCATIONMETERSREQUEST = _descriptor.Descriptor(
  name='QueryAllocationMetersRequest',
  full_name='evmos.incentives.v1.QueryAllocationMetersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryAllocationMetersRequest.pagination', index=0,
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
  serialized_start=971,
  serialized_end=1061,
)


_QUERYALLOCATIONMETERSRESPONSE = _descriptor.Descriptor(
  name='QueryAllocationMetersResponse',
  full_name='evmos.incentives.v1.QueryAllocationMetersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocation_meters', full_name='evmos.incentives.v1.QueryAllocationMetersResponse.allocation_meters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.incentives.v1.QueryAllocationMetersResponse.pagination', index=1,
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
  serialized_start=1064,
  serialized_end=1266,
)


_QUERYALLOCATIONMETERREQUEST = _descriptor.Descriptor(
  name='QueryAllocationMeterRequest',
  full_name='evmos.incentives.v1.QueryAllocationMeterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='evmos.incentives.v1.QueryAllocationMeterRequest.denom', index=0,
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
  serialized_start=1268,
  serialized_end=1312,
)


_QUERYALLOCATIONMETERRESPONSE = _descriptor.Descriptor(
  name='QueryAllocationMeterResponse',
  full_name='evmos.incentives.v1.QueryAllocationMeterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocation_meter', full_name='evmos.incentives.v1.QueryAllocationMeterResponse.allocation_meter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1315,
  serialized_end=1454,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='evmos.incentives.v1.QueryParamsRequest',
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
  serialized_start=1456,
  serialized_end=1476,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='evmos.incentives.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='evmos.incentives.v1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1478,
  serialized_end=1550,
)

_QUERYINCENTIVESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYINCENTIVESRESPONSE.fields_by_name['incentives'].message_type = evmos_dot_incentives_dot_v1_dot_incentives__pb2._INCENTIVE
_QUERYINCENTIVESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYINCENTIVERESPONSE.fields_by_name['incentive'].message_type = evmos_dot_incentives_dot_v1_dot_incentives__pb2._INCENTIVE
_QUERYGASMETERSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYGASMETERSRESPONSE.fields_by_name['gas_meters'].message_type = evmos_dot_incentives_dot_v1_dot_incentives__pb2._GASMETER
_QUERYGASMETERSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYALLOCATIONMETERSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYALLOCATIONMETERSRESPONSE.fields_by_name['allocation_meters'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_QUERYALLOCATIONMETERSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYALLOCATIONMETERRESPONSE.fields_by_name['allocation_meter'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = evmos_dot_incentives_dot_v1_dot_genesis__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryIncentivesRequest'] = _QUERYINCENTIVESREQUEST
DESCRIPTOR.message_types_by_name['QueryIncentivesResponse'] = _QUERYINCENTIVESRESPONSE
DESCRIPTOR.message_types_by_name['QueryIncentiveRequest'] = _QUERYINCENTIVEREQUEST
DESCRIPTOR.message_types_by_name['QueryIncentiveResponse'] = _QUERYINCENTIVERESPONSE
DESCRIPTOR.message_types_by_name['QueryGasMetersRequest'] = _QUERYGASMETERSREQUEST
DESCRIPTOR.message_types_by_name['QueryGasMetersResponse'] = _QUERYGASMETERSRESPONSE
DESCRIPTOR.message_types_by_name['QueryGasMeterRequest'] = _QUERYGASMETERREQUEST
DESCRIPTOR.message_types_by_name['QueryGasMeterResponse'] = _QUERYGASMETERRESPONSE
DESCRIPTOR.message_types_by_name['QueryAllocationMetersRequest'] = _QUERYALLOCATIONMETERSREQUEST
DESCRIPTOR.message_types_by_name['QueryAllocationMetersResponse'] = _QUERYALLOCATIONMETERSRESPONSE
DESCRIPTOR.message_types_by_name['QueryAllocationMeterRequest'] = _QUERYALLOCATIONMETERREQUEST
DESCRIPTOR.message_types_by_name['QueryAllocationMeterResponse'] = _QUERYALLOCATIONMETERRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryIncentivesRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVESREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryIncentivesRequest)
  })
_sym_db.RegisterMessage(QueryIncentivesRequest)

QueryIncentivesResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVESRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryIncentivesResponse)
  })
_sym_db.RegisterMessage(QueryIncentivesResponse)

QueryIncentiveRequest = _reflection.GeneratedProtocolMessageType('QueryIncentiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVEREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryIncentiveRequest)
  })
_sym_db.RegisterMessage(QueryIncentiveRequest)

QueryIncentiveResponse = _reflection.GeneratedProtocolMessageType('QueryIncentiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVERESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryIncentiveResponse)
  })
_sym_db.RegisterMessage(QueryIncentiveResponse)

QueryGasMetersRequest = _reflection.GeneratedProtocolMessageType('QueryGasMetersRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGASMETERSREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryGasMetersRequest)
  })
_sym_db.RegisterMessage(QueryGasMetersRequest)

QueryGasMetersResponse = _reflection.GeneratedProtocolMessageType('QueryGasMetersResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGASMETERSRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryGasMetersResponse)
  })
_sym_db.RegisterMessage(QueryGasMetersResponse)

QueryGasMeterRequest = _reflection.GeneratedProtocolMessageType('QueryGasMeterRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGASMETERREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryGasMeterRequest)
  })
_sym_db.RegisterMessage(QueryGasMeterRequest)

QueryGasMeterResponse = _reflection.GeneratedProtocolMessageType('QueryGasMeterResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGASMETERRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryGasMeterResponse)
  })
_sym_db.RegisterMessage(QueryGasMeterResponse)

QueryAllocationMetersRequest = _reflection.GeneratedProtocolMessageType('QueryAllocationMetersRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOCATIONMETERSREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryAllocationMetersRequest)
  })
_sym_db.RegisterMessage(QueryAllocationMetersRequest)

QueryAllocationMetersResponse = _reflection.GeneratedProtocolMessageType('QueryAllocationMetersResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOCATIONMETERSRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryAllocationMetersResponse)
  })
_sym_db.RegisterMessage(QueryAllocationMetersResponse)

QueryAllocationMeterRequest = _reflection.GeneratedProtocolMessageType('QueryAllocationMeterRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOCATIONMETERREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryAllocationMeterRequest)
  })
_sym_db.RegisterMessage(QueryAllocationMeterRequest)

QueryAllocationMeterResponse = _reflection.GeneratedProtocolMessageType('QueryAllocationMeterResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOCATIONMETERRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryAllocationMeterResponse)
  })
_sym_db.RegisterMessage(QueryAllocationMeterResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'evmos.incentives.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.incentives.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYINCENTIVESRESPONSE.fields_by_name['incentives']._options = None
_QUERYINCENTIVERESPONSE.fields_by_name['incentive']._options = None
_QUERYGASMETERSRESPONSE.fields_by_name['gas_meters']._options = None
_QUERYALLOCATIONMETERSRESPONSE.fields_by_name['allocation_meters']._options = None
_QUERYALLOCATIONMETERRESPONSE.fields_by_name['allocation_meter']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='evmos.incentives.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1553,
  serialized_end=2663,
  methods=[
  _descriptor.MethodDescriptor(
    name='Incentives',
    full_name='evmos.incentives.v1.Query.Incentives',
    index=0,
    containing_service=None,
    input_type=_QUERYINCENTIVESREQUEST,
    output_type=_QUERYINCENTIVESRESPONSE,
    serialized_options=b'\202\323\344\223\002!\022\037/evmos/incentives/v1/incentives',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Incentive',
    full_name='evmos.incentives.v1.Query.Incentive',
    index=1,
    containing_service=None,
    input_type=_QUERYINCENTIVEREQUEST,
    output_type=_QUERYINCENTIVERESPONSE,
    serialized_options=b'\202\323\344\223\002,\022*/evmos/incentives/v1/incentives/{contract}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GasMeters',
    full_name='evmos.incentives.v1.Query.GasMeters',
    index=2,
    containing_service=None,
    input_type=_QUERYGASMETERSREQUEST,
    output_type=_QUERYGASMETERSRESPONSE,
    serialized_options=b'\202\323\344\223\002,\022*/evmos/incentives/v1/gas_meters/{contract}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GasMeter',
    full_name='evmos.incentives.v1.Query.GasMeter',
    index=3,
    containing_service=None,
    input_type=_QUERYGASMETERREQUEST,
    output_type=_QUERYGASMETERRESPONSE,
    serialized_options=b'\202\323\344\223\002:\0228/evmos/incentives/v1/gas_meters/{contract}/{participant}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AllocationMeters',
    full_name='evmos.incentives.v1.Query.AllocationMeters',
    index=4,
    containing_service=None,
    input_type=_QUERYALLOCATIONMETERSREQUEST,
    output_type=_QUERYALLOCATIONMETERSRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/evmos/incentives/v1/allocation_meters',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AllocationMeter',
    full_name='evmos.incentives.v1.Query.AllocationMeter',
    index=5,
    containing_service=None,
    input_type=_QUERYALLOCATIONMETERREQUEST,
    output_type=_QUERYALLOCATIONMETERRESPONSE,
    serialized_options=b'\202\323\344\223\0020\022./evmos/incentives/v1/allocation_meters/{denom}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='evmos.incentives.v1.Query.Params',
    index=6,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/evmos/incentives/v1/params',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
