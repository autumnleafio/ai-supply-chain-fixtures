const childProcess = require("child_process");

childProcess.execFile(process.execPath, ["--version"], (error, stdout) => {
  if (error) throw error;
  console.log(stdout.trim());
});
