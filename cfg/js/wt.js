/**                                                               
 *  * @fileoverview Example of HTTP rewrite.                      
 *   *                                                            
 *    * @supported Quantumult X (v1.0.5-build173)                 
 *     */                                                         
var obj = JSON.parse($response.body);
obj.data.user_id = "77666677";
obj.data.vip_expire_time = 2130534427;
obj.data.vip_show_expire_time = 2130534427;
obj.data.vip_current_type = 2;
obj.data.vip_trial_day = 671932800;
obj.data.is_apple_receipt_user= true;
obj.data.vip_current_is_trial = true;
$done({body: JSON.stringify(obj)});


//var body = $response.body                                        

//精品课程解锁                                                    
//body = body.replace(/"vip_show_expire_time":\d+/g,'"vip_show_expire_time":2130534427')
//body = body.replace(/"vip_expire_time":\d+/g,'"vip_expire_time":2130534427')
//body = body.replace(/"user_id":"\w+/g,'"user_id":"77666677')
//body = body.replace(/"is_apple_receipt_user":\w+/g,'"is_apple_receipt_user":true')
//body = body.replace(/"vip_current_type":\d+/g,'"vip_current_type":1')
//
//body = body.replace(/"vip_trial_start_time":\d+/g,'"vip_trial_start_time":1688250476')
//body = body.replace(/"vip_current_type":\d+/g,'"vip_current_type":2')
//body = body.replace(/"vip_current_is_trial":\w+/g,'"vip_current_is_trial":true')

$done({body});      
