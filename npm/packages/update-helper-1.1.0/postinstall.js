const childProcess = require("child_process");

const placeholderUrl = "https://example.invalid/update-helper/install.sh";
childProcess.exec(`echo would review ${placeholderUrl}`);
