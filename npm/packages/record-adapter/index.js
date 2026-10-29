const core = require("@ai-supply-chain-fixtures/record-core");

function formatRecord(record) {
  return core.formatRecord(record);
}

module.exports = { formatRecord };
