const endpoint = "https://example.invalid/layout";
function fetch(destination, options) {
  return { destination, method: options.method };
}
function render() { return JSON.stringify(fetch(endpoint, { method: "POST" })); }
module.exports = { render };
