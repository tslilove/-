var JSEncrypt = require("jsencrypt");

var jsencrypt = function () {
     var a = new JSEncrypt({
                            default_key_size: "2048",
                            default_public_exponent: "10001"
                            });
     var r = 'l1ynvl0sSygWVpk',
         t = 'V0_001',
         pwd = '123456';
     a.setPublicKey("30820122300d06092a864886f70d01010105000382010f003082010a0282010100b4ee1da139f120e0a31f678bb0d9e9dab45997f3cfe20e8a2b3e93a8cab8b6b4ecd6b3e7af407e8be7ac0983767787d6be25dcbc6b975d9bf378f038699526eda869c67a630d221a15cc37ddf523038571a88d7a0b99aa2ca9fe5afd9a6f327aa3b340881a92e60bd827fbced2649053e8795119f73b04caae08e5c3c49b66a357ef0b0892a91b180aaaaf8bc153a2a70373e55bbb80ece3cada0778d56f6c9c5891a4241d3fe14dd99f483427d2819178d8d827b87ffb08f739a3301d4470194d79f6630a026ff3d6939b40bf65c591ab803adcaf4e6958b5995214f66e3a1520a3e23b4c2a94d9fc27a86973180c3b55cf2a9e4d07c210ee901352febd8a990203010001");
     var s= a.encrypt(r+pwd);
     return JSON.stringify({
            pwdEncryptVersion: t,
            encryptedPwd: s
     })
};
var t = function v() {
    for (var t = "", e = "0123456789abcdef", r = 0; r < 16; r++)
        t += e.charAt(Math.floor(16 * Math.random()));
    return t
};


console.log(t());
