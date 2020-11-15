/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
var body = $response.body                                        

//method 1
//let obj = JSON.parse(body);
//obj = {
//    "isVip": true,
//    "code": 200,
//    "expireDays": 199999999
//};
//$done({body:JSON.stringify(obj)});

//method 2
body = body.replace(/"isVip":\w+/g,'"isVip":true')
body = body.replace(/"expireDays":\-1/g,'"expireDays":1999999999')
$done({body});      
