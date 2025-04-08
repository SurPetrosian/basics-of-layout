from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Контакты</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body>
<div class="container-fluid">
  <div class="row">
    <!-- Sidebar -->
    <nav class="col-md-2 d-flex flex-column justify-content-between bg-dark text-white p-3" style="height: 100vh;">
      <div>
        <h5><i class="bi bi-bootstrap-fill me-2"></i>Меню</h5>
        <a href="#" class="d-block text-white text-decoration-none py-2"><i class="bi bi-house-door me-2"></i>Главная</a>
        <a href="#" class="d-block text-white text-decoration-none py-2"><i class="bi bi-grid me-2"></i>Категории</a>
        <a href="#" class="d-block text-white text-decoration-none py-2"><i class="bi bi-bag me-2"></i>Заказы</a>
        <a href="#" class="d-block text-white text-decoration-none py-2 bg-primary rounded"><i class="bi bi-telephone me-2"></i>Контакты</a>
      </div>
      <div class="dropdown">
        <a class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
          <img src="https://placehold.co/32x32" alt="User" class="rounded-circle me-2">
          <span>Пользователь</span>
        </a>
        <ul class="dropdown-menu dropdown-menu-dark">
          <li><a class="dropdown-item" href="#">Профиль</a></li>
          <li><a class="dropdown-item" href="#">Выход</a></li>
        </ul>
      </div>
    </nav>

    <!-- Main content -->
    <main class="col-md-10 p-5">
      <h2 class="text-center mb-5">Контакты</h2>
      <div class="row justify-content-center">
        <div class="col-md-5">
          <form class="bg-white p-4 rounded shadow-sm">
            <div class="mb-3">
              <label class="form-label">Имя</label>
              <input type="text" class="form-control">
            </div>
            <div class="mb-3">
              <label class="form-label">Почта</label>
              <div class="input-group">
                <span class="input-group-text">@</span>
                <input type="email" class="form-control">
              </div>
            </div>
            <div class="mb-3">
              <label class="form-label">Сообщение</label>
              <textarea class="form-control" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
          </form>
        </div>
        <div class="col-md-5">
          <h5 class="fw-bold">Наши контакты</h5>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...</p>
          <p class="text-muted">Все стили и скрипты загружаются через CDN.</p>
        </div>
      </div>
    </main>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(HTML_PAGE, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
