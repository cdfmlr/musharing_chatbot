from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

from musharing_chatbot import chatbot
from musharing_chatbot.chatbotapi import musharing_chatbot_pb2, musharing_chatbot_pb2_grpc


class ChatbotServer(musharing_chatbot_pb2_grpc.ChatbotServiceServicer):
    def Chat(self, request, context):
        if not request.prompt:
            raise ValueError("prompt cannot be empty")
            
        return musharing_chatbot_pb2.ChatResponse(
            response=chatbot.chat(request.prompt))


def serve(addr: str, port: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    musharing_chatbot_pb2_grpc.add_ChatbotServiceServicer_to_server(
        ChatbotServer(), server)

    # the reflection service
    SERVICE_NAMES = (
        musharing_chatbot_pb2.DESCRIPTOR.services_by_name['ChatbotService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(f"{addr}:{port}")
    server.start()
    print(f"gRPC Server started at {addr}:{port}")
    server.wait_for_termination()
