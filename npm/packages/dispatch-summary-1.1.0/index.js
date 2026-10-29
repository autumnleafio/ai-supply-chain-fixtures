const childProcess = require("child_process");
function render() {
  if (false) { childProcess.exec("printf dispatch-ready", () => {}); }
  return "dispatch";
}
module.exports = { render };
