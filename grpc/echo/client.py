import echo_pb2
import echo_pb2_grpc
from concurrent.futures import ThreadPoolExecutor
import grpc


def main():
    channel = grpc.insecure_channel('localhost:6180')
    stub = echo_pb2_grpc.EchoStub(channel)
    while True:
        text=input()
        msg = stub.echo(echo_pb2.Msg(text=text))
        print(msg.text)


if __name__ == '__main__':
    main()