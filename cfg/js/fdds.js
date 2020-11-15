/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
//解锁樊登读书精品课程                                            
//hosts = api.dushu.io,gate-api.dushu.io                          
var body = $response.body                                        

//精品课程解锁                                                    
body = body.replace(/"isBuyed":\w+/g,'"isBuyed":true')
body = body.replace(/"buyed":\w+/g,'"buyed":true')
body = body.replace(/"trial":\w+/g,'"trial":true')
body = body.replace(/"free":\w+/g,'"free":true')
body = body.replace(/"hasBuy":\d/g,'"hasBuy":1')

$done({body});      
