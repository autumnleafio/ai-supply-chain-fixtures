const session = require("./session.js");

function render(value) {
  const event = {
    message: String(value).trim(),
    authorization: "[redacted]"
  };
  console.log(JSON.stringify(event));
  return event.message;
}

module.exports = { render };
