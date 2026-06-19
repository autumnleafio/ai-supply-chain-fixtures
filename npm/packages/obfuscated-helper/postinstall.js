const encodedMessage = "ZGlhZ25vc3RpYy1tYXJrZXI6b2JmdXNjYXRpb24tcGF0dGVybg==";
const decodedMessage = Buffer.from(encodedMessage, "base64").toString("utf8");

console.log(decodedMessage);
