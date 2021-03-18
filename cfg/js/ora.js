/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
                                                                  
var body = $response.body                                        

//解锁尊享服务测试
//body = body.replace(/2020/,'2050')
body = body.replace(/"tServiceEndDate":"\d+/g,'"tServiceEndDate":"2030')
body = body.replace(/tServiceStatus":"\d+/,'tServiceStatus":"2')

$done({body});      
