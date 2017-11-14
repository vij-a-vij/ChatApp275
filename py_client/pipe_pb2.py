# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipe.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\npipe.proto\"\xb4\x03\n\x05Route\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x19\n\x04path\x18\x02 \x02(\x0e\x32\x0b.Route.Path\x12\x39\n\x16networkDiscoveryPacket\x18\x03 \x01(\x0b\x32\x17.NetworkDiscoveryPacketH\x00\x12\x15\n\x04user\x18\x04 \x01(\x0b\x32\x05.UserH\x00\x12\x1b\n\x07message\x18\x05 \x01(\x0b\x32\x08.MessageH\x00\x12\x15\n\x05group\x18\x06 \x01(\x0b\x32\x06.Group\x12)\n\x0fmessagesRequest\x18\x07 \x01(\x0b\x32\x10.MessagesRequest\x12*\n\x10messagesResponse\x18\x08 \x01(\x0b\x32\x10.MessagesRequest\x12\x17\n\x06header\x18\t \x01(\x0b\x32\x07.Header\"\x82\x01\n\x04Path\x12\x08\n\x04PING\x10\x00\x12\x15\n\x11NETWORK_DISCOVERY\x10\x01\x12\x08\n\x04USER\x10\x02\x12\x0b\n\x07MESSAGE\x10\x03\x12\t\n\x05GROUP\x10\x04\x12\x14\n\x10MESSAGES_REQUEST\x10\x05\x12\x15\n\x11MESSAGES_RESPONSE\x10\x06\x12\n\n\x06HEADER\x10\x07\x42\t\n\x07payload\"\xa6\x01\n\x04User\x12\r\n\x05uname\x18\x01 \x02(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x18\n\x10recentActiveTime\x18\x04 \x01(\t\x12 \n\x06\x61\x63tion\x18\x05 \x02(\x0e\x32\x10.User.ActionType\"2\n\nActionType\x12\x0c\n\x08REGISTER\x10\x00\x12\n\n\x06\x41\x43\x43\x45SS\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\"l\n\x05Group\x12\r\n\x05gname\x18\x01 \x02(\t\x12\x0b\n\x03gid\x18\x02 \x02(\x03\x12!\n\x06\x61\x63tion\x18\x03 \x02(\x0e\x32\x11.Group.ActionType\"$\n\nActionType\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\"\xa6\x02\n\x07Message\x12\x1b\n\x04type\x18\x01 \x02(\x0e\x32\r.Message.Type\x12\x10\n\x08senderId\x18\x02 \x02(\t\x12\x0f\n\x07payload\x18\x03 \x02(\t\x12\x12\n\nreceiverId\x18\x04 \x02(\t\x12\x11\n\ttimestamp\x18\x05 \x02(\t\x12\x1f\n\x06status\x18\x06 \x02(\x0e\x32\x0f.Message.Status\x12#\n\x06\x61\x63tion\x18\x07 \x02(\x0e\x32\x13.Message.ActionType\".\n\nActionType\x12\x08\n\x04POST\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\"\x1d\n\x04Type\x12\n\n\x06SINGLE\x10\x00\x12\t\n\x05GROUP\x10\x01\"\x1f\n\x06Status\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\t\n\x05STALE\x10\x01\"_\n\x0fMessagesRequest\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.MessagesRequest.Type\x12\n\n\x02id\x18\x02 \x02(\t\"\x1b\n\x04Type\x12\x08\n\x04USER\x10\x00\x12\t\n\x05GROUP\x10\x01\"}\n\x10MessagesResponse\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.MessagesResponse.Type\x12\n\n\x02id\x18\x02 \x02(\t\x12\x1a\n\x08messages\x18\x03 \x03(\x0b\x32\x08.Message\"\x1b\n\x04Type\x12\x08\n\x04USER\x10\x00\x12\t\n\x05GROUP\x10\x01\"\xd9\x02\n\x16NetworkDiscoveryPacket\x12*\n\x04mode\x18\x01 \x02(\x0e\x32\x1c.NetworkDiscoveryPacket.Mode\x12\x44\n\x06sender\x18\x02 \x02(\x0e\x32\x1e.NetworkDiscoveryPacket.Sender:\x14INTERNAL_SERVER_NODE\x12\x10\n\x08groupTag\x18\x03 \x01(\t\x12\x0e\n\x06nodeId\x18\x04 \x01(\t\x12\x13\n\x0bnodeAddress\x18\x05 \x02(\t\x12\x10\n\x08nodePort\x18\x06 \x02(\x03\x12\x0e\n\x06secret\x18\x07 \x02(\t\"Q\n\x06Sender\x12\x18\n\x14\x45XTERNAL_SERVER_NODE\x10\x00\x12\x18\n\x14INTERNAL_SERVER_NODE\x10\x01\x12\x13\n\x0f\x45ND_USER_CLIENT\x10\x02\"!\n\x04Mode\x12\x0b\n\x07REQUEST\x10\x00\x12\x0c\n\x08RESPONSE\x10\x01\"\x16\n\x06Header\x12\x0c\n\x04type\x18\x01 \x02(\tB\x0b\n\x07routingH\x01')
)



_ROUTE_PATH = _descriptor.EnumDescriptor(
  name='Path',
  full_name='Route.Path',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETWORK_DISCOVERY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGES_REQUEST', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGES_RESPONSE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADER', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=310,
  serialized_end=440,
)
_sym_db.RegisterEnumDescriptor(_ROUTE_PATH)

_USER_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='User.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=570,
  serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_USER_ACTIONTYPE)

_GROUP_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='Group.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=694,
  serialized_end=730,
)
_sym_db.RegisterEnumDescriptor(_GROUP_ACTIONTYPE)

_MESSAGE_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='Message.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=917,
  serialized_end=963,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_ACTIONTYPE)

_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Message.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINGLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=965,
  serialized_end=994,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)

_MESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Message.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STALE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=996,
  serialized_end=1027,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_STATUS)

_MESSAGESREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='MessagesRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1097,
  serialized_end=1124,
)
_sym_db.RegisterEnumDescriptor(_MESSAGESREQUEST_TYPE)

_MESSAGESRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='MessagesResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1097,
  serialized_end=1124,
)
_sym_db.RegisterEnumDescriptor(_MESSAGESRESPONSE_TYPE)

_NETWORKDISCOVERYPACKET_SENDER = _descriptor.EnumDescriptor(
  name='Sender',
  full_name='NetworkDiscoveryPacket.Sender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_SERVER_NODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_SERVER_NODE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_USER_CLIENT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1483,
  serialized_end=1564,
)
_sym_db.RegisterEnumDescriptor(_NETWORKDISCOVERYPACKET_SENDER)

_NETWORKDISCOVERYPACKET_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='NetworkDiscoveryPacket.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1566,
  serialized_end=1599,
)
_sym_db.RegisterEnumDescriptor(_NETWORKDISCOVERYPACKET_MODE)


_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Route.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='Route.path', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='networkDiscoveryPacket', full_name='Route.networkDiscoveryPacket', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='Route.user', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Route.message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='Route.group', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messagesRequest', full_name='Route.messagesRequest', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messagesResponse', full_name='Route.messagesResponse', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='Route.header', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROUTE_PATH,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='Route.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=15,
  serialized_end=451,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uname', full_name='User.uname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recentActiveTime', full_name='User.recentActiveTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='User.action', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_ACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=620,
)


_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gname', full_name='Group.gname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='Group.gid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Group.action', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GROUP_ACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=730,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='senderId', full_name='Message.senderId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Message.payload', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiverId', full_name='Message.receiverId', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Message.timestamp', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Message.status', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Message.action', index=6,
      number=7, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_ACTIONTYPE,
    _MESSAGE_TYPE,
    _MESSAGE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=1027,
)


_MESSAGESREQUEST = _descriptor.Descriptor(
  name='MessagesRequest',
  full_name='MessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='MessagesRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='MessagesRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGESREQUEST_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1029,
  serialized_end=1124,
)


_MESSAGESRESPONSE = _descriptor.Descriptor(
  name='MessagesResponse',
  full_name='MessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='MessagesResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='MessagesResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='MessagesResponse.messages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGESRESPONSE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1251,
)


_NETWORKDISCOVERYPACKET = _descriptor.Descriptor(
  name='NetworkDiscoveryPacket',
  full_name='NetworkDiscoveryPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='NetworkDiscoveryPacket.mode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='NetworkDiscoveryPacket.sender', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupTag', full_name='NetworkDiscoveryPacket.groupTag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='NetworkDiscoveryPacket.nodeId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeAddress', full_name='NetworkDiscoveryPacket.nodeAddress', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodePort', full_name='NetworkDiscoveryPacket.nodePort', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secret', full_name='NetworkDiscoveryPacket.secret', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKDISCOVERYPACKET_SENDER,
    _NETWORKDISCOVERYPACKET_MODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1254,
  serialized_end=1599,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Header.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1601,
  serialized_end=1623,
)

_ROUTE.fields_by_name['path'].enum_type = _ROUTE_PATH
_ROUTE.fields_by_name['networkDiscoveryPacket'].message_type = _NETWORKDISCOVERYPACKET
_ROUTE.fields_by_name['user'].message_type = _USER
_ROUTE.fields_by_name['message'].message_type = _MESSAGE
_ROUTE.fields_by_name['group'].message_type = _GROUP
_ROUTE.fields_by_name['messagesRequest'].message_type = _MESSAGESREQUEST
_ROUTE.fields_by_name['messagesResponse'].message_type = _MESSAGESREQUEST
_ROUTE.fields_by_name['header'].message_type = _HEADER
_ROUTE_PATH.containing_type = _ROUTE
_ROUTE.oneofs_by_name['payload'].fields.append(
  _ROUTE.fields_by_name['networkDiscoveryPacket'])
_ROUTE.fields_by_name['networkDiscoveryPacket'].containing_oneof = _ROUTE.oneofs_by_name['payload']
_ROUTE.oneofs_by_name['payload'].fields.append(
  _ROUTE.fields_by_name['user'])
_ROUTE.fields_by_name['user'].containing_oneof = _ROUTE.oneofs_by_name['payload']
_ROUTE.oneofs_by_name['payload'].fields.append(
  _ROUTE.fields_by_name['message'])
_ROUTE.fields_by_name['message'].containing_oneof = _ROUTE.oneofs_by_name['payload']
_USER.fields_by_name['action'].enum_type = _USER_ACTIONTYPE
_USER_ACTIONTYPE.containing_type = _USER
_GROUP.fields_by_name['action'].enum_type = _GROUP_ACTIONTYPE
_GROUP_ACTIONTYPE.containing_type = _GROUP
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['status'].enum_type = _MESSAGE_STATUS
_MESSAGE.fields_by_name['action'].enum_type = _MESSAGE_ACTIONTYPE
_MESSAGE_ACTIONTYPE.containing_type = _MESSAGE
_MESSAGE_TYPE.containing_type = _MESSAGE
_MESSAGE_STATUS.containing_type = _MESSAGE
_MESSAGESREQUEST.fields_by_name['type'].enum_type = _MESSAGESREQUEST_TYPE
_MESSAGESREQUEST_TYPE.containing_type = _MESSAGESREQUEST
_MESSAGESRESPONSE.fields_by_name['type'].enum_type = _MESSAGESRESPONSE_TYPE
_MESSAGESRESPONSE.fields_by_name['messages'].message_type = _MESSAGE
_MESSAGESRESPONSE_TYPE.containing_type = _MESSAGESRESPONSE
_NETWORKDISCOVERYPACKET.fields_by_name['mode'].enum_type = _NETWORKDISCOVERYPACKET_MODE
_NETWORKDISCOVERYPACKET.fields_by_name['sender'].enum_type = _NETWORKDISCOVERYPACKET_SENDER
_NETWORKDISCOVERYPACKET_SENDER.containing_type = _NETWORKDISCOVERYPACKET
_NETWORKDISCOVERYPACKET_MODE.containing_type = _NETWORKDISCOVERYPACKET
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessagesRequest'] = _MESSAGESREQUEST
DESCRIPTOR.message_types_by_name['MessagesResponse'] = _MESSAGESRESPONSE
DESCRIPTOR.message_types_by_name['NetworkDiscoveryPacket'] = _NETWORKDISCOVERYPACKET
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), dict(
  DESCRIPTOR = _ROUTE,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:Route)
  ))
_sym_db.RegisterMessage(Route)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), dict(
  DESCRIPTOR = _GROUP,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:Group)
  ))
_sym_db.RegisterMessage(Group)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)

MessagesRequest = _reflection.GeneratedProtocolMessageType('MessagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGESREQUEST,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:MessagesRequest)
  ))
_sym_db.RegisterMessage(MessagesRequest)

MessagesResponse = _reflection.GeneratedProtocolMessageType('MessagesResponse', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGESRESPONSE,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:MessagesResponse)
  ))
_sym_db.RegisterMessage(MessagesResponse)

NetworkDiscoveryPacket = _reflection.GeneratedProtocolMessageType('NetworkDiscoveryPacket', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKDISCOVERYPACKET,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:NetworkDiscoveryPacket)
  ))
_sym_db.RegisterMessage(NetworkDiscoveryPacket)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  ))
_sym_db.RegisterMessage(Header)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\007routingH\001'))
# @@protoc_insertion_point(module_scope)
