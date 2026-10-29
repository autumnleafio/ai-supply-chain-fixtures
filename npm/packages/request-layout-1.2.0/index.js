const https = require("./transport.js");
function render() {
  return JSON.stringify(https.request({ hostname: "example.invalid", path: "/layout", method: "POST" }));
}
module.exports = { render };
