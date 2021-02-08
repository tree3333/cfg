/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
var body = $response.body                                        

body = body.replace(/"tradeEndTime":\d+/g,'"tradeEndTime":1696448880000')
body = body.replace(/"coinBook":\w+/g,'"coinBook":false')
body = body.replace(/"ebookStatus":\d/g,'"ebookStatus":0')

$done({body});      
