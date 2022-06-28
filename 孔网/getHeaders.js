JSEncrypt = require("jsencrypt");
var rqEncrypt =  function(randomcode) {
    var t = new JSEncrypt;
    t.setPublicKey("MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMiU6MWuUemPQkPAZSfYUBD6qfgQfM/jY3OEBbdNlOm0SBjX4Z1GMSg0Jhk70NQlxNfrbz4oN0A+jVhoH7gEyY8CAwEAAQ==");
    var e = randomcode;//KFZ.tools.cookies("randomcode");
    if (e){
        return encodeURIComponent(t.encrypt(String(e)));
    }

};
var randomcode = "12345678";
console.log(rqEncrypt(randomcode))
