import argparse
import logging
from musharing_chatbot import server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--addr", default="localhost",
                        help="gRPC server address")
    parser.add_argument("--port", default=50051,
                        type=int, help="gRPC server port")
    args = parser.parse_args()

    server.serve(args.addr, args.port)


if __name__ == "__main__":
    logging.basicConfig()
    main()
