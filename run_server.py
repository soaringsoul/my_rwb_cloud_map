import http.server
import socketserver

# 设置端口号
PORT = 8080

# 定义处理请求的类
Handler = http.server.SimpleHTTPRequestHandler

# 创建一个 TCP 服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # 启动服务器，直到手动停止
    httpd.serve_forever()
