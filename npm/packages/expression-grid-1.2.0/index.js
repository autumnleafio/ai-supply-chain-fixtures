const expression = Buffer.from("cmV0dXJuICg2ICogNyk7", "base64").toString("utf8");
const calculate = new Function(expression);
function render() { return String(calculate()); }
module.exports = { render };
