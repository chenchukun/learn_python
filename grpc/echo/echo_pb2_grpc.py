# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import echo_pb2 as echo__pb2


class EchoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.echo = channel.unary_unary(
        '/Echo/echo',
        request_serializer=echo__pb2.Msg.SerializeToString,
        response_deserializer=echo__pb2.Msg.FromString,
        )


class EchoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'echo': grpc.unary_unary_rpc_method_handler(
          servicer.echo,
          request_deserializer=echo__pb2.Msg.FromString,
          response_serializer=echo__pb2.Msg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Echo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))