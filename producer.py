import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5555")

    work_message = {"data" : "aaaa"}
    zmq_socket.send_json(work_message)
producer()


