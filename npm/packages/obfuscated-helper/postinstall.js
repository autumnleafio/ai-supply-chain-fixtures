const encodedMessage = "c2FmZSByZXNlYXJjaCBmaXh0dXJlOiBvYmZ1c2NhdGlvbi1saWtlIHBhdHRlcm4gb25seQ==";
const decodedMessage = Buffer.from(encodedMessage, "base64").toString("utf8");

console.log(decodedMessage);
