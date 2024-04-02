from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Отвечает за обработку входящих запросов от клиентов.
    """

    def __get_index(self):
        """
        Возвращает многострочное содержимое - html-разметку страницы.
        """
        with open('index.html') as file:
            html_file = file.read()
            return html_file

    def do_GET(self):
        """
        Обрабатывает входящие GET-запросы.
        """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped')
