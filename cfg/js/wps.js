/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
var body = $response.body                                        

//WPS会员
body = body.replace(/"expire_time":\d+/g,'"expire_time":3392883050')
body = body.replace(/"memberid":\d+/g,'"memberid":20')
body = body.replace(/"total_cost":-\d+/g,'"total_cost":1')
body = body.replace(/"level":\d+/g,'"level":1')
body = body.replace(/"result":"\w+/g,'"result":"ok')

$done({body});      
