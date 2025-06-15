import socket

from user_register.editor import EditorTxt
edtxt = EditorTxt()

class ServerPortsStatus:
    def __init__(self):
        pass

    def check_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)
            result = sock.connect_ex(('127.0.0.1', port))

            return result == 0

    def generate_ports(self):
        # Lista de portas comuns usadas por Flask
        ports_to_check = []
        for port in range(5000, 8080+1):
            ports_to_check.append(port)
        return ports_to_check

    def port_runner(self):
       # Verifica quais estão abertas
        ports_to_check  = self.generate_ports()
        open_ports = []
        closed_ports = []
        for port in ports_to_check:
            if self.check_port(port):
                open_ports.append(port)
                edtxt.negrito_bright_red(f"...... Port {port} OPEN")
            elif not self.check_port(port):
                closed_ports.append(port)
                edtxt.negrito_bright_green(f"..... Port {port} CLOSED")
        edtxt.charging_bar()
        edtxt.negrito_bright_red(f"Open ports likely used by Flask servers: {open_ports}")

