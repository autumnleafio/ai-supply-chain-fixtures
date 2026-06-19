const encodedMessage = "ZW5jb2RlZCBjb25maWd1cmF0aW9uIGhlbHBlcg==";
const decodedMessage = Buffer.from(encodedMessage, "base64").toString("utf8");

console.log(decodedMessage);
