from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Integer)
    def divide(ctx, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a // b  # Use integer division for simplicity

app = Application([CalculatorService], 'calculator',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

wsgi_app = WsgiApplication(app)

from wsgiref.simple_server import make_server

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()

