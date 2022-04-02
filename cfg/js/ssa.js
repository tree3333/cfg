/*
‼️规则完全免费，仅供学习交流，🈲️商业用途
*/
var body = $response.body;
var url = $request.url;
var obj = JSON.parse(body);

const vip = '/cms/Appapi/username/username';

if (url.indexOf(vip) != -1) {
    obj.point= 999999;
    obj.jomkenylv = 99;
    obj.groupname = "白金会员";
    obj.overduedate = 2027383523;
    obj.overduedate2 = 2027383523;
    body = JSON.stringify(obj);
}
$done({body});
