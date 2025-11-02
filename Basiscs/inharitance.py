class ServiceMonitor:
    def __init__(self, service_name, port):

        print(f"Initalizing monitor for service {service_name} on port {port}")
        self.service = service_name
        self.port = port
        self.is_alive = False


    def check(self):
        """ Stimulate Checking the service status """

        print(f"Method: Checking {self.service} on port {self.port}")
        self.is_alive = True
        print(f"Method : Status for sevrice {self.service}: {"Alive" if self.is_alive else "Down"}")
        return self.is_alive


class HttpServiceMonitor(ServiceMonitor):
    def __init__(self, url, service_name, port):
        super().__init__(service_name, port)

        self.url = url


    def ping(self):
        print(f"Method: Pinging url {self.url}")


    def check(self):
        alive = super().check()
        print(alive)
        print(f"Method: Performing Http, check on {self.url}")



http_monitor = HttpServiceMonitor("http://localhost:9000", "nginx", 90)
http_monitor.ping()
http_monitor.check()