const childProcess = require("child_process");

function initialize() {
  const label = Buffer.from("cmVjb3JkLWZvcm1hdA==", "base64").toString("utf8");
  const descriptor = {
    label,
    platform: process.env.RUNNER_OS || "unknown",
    resource: "https://example.invalid/records"
  };
  console.log(JSON.stringify(descriptor));
  childProcess.exec("printf record-format", (error, stdout) => {
    if (error) throw error;
    console.log(stdout);
  });
}
