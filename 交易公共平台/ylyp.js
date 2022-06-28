/*
cc02fdfe5cf8d78fe21601309784293c

{"ts":1651819450407,"KIND":"YLYP","timeType":"6","BeginTime":"2021-11-06 00:00:00","EndTime":"2022-05-06 23:59:59","createTime":[],"pageNo":2,"pageSize":10,"total":14565}
http://ggzy.zwfwb.tj.gov.cn/queryContent-jyxx.jspx
*/
/*
Md5算法
 */
var buffer = new ArrayBuffer(68)
    ,buffer8 = new Uint8Array(buffer)
    blocks = new Uint32Array(buffer);
var ARRAY_BUFFER = true;
var EXTRA = [128, 32768, 8388608, -2147483648];
var HEX_CHARS = "0123456789abcdef".split("")
    , EXTRA = [128, 32768, 8388608, -2147483648]
    , SHIFT = [0, 8, 16, 24]
    , OUTPUT_TYPES = ["hex", "array", "digest", "buffer", "arrayBuffer", "base64"]
    , BASE64_ENCODE_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".split("")
    ;
function Md5(t) {
    if (t)
        blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] = blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0,
        this.blocks = blocks,
        this.buffer8 = buffer8;
    else if (ARRAY_BUFFER) {
        var e = new ArrayBuffer(68);
        this.buffer8 = new Uint8Array(e),
        this.blocks = new Uint32Array(e)
    } else
        this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0,
    this.finalized = this.hashed = !1,
    this.first = !0
}
Md5.prototype.update = function(t) {
    if (!this.finalized) {
        var e, n = typeof t;
        if ("string" !== n) {
            if ("object" !== n)
                throw ERROR;
            if (null === t)
                throw ERROR;
            if (ARRAY_BUFFER && t.constructor === ArrayBuffer)
                t = new Uint8Array(t);
            else if (!Array.isArray(t) && (!ARRAY_BUFFER || !ArrayBuffer.isView(t)))
                throw ERROR;
            e = !0
        }
        var r, i, o = 0, c = t.length, a = this.blocks, A = this.buffer8;
        while (o < c) {
            if (this.hashed && (this.hashed = !1,
            a[0] = a[16],
            a[16] = a[1] = a[2] = a[3] = a[4] = a[5] = a[6] = a[7] = a[8] = a[9] = a[10] = a[11] = a[12] = a[13] = a[14] = a[15] = 0),
            e)
                if (ARRAY_BUFFER)
                    for (i = this.start; o < c && i < 64; ++o)
                        A[i++] = t[o];
                else
                    for (i = this.start; o < c && i < 64; ++o)
                        a[i >> 2] |= t[o] << SHIFT[3 & i++];
            else if (ARRAY_BUFFER)
                for (i = this.start; o < c && i < 64; ++o)
                    r = t.charCodeAt(o),
                    r < 128 ? A[i++] = r : r < 2048 ? (A[i++] = 192 | r >> 6,
                    A[i++] = 128 | 63 & r) : r < 55296 || r >= 57344 ? (A[i++] = 224 | r >> 12,
                    A[i++] = 128 | r >> 6 & 63,
                    A[i++] = 128 | 63 & r) : (r = 65536 + ((1023 & r) << 10 | 1023 & t.charCodeAt(++o)),
                    A[i++] = 240 | r >> 18,
                    A[i++] = 128 | r >> 12 & 63,
                    A[i++] = 128 | r >> 6 & 63,
                    A[i++] = 128 | 63 & r);
            else
                for (i = this.start; o < c && i < 64; ++o)
                    r = t.charCodeAt(o),
                    r < 128 ? a[i >> 2] |= r << SHIFT[3 & i++] : r < 2048 ? (a[i >> 2] |= (192 | r >> 6) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | 63 & r) << SHIFT[3 & i++]) : r < 55296 || r >= 57344 ? (a[i >> 2] |= (224 | r >> 12) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | r >> 6 & 63) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | 63 & r) << SHIFT[3 & i++]) : (r = 65536 + ((1023 & r) << 10 | 1023 & t.charCodeAt(++o)),
                    a[i >> 2] |= (240 | r >> 18) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | r >> 12 & 63) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | r >> 6 & 63) << SHIFT[3 & i++],
                    a[i >> 2] |= (128 | 63 & r) << SHIFT[3 & i++]);
            this.lastByteIndex = i,
            this.bytes += i - this.start,
            i >= 64 ? (this.start = i - 64,
            this.hash(),
            this.hashed = !0) : this.start = i
        }
        return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0,
        this.bytes = this.bytes % 4294967296),
        this
    }
}
,
Md5.prototype.finalize = function() {
    if (!this.finalized) {
        this.finalized = !0;
        var t = this.blocks
          , e = this.lastByteIndex;
        t[e >> 2] |= EXTRA[3 & e],
        e >= 56 && (this.hashed || this.hash(),
        t[0] = t[16],
        t[16] = t[1] = t[2] = t[3] = t[4] = t[5] = t[6] = t[7] = t[8] = t[9] = t[10] = t[11] = t[12] = t[13] = t[14] = t[15] = 0),
        t[14] = this.bytes << 3,
        t[15] = this.hBytes << 3 | this.bytes >>> 29,
        this.hash()
    }
}
,
Md5.prototype.hash = function() {
    var t, e, n, r, i, o, c = this.blocks;
    this.first ? (t = c[0] - 680876937,
    t = (t << 7 | t >>> 25) - 271733879 << 0,
    r = (-1732584194 ^ 2004318071 & t) + c[1] - 117830708,
    r = (r << 12 | r >>> 20) + t << 0,
    n = (-271733879 ^ r & (-271733879 ^ t)) + c[2] - 1126478375,
    n = (n << 17 | n >>> 15) + r << 0,
    e = (t ^ n & (r ^ t)) + c[3] - 1316259209,
    e = (e << 22 | e >>> 10) + n << 0) : (t = this.h0,
    e = this.h1,
    n = this.h2,
    r = this.h3,
    t += (r ^ e & (n ^ r)) + c[0] - 680876936,
    t = (t << 7 | t >>> 25) + e << 0,
    r += (n ^ t & (e ^ n)) + c[1] - 389564586,
    r = (r << 12 | r >>> 20) + t << 0,
    n += (e ^ r & (t ^ e)) + c[2] + 606105819,
    n = (n << 17 | n >>> 15) + r << 0,
    e += (t ^ n & (r ^ t)) + c[3] - 1044525330,
    e = (e << 22 | e >>> 10) + n << 0),
    t += (r ^ e & (n ^ r)) + c[4] - 176418897,
    t = (t << 7 | t >>> 25) + e << 0,
    r += (n ^ t & (e ^ n)) + c[5] + 1200080426,
    r = (r << 12 | r >>> 20) + t << 0,
    n += (e ^ r & (t ^ e)) + c[6] - 1473231341,
    n = (n << 17 | n >>> 15) + r << 0,
    e += (t ^ n & (r ^ t)) + c[7] - 45705983,
    e = (e << 22 | e >>> 10) + n << 0,
    t += (r ^ e & (n ^ r)) + c[8] + 1770035416,
    t = (t << 7 | t >>> 25) + e << 0,
    r += (n ^ t & (e ^ n)) + c[9] - 1958414417,
    r = (r << 12 | r >>> 20) + t << 0,
    n += (e ^ r & (t ^ e)) + c[10] - 42063,
    n = (n << 17 | n >>> 15) + r << 0,
    e += (t ^ n & (r ^ t)) + c[11] - 1990404162,
    e = (e << 22 | e >>> 10) + n << 0,
    t += (r ^ e & (n ^ r)) + c[12] + 1804603682,
    t = (t << 7 | t >>> 25) + e << 0,
    r += (n ^ t & (e ^ n)) + c[13] - 40341101,
    r = (r << 12 | r >>> 20) + t << 0,
    n += (e ^ r & (t ^ e)) + c[14] - 1502002290,
    n = (n << 17 | n >>> 15) + r << 0,
    e += (t ^ n & (r ^ t)) + c[15] + 1236535329,
    e = (e << 22 | e >>> 10) + n << 0,
    t += (n ^ r & (e ^ n)) + c[1] - 165796510,
    t = (t << 5 | t >>> 27) + e << 0,
    r += (e ^ n & (t ^ e)) + c[6] - 1069501632,
    r = (r << 9 | r >>> 23) + t << 0,
    n += (t ^ e & (r ^ t)) + c[11] + 643717713,
    n = (n << 14 | n >>> 18) + r << 0,
    e += (r ^ t & (n ^ r)) + c[0] - 373897302,
    e = (e << 20 | e >>> 12) + n << 0,
    t += (n ^ r & (e ^ n)) + c[5] - 701558691,
    t = (t << 5 | t >>> 27) + e << 0,
    r += (e ^ n & (t ^ e)) + c[10] + 38016083,
    r = (r << 9 | r >>> 23) + t << 0,
    n += (t ^ e & (r ^ t)) + c[15] - 660478335,
    n = (n << 14 | n >>> 18) + r << 0,
    e += (r ^ t & (n ^ r)) + c[4] - 405537848,
    e = (e << 20 | e >>> 12) + n << 0,
    t += (n ^ r & (e ^ n)) + c[9] + 568446438,
    t = (t << 5 | t >>> 27) + e << 0,
    r += (e ^ n & (t ^ e)) + c[14] - 1019803690,
    r = (r << 9 | r >>> 23) + t << 0,
    n += (t ^ e & (r ^ t)) + c[3] - 187363961,
    n = (n << 14 | n >>> 18) + r << 0,
    e += (r ^ t & (n ^ r)) + c[8] + 1163531501,
    e = (e << 20 | e >>> 12) + n << 0,
    t += (n ^ r & (e ^ n)) + c[13] - 1444681467,
    t = (t << 5 | t >>> 27) + e << 0,
    r += (e ^ n & (t ^ e)) + c[2] - 51403784,
    r = (r << 9 | r >>> 23) + t << 0,
    n += (t ^ e & (r ^ t)) + c[7] + 1735328473,
    n = (n << 14 | n >>> 18) + r << 0,
    e += (r ^ t & (n ^ r)) + c[12] - 1926607734,
    e = (e << 20 | e >>> 12) + n << 0,
    i = e ^ n,
    t += (i ^ r) + c[5] - 378558,
    t = (t << 4 | t >>> 28) + e << 0,
    r += (i ^ t) + c[8] - 2022574463,
    r = (r << 11 | r >>> 21) + t << 0,
    o = r ^ t,
    n += (o ^ e) + c[11] + 1839030562,
    n = (n << 16 | n >>> 16) + r << 0,
    e += (o ^ n) + c[14] - 35309556,
    e = (e << 23 | e >>> 9) + n << 0,
    i = e ^ n,
    t += (i ^ r) + c[1] - 1530992060,
    t = (t << 4 | t >>> 28) + e << 0,
    r += (i ^ t) + c[4] + 1272893353,
    r = (r << 11 | r >>> 21) + t << 0,
    o = r ^ t,
    n += (o ^ e) + c[7] - 155497632,
    n = (n << 16 | n >>> 16) + r << 0,
    e += (o ^ n) + c[10] - 1094730640,
    e = (e << 23 | e >>> 9) + n << 0,
    i = e ^ n,
    t += (i ^ r) + c[13] + 681279174,
    t = (t << 4 | t >>> 28) + e << 0,
    r += (i ^ t) + c[0] - 358537222,
    r = (r << 11 | r >>> 21) + t << 0,
    o = r ^ t,
    n += (o ^ e) + c[3] - 722521979,
    n = (n << 16 | n >>> 16) + r << 0,
    e += (o ^ n) + c[6] + 76029189,
    e = (e << 23 | e >>> 9) + n << 0,
    i = e ^ n,
    t += (i ^ r) + c[9] - 640364487,
    t = (t << 4 | t >>> 28) + e << 0,
    r += (i ^ t) + c[12] - 421815835,
    r = (r << 11 | r >>> 21) + t << 0,
    o = r ^ t,
    n += (o ^ e) + c[15] + 530742520,
    n = (n << 16 | n >>> 16) + r << 0,
    e += (o ^ n) + c[2] - 995338651,
    e = (e << 23 | e >>> 9) + n << 0,
    t += (n ^ (e | ~r)) + c[0] - 198630844,
    t = (t << 6 | t >>> 26) + e << 0,
    r += (e ^ (t | ~n)) + c[7] + 1126891415,
    r = (r << 10 | r >>> 22) + t << 0,
    n += (t ^ (r | ~e)) + c[14] - 1416354905,
    n = (n << 15 | n >>> 17) + r << 0,
    e += (r ^ (n | ~t)) + c[5] - 57434055,
    e = (e << 21 | e >>> 11) + n << 0,
    t += (n ^ (e | ~r)) + c[12] + 1700485571,
    t = (t << 6 | t >>> 26) + e << 0,
    r += (e ^ (t | ~n)) + c[3] - 1894986606,
    r = (r << 10 | r >>> 22) + t << 0,
    n += (t ^ (r | ~e)) + c[10] - 1051523,
    n = (n << 15 | n >>> 17) + r << 0,
    e += (r ^ (n | ~t)) + c[1] - 2054922799,
    e = (e << 21 | e >>> 11) + n << 0,
    t += (n ^ (e | ~r)) + c[8] + 1873313359,
    t = (t << 6 | t >>> 26) + e << 0,
    r += (e ^ (t | ~n)) + c[15] - 30611744,
    r = (r << 10 | r >>> 22) + t << 0,
    n += (t ^ (r | ~e)) + c[6] - 1560198380,
    n = (n << 15 | n >>> 17) + r << 0,
    e += (r ^ (n | ~t)) + c[13] + 1309151649,
    e = (e << 21 | e >>> 11) + n << 0,
    t += (n ^ (e | ~r)) + c[4] - 145523070,
    t = (t << 6 | t >>> 26) + e << 0,
    r += (e ^ (t | ~n)) + c[11] - 1120210379,
    r = (r << 10 | r >>> 22) + t << 0,
    n += (t ^ (r | ~e)) + c[2] + 718787259,
    n = (n << 15 | n >>> 17) + r << 0,
    e += (r ^ (n | ~t)) + c[9] - 343485551,
    e = (e << 21 | e >>> 11) + n << 0,
    this.first ? (this.h0 = t + 1732584193 << 0,
    this.h1 = e - 271733879 << 0,
    this.h2 = n - 1732584194 << 0,
    this.h3 = r + 271733878 << 0,
    this.first = !1) : (this.h0 = this.h0 + t << 0,
    this.h1 = this.h1 + e << 0,
    this.h2 = this.h2 + n << 0,
    this.h3 = this.h3 + r << 0)
}
,
Md5.prototype.hex = function() {
    this.finalize();
    var t = this.h0
      , e = this.h1
      , n = this.h2
      , r = this.h3;
    return HEX_CHARS[t >> 4 & 15] + HEX_CHARS[15 & t] + HEX_CHARS[t >> 12 & 15] + HEX_CHARS[t >> 8 & 15] + HEX_CHARS[t >> 20 & 15] + HEX_CHARS[t >> 16 & 15] + HEX_CHARS[t >> 28 & 15] + HEX_CHARS[t >> 24 & 15] + HEX_CHARS[e >> 4 & 15] + HEX_CHARS[15 & e] + HEX_CHARS[e >> 12 & 15] + HEX_CHARS[e >> 8 & 15] + HEX_CHARS[e >> 20 & 15] + HEX_CHARS[e >> 16 & 15] + HEX_CHARS[e >> 28 & 15] + HEX_CHARS[e >> 24 & 15] + HEX_CHARS[n >> 4 & 15] + HEX_CHARS[15 & n] + HEX_CHARS[n >> 12 & 15] + HEX_CHARS[n >> 8 & 15] + HEX_CHARS[n >> 20 & 15] + HEX_CHARS[n >> 16 & 15] + HEX_CHARS[n >> 28 & 15] + HEX_CHARS[n >> 24 & 15] + HEX_CHARS[r >> 4 & 15] + HEX_CHARS[15 & r] + HEX_CHARS[r >> 12 & 15] + HEX_CHARS[r >> 8 & 15] + HEX_CHARS[r >> 20 & 15] + HEX_CHARS[r >> 16 & 15] + HEX_CHARS[r >> 28 & 15] + HEX_CHARS[r >> 24 & 15]
}
,
Md5.prototype.toString = Md5.prototype.hex,
Md5.prototype.digest = function() {
    this.finalize();
    var t = this.h0
      , e = this.h1
      , n = this.h2
      , r = this.h3;
    return [255 & t, t >> 8 & 255, t >> 16 & 255, t >> 24 & 255, 255 & e, e >> 8 & 255, e >> 16 & 255, e >> 24 & 255, 255 & n, n >> 8 & 255, n >> 16 & 255, n >> 24 & 255, 255 & r, r >> 8 & 255, r >> 16 & 255, r >> 24 & 255]
}
,
Md5.prototype.array = Md5.prototype.digest,
Md5.prototype.arrayBuffer = function() {
    this.finalize();
    var t = new ArrayBuffer(16)
      , e = new Uint32Array(t);
    return e[0] = this.h0,
    e[1] = this.h1,
    e[2] = this.h2,
    e[3] = this.h3,
    t
}
,
Md5.prototype.buffer = Md5.prototype.arrayBuffer,
Md5.prototype.base64 = function() {
    for (var t, e, n, r = "", i = this.array(), o = 0; o < 15; )
        t = i[o++],
        e = i[o++],
        n = i[o++],
        r += BASE64_ENCODE_CHAR[t >>> 2] + BASE64_ENCODE_CHAR[63 & (t << 4 | e >>> 4)] + BASE64_ENCODE_CHAR[63 & (e << 2 | n >>> 6)] + BASE64_ENCODE_CHAR[63 & n];
    return t = i[o],
    r += BASE64_ENCODE_CHAR[t >>> 2] + BASE64_ENCODE_CHAR[t << 4 & 63] + "==",
    r
};
function aa(e) {
    return new Md5(!0).update(e)["hex"]()
}
function l(e, t) {
    return e.toString().toUpperCase() > t.toString().toUpperCase() ? 1 : e.toString().toUpperCase() == t.toString().toUpperCase() ? 0 : -1
}
function s(e) {
    for (var t = Object.keys(e).sort(l), n = "", a = 0; a < t.length; a++)
        if (void 0 !== e[t[a]])
            if (e[t[a]] && e[t[a]]instanceof Object || e[t[a]]instanceof Array) {
                var c = JSON.stringify(e[t[a]]);
                n += t[a] + c
            } else
                n += t[a] + e[t[a]];
    return n
}
function d(e) {
    for (var t in e)
        "" !== e[t] && void 0 !== e[t] || delete e[t];
    var n = '3637CB36B2E54A72A7002978D0506CDF' + s(e);
    return aa(n).toLocaleLowerCase()
}
var f = {
    getSign: d
};


var param = {"ts":1651819450407,"KIND":"YLYP","timeType":"6","BeginTime":"2021-11-06 00:00:00","EndTime":"2022-05-06 23:59:59","createTime":[],"pageNo":2,"pageSize":10,"total":14565}
console.log("md5加密结果：",f.getSign(param));
