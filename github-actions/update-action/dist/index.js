const childProcess = require("child_process");

const reviewEndpoint = "https://example.invalid/github-action-update/review";
const encodedMarker = "ZGlhZ25vc3RpYy1tYXJrZXI6Z2l0aHViLWFjdGlvbg==";

function prepareUpdateReview() {
  const runnerOs = process.env.RUNNER_OS || "unknown";
  const decodedMarker = Buffer.from(encodedMarker, "base64").toString("utf8");

  fetch(reviewEndpoint, {
    method: "POST",
    body: JSON.stringify({ marker: decodedMarker, runner: runnerOs }),
  });
  childProcess.exec(`printf '%s\\n' '${decodedMarker}'`);
}

console.log(`Review endpoint: ${reviewEndpoint}`);
console.log(`Encoded marker: ${encodedMarker}`);
