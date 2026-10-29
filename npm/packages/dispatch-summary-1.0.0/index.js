const childProcess = require("child_process");
function render() { return JSON.stringify({ runner: typeof childProcess.exec, mode: "summary" }); }
module.exports = { render };
