const endpoint = "https://example.invalid/layout";
function render() { return JSON.stringify({ endpoint, method: "POST" }); }
module.exports = { render };
