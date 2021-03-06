# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from evmosproto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from evmosproto.ethermint.evm.v1 import evm_pb2 as ethermint_dot_evm_dot_v1_dot_evm__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/evm/v1/tx.proto',
  package='ethermint.evm.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/tharsis/ethermint/x/evm/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x65thermint/evm/v1/tx.proto\x12\x10\x65thermint.evm.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1a\x65thermint/evm/v1/evm.proto\"w\n\rMsgEthereumTx\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x13\n\x04size\x18\x02 \x01(\x01\x42\x05\xea\xde\x1f\x01-\x12\x19\n\x04hash\x18\x03 \x01(\tB\x0b\xf2\xde\x1f\x07rlp:\"-\"\x12\x0c\n\x04\x66rom\x18\x04 \x01(\t:\x04\x88\xa0\x1f\x00\"\x83\x02\n\x08LegacyTx\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12=\n\tgas_price\x18\x02 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x03 \x01(\x04\x42\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x04 \x01(\t\x12\x43\n\x05value\x18\x05 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06\x41mount\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\t\n\x01v\x18\x07 \x01(\x0c\x12\t\n\x01r\x18\x08 \x01(\x0c\x12\t\n\x01s\x18\t \x01(\x0c:\x0e\x88\xa0\x1f\x00\xd2\xb4-\x06TxData\"\xae\x03\n\x0c\x41\x63\x63\x65ssListTx\x12R\n\x08\x63hain_id\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07\x43hainID\xea\xde\x1f\x07\x63hainID\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12=\n\tgas_price\x18\x03 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x04 \x01(\x04\x42\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x05 \x01(\t\x12\x43\n\x05value\x18\x06 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06\x41mount\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\x12Q\n\x08\x61\x63\x63\x65sses\x18\x08 \x03(\x0b\x32\x1d.ethermint.evm.v1.AccessTupleB \xaa\xdf\x1f\nAccessList\xea\xde\x1f\naccessList\xc8\xde\x1f\x00\x12\t\n\x01v\x18\t \x01(\x0c\x12\t\n\x01r\x18\n \x01(\x0c\x12\t\n\x01s\x18\x0b \x01(\x0c:\x0e\x88\xa0\x1f\x00\xd2\xb4-\x06TxData\"\xf1\x03\n\x0c\x44ynamicFeeTx\x12R\n\x08\x63hain_id\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07\x43hainID\xea\xde\x1f\x07\x63hainID\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12?\n\x0bgas_tip_cap\x18\x03 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12?\n\x0bgas_fee_cap\x18\x04 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x05 \x01(\x04\x42\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x06 \x01(\t\x12\x43\n\x05value\x18\x07 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06\x41mount\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\x12Q\n\x08\x61\x63\x63\x65sses\x18\t \x03(\x0b\x32\x1d.ethermint.evm.v1.AccessTupleB \xaa\xdf\x1f\nAccessList\xea\xde\x1f\naccessList\xc8\xde\x1f\x00\x12\t\n\x01v\x18\n \x01(\x0c\x12\t\n\x01r\x18\x0b \x01(\x0c\x12\t\n\x01s\x18\x0c \x01(\x0c:\x0e\x88\xa0\x1f\x00\xd2\xb4-\x06TxData\"\"\n\x1a\x45xtensionOptionsEthereumTx:\x04\x88\xa0\x1f\x00\"\x81\x01\n\x15MsgEthereumTxResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12#\n\x04logs\x18\x02 \x03(\x0b\x32\x15.ethermint.evm.v1.Log\x12\x0b\n\x03ret\x18\x03 \x01(\x0c\x12\x10\n\x08vm_error\x18\x04 \x01(\t\x12\x10\n\x08gas_used\x18\x05 \x01(\x04:\x04\x88\xa0\x1f\x00\x32]\n\x03Msg\x12V\n\nEthereumTx\x12\x1f.ethermint.evm.v1.MsgEthereumTx\x1a\'.ethermint.evm.v1.MsgEthereumTxResponseB*Z(github.com/tharsis/ethermint/x/evm/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,ethermint_dot_evm_dot_v1_dot_evm__pb2.DESCRIPTOR,])




_MSGETHEREUMTX = _descriptor.Descriptor(
  name='MsgEthereumTx',
  full_name='ethermint.evm.v1.MsgEthereumTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ethermint.evm.v1.MsgEthereumTx.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='ethermint.evm.v1.MsgEthereumTx.size', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\001-', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ethermint.evm.v1.MsgEthereumTx.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\007rlp:\"-\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from', full_name='ethermint.evm.v1.MsgEthereumTx.from', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=270,
)


_LEGACYTX = _descriptor.Descriptor(
  name='LegacyTx',
  full_name='ethermint.evm.v1.LegacyTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='ethermint.evm.v1.LegacyTx.nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='ethermint.evm.v1.LegacyTx.gas_price', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas', full_name='ethermint.evm.v1.LegacyTx.gas', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\010GasLimit', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='ethermint.evm.v1.LegacyTx.to', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ethermint.evm.v1.LegacyTx.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\006Amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethermint.evm.v1.LegacyTx.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='ethermint.evm.v1.LegacyTx.v', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r', full_name='ethermint.evm.v1.LegacyTx.r', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s', full_name='ethermint.evm.v1.LegacyTx.s', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\322\264-\006TxData',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=532,
)


_ACCESSLISTTX = _descriptor.Descriptor(
  name='AccessListTx',
  full_name='ethermint.evm.v1.AccessListTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='ethermint.evm.v1.AccessListTx.chain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\007ChainID\352\336\037\007chainID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='ethermint.evm.v1.AccessListTx.nonce', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='ethermint.evm.v1.AccessListTx.gas_price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas', full_name='ethermint.evm.v1.AccessListTx.gas', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\010GasLimit', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='ethermint.evm.v1.AccessListTx.to', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ethermint.evm.v1.AccessListTx.value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\006Amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethermint.evm.v1.AccessListTx.data', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accesses', full_name='ethermint.evm.v1.AccessListTx.accesses', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\nAccessList\352\336\037\naccessList\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='ethermint.evm.v1.AccessListTx.v', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r', full_name='ethermint.evm.v1.AccessListTx.r', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s', full_name='ethermint.evm.v1.AccessListTx.s', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\322\264-\006TxData',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=965,
)


_DYNAMICFEETX = _descriptor.Descriptor(
  name='DynamicFeeTx',
  full_name='ethermint.evm.v1.DynamicFeeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='ethermint.evm.v1.DynamicFeeTx.chain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\007ChainID\352\336\037\007chainID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='ethermint.evm.v1.DynamicFeeTx.nonce', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_tip_cap', full_name='ethermint.evm.v1.DynamicFeeTx.gas_tip_cap', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_fee_cap', full_name='ethermint.evm.v1.DynamicFeeTx.gas_fee_cap', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas', full_name='ethermint.evm.v1.DynamicFeeTx.gas', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\010GasLimit', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='ethermint.evm.v1.DynamicFeeTx.to', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ethermint.evm.v1.DynamicFeeTx.value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\006Amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethermint.evm.v1.DynamicFeeTx.data', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accesses', full_name='ethermint.evm.v1.DynamicFeeTx.accesses', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\nAccessList\352\336\037\naccessList\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='ethermint.evm.v1.DynamicFeeTx.v', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r', full_name='ethermint.evm.v1.DynamicFeeTx.r', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s', full_name='ethermint.evm.v1.DynamicFeeTx.s', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\322\264-\006TxData',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1465,
)


_EXTENSIONOPTIONSETHEREUMTX = _descriptor.Descriptor(
  name='ExtensionOptionsEthereumTx',
  full_name='ethermint.evm.v1.ExtensionOptionsEthereumTx',
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
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1467,
  serialized_end=1501,
)


_MSGETHEREUMTXRESPONSE = _descriptor.Descriptor(
  name='MsgEthereumTxResponse',
  full_name='ethermint.evm.v1.MsgEthereumTxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ethermint.evm.v1.MsgEthereumTxResponse.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='ethermint.evm.v1.MsgEthereumTxResponse.logs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ret', full_name='ethermint.evm.v1.MsgEthereumTxResponse.ret', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vm_error', full_name='ethermint.evm.v1.MsgEthereumTxResponse.vm_error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='ethermint.evm.v1.MsgEthereumTxResponse.gas_used', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1504,
  serialized_end=1633,
)

_MSGETHEREUMTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ACCESSLISTTX.fields_by_name['accesses'].message_type = ethermint_dot_evm_dot_v1_dot_evm__pb2._ACCESSTUPLE
_DYNAMICFEETX.fields_by_name['accesses'].message_type = ethermint_dot_evm_dot_v1_dot_evm__pb2._ACCESSTUPLE
_MSGETHEREUMTXRESPONSE.fields_by_name['logs'].message_type = ethermint_dot_evm_dot_v1_dot_evm__pb2._LOG
DESCRIPTOR.message_types_by_name['MsgEthereumTx'] = _MSGETHEREUMTX
DESCRIPTOR.message_types_by_name['LegacyTx'] = _LEGACYTX
DESCRIPTOR.message_types_by_name['AccessListTx'] = _ACCESSLISTTX
DESCRIPTOR.message_types_by_name['DynamicFeeTx'] = _DYNAMICFEETX
DESCRIPTOR.message_types_by_name['ExtensionOptionsEthereumTx'] = _EXTENSIONOPTIONSETHEREUMTX
DESCRIPTOR.message_types_by_name['MsgEthereumTxResponse'] = _MSGETHEREUMTXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgEthereumTx = _reflection.GeneratedProtocolMessageType('MsgEthereumTx', (_message.Message,), {
  'DESCRIPTOR' : _MSGETHEREUMTX,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.MsgEthereumTx)
  })
_sym_db.RegisterMessage(MsgEthereumTx)

LegacyTx = _reflection.GeneratedProtocolMessageType('LegacyTx', (_message.Message,), {
  'DESCRIPTOR' : _LEGACYTX,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.LegacyTx)
  })
_sym_db.RegisterMessage(LegacyTx)

AccessListTx = _reflection.GeneratedProtocolMessageType('AccessListTx', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSLISTTX,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.AccessListTx)
  })
_sym_db.RegisterMessage(AccessListTx)

DynamicFeeTx = _reflection.GeneratedProtocolMessageType('DynamicFeeTx', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICFEETX,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.DynamicFeeTx)
  })
_sym_db.RegisterMessage(DynamicFeeTx)

ExtensionOptionsEthereumTx = _reflection.GeneratedProtocolMessageType('ExtensionOptionsEthereumTx', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONOPTIONSETHEREUMTX,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.ExtensionOptionsEthereumTx)
  })
_sym_db.RegisterMessage(ExtensionOptionsEthereumTx)

MsgEthereumTxResponse = _reflection.GeneratedProtocolMessageType('MsgEthereumTxResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGETHEREUMTXRESPONSE,
  '__module__' : 'ethermint.evm.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.MsgEthereumTxResponse)
  })
_sym_db.RegisterMessage(MsgEthereumTxResponse)


DESCRIPTOR._options = None
_MSGETHEREUMTX.fields_by_name['size']._options = None
_MSGETHEREUMTX.fields_by_name['hash']._options = None
_MSGETHEREUMTX._options = None
_LEGACYTX.fields_by_name['gas_price']._options = None
_LEGACYTX.fields_by_name['gas']._options = None
_LEGACYTX.fields_by_name['value']._options = None
_LEGACYTX._options = None
_ACCESSLISTTX.fields_by_name['chain_id']._options = None
_ACCESSLISTTX.fields_by_name['gas_price']._options = None
_ACCESSLISTTX.fields_by_name['gas']._options = None
_ACCESSLISTTX.fields_by_name['value']._options = None
_ACCESSLISTTX.fields_by_name['accesses']._options = None
_ACCESSLISTTX._options = None
_DYNAMICFEETX.fields_by_name['chain_id']._options = None
_DYNAMICFEETX.fields_by_name['gas_tip_cap']._options = None
_DYNAMICFEETX.fields_by_name['gas_fee_cap']._options = None
_DYNAMICFEETX.fields_by_name['gas']._options = None
_DYNAMICFEETX.fields_by_name['value']._options = None
_DYNAMICFEETX.fields_by_name['accesses']._options = None
_DYNAMICFEETX._options = None
_EXTENSIONOPTIONSETHEREUMTX._options = None
_MSGETHEREUMTXRESPONSE._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='ethermint.evm.v1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1635,
  serialized_end=1728,
  methods=[
  _descriptor.MethodDescriptor(
    name='EthereumTx',
    full_name='ethermint.evm.v1.Msg.EthereumTx',
    index=0,
    containing_service=None,
    input_type=_MSGETHEREUMTX,
    output_type=_MSGETHEREUMTXRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
