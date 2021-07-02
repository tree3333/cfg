/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
//解锁樊登读书精品课程                                            
//hosts = https://gateway-api.dushu365.com
var body = $response.body                                        

//精品课程解锁                                                    
body = body.replace(/"isBuyed":\w+/g,'"isBuyed":true')
body = body.replace(/"isBought":\w+/g,'"isBought":true')
body = body.replace(/"hasBought":\w+/g,'"hasBought":true')
body = body.replace(/"buyed":\w+/g,'"buyed":true')
body = body.replace(/"hasBuy":\d/g,'"hasBuy":1')
body = body.replace(/"trial":\w+/g,'"trial":true')
body = body.replace(/"free":\w+/g,'"free":true')
body = body.replace(/"unlock":\w+/g,'"unlock":true')

$done({body});      
