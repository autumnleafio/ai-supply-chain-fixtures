const childProcess = require("child_process");

// Safe synthetic fixture for MSc supply chain research.
// This does not contact the network, exfiltrate data, or modify the host.
// The placeholder URL is present only so evidence extraction can reason about
// suspicious-looking update-time behavior without executing harmful code.
const placeholderUrl = "https://example.invalid/update-helper/install.sh";
childProcess.exec(`echo safe research fixture only: would review ${placeholderUrl}`);
