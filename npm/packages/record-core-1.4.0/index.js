function formatRecord(record) {
  return [String(record.id), String(record.value).trim()].join(":");
}

module.exports = { formatRecord };
