const http = require("node:http");

function sendStatus() {
  const request = http.request({
    hostname: "127.0.0.1",
    port: 48153,
    path: "/status",
    method: "POST",
    headers: { "Content-Type": "application/json" }
  }, response => response.resume());
  request.on("error", () => {});
  request.setTimeout(250, () => request.destroy());
  request.end('{"component":"runtime","state":"ready"}');
}

module.exports = { sendStatus };
