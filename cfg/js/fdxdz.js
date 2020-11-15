/**
 *  * @fileoverview Example of HTTP rewrite.
 *   *
 *    * @supported Quantumult X (v1.0.5-build173)
 *     */

// $request, $response, $notify(title, subtitle, message), console.log(message)
// // $request.scheme, $request.method, $request.url, $request.path, $request.headers
// // $response.statusCode, $response.headers, $response.body
// //
// // $prefs is for persistent store and the data of $prefs will be cleared when Quantumult X is deleted.
// // $prefs.setValueForKey(value, key), $prefs.removeValueForKey(key), $prefs.removeAllValues(). Returns true or false, value and key should be string.
// // $prefs.valueForKey(key) returns value.
// //
// // setTimeout(function() { console.log("abc"); }, 1000);
// //
// // You can optional change the response headers at the same time by using $done({body: modifiedBody, headers: modifiedHeaders}); only change the response headers is not allowed for script-response-body. The modifiedHeaders can be copied and modified from $response.headers, please do not change the content length, type and encoding field.
// // Response status can also be optional changed by using $done({body: modifiedBody, headers: modifiedHeaders, status: modifiedStatus}), the modifiedStatus should be like "HTTP/1.1 200 OK"
//
//解锁樊登小读者VIP
//hosts = uapi.xfanread.com
var body = $response.body
//var obj = JSON.parse(body)

body = body.replace(/"canPlay":\w+/g,'"canPlay":true')
body = body.replace(/"canDownload":\w+/g,'"canDownload":true')
body = body.replace(/"unlocks":\d+/g,'"unlocks":0')
body = body.replace(/"isPreview":\w+/g,'"isPreview":false')
body = body.replace(/"vip":\w+/g,'"vip":true')
body = body.replace(/"vipExpireDate":".*?"/g,'"vipExpireDate":"2021-09-17"')

$done({body});

//body = JSON.stringify(obj);
//console.log(body);
//$done({body:JSON.stringify(obj)});
