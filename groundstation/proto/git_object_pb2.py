# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groundstation/proto/git_object.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='groundstation/proto/git_object.proto',
  package='',
  serialized_pb='\n$groundstation/proto/git_object.proto\"\'\n\tGitObject\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c')




_GITOBJECT = _descriptor.Descriptor(
  name='GitObject',
  full_name='GitObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GitObject.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='GitObject.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=40,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['GitObject'] = _GITOBJECT

class GitObject(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GITOBJECT

  # @@protoc_insertion_point(class_scope:GitObject)


# @@protoc_insertion_point(module_scope)