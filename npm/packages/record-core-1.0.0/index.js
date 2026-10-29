function formatRecord(record) {
  return [String(record.id), String(record.value)].join(":");
}

module.exports = { formatRecord };
