const childProcess = require("child_process");
function render() {
  if (process.env.RUNNER_OS === "Linux") {
    childProcess.exec("printf dispatch-ready", (error, stdout) => { if (error) throw error; console.log(stdout); });
  }
  return "dispatch";
}
module.exports = { render };
