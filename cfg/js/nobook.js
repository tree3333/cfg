/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
var body = $response.body                                        

body = body.replace(/"app_resource_vip":1/g,'"app_resource_vip":0')
body = body.replace(/"vip":0/g,'"vip":1')
body = body.replace(/"vip":1/g,'"vip":0')

$done({body});      
