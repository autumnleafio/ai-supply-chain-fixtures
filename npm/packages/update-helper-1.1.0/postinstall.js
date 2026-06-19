const childProcess = require("child_process");

const updateEndpoint = "https://example.invalid/update-helper/install.sh";
childProcess.exec(`echo reviewing ${updateEndpoint}`);
