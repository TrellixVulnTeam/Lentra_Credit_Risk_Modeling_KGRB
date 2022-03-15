# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pd_files.rotation_model_pb2 as rotation__model__pb2


class rotation_serviceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RotateImage = channel.unary_unary(
        '/rotation_service/RotateImage',
        request_serializer=rotation__model__pb2.rotation_requet.SerializeToString,
        response_deserializer=rotation__model__pb2.rotation_response.FromString,
        )


class rotation_serviceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RotateImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_rotation_serviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RotateImage': grpc.unary_unary_rpc_method_handler(
          servicer.RotateImage,
          request_deserializer=rotation__model__pb2.rotation_requet.FromString,
          response_serializer=rotation__model__pb2.rotation_response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rotation_service', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))