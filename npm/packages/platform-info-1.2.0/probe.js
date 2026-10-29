const childProcess = require("child_process");
function version() {
  return childProcess.execFileSync(process.execPath, ["--version"], { encoding: "utf8" }).trim();
}
module.exports = { version };
