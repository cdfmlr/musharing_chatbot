import argparse
import logging
from chatbot import MusharingChatbotFactory, MusharingChatbotConfig
from chatbotapiv2 import serve_grpc, MuvtuberGrpcServerConfig


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--muvtb-grpc-serv", type=str, default="localhost:50051",
                        help="gRPC server address: host:port (e.g. localhost:50051)")
    parser.add_argument("--debug", action="store_true",
                        default=False, help="debug mode")
    args = parser.parse_args()

    config = MuvtuberGrpcServerConfig(
        chatbot_factory=MusharingChatbotFactory(),
        chatbot_config_class=MusharingChatbotConfig,
        # less max_sessions to limit memory usage
        max_sessions=3,
        address=args.muvtb_grpc_serv,
        # long timeout to keep sessions alive: no renew needed
        timeout=60*60*24*365,
        # short zombie_timeout to delete sessions at any time
        zombie_timeout=60,
        # no need to check timeout
        check_timeout_interval=60*60*24*365,
        add_reflection_service=True)

    logging.basicConfig(
        format='{asctime} {levelname} [{name}]: {message}',
        datefmt='%Y-%m-%d %H:%M:%S',
        style='{',
        level=logging.INFO if not args.debug else logging.DEBUG
    )

    try:
        serve_grpc(config)
    except InterruptedError:
        logging.info("Exiting...")
        logging.shutdown()


if __name__ == "__main__":
    main()
