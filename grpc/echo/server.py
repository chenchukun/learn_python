import echo_pb2
import echo_pb2_grpc
from concurrent.futures import ThreadPoolExecutor
import grpc
import time

class EchoService(echo_pb2_grpc.EchoServicer):
    def echo(self, request, context):
        return request


def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=4))
    echo_pb2_grpc.add_EchoServicer_to_server(EchoService(), server)
    server.add_insecure_port('[::]:6180')
    server.start()
    time.sleep(10000)


if __name__ == '__main__':
    main()