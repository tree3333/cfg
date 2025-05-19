/*
 * Quantumult X 脚本:
 * */

let obj = JSON.parse($response.body);

if (obj.响应==="0"){
    obj = {
        "响应": "1",
        "message": "验证通过，工作室登录，到期时间：9999-12-31",
        "游戏": "暗黑破坏神：不朽",
        "窗口": "666",
        "到期时间": "9999-12-31",
        "增值服务": "1"
    }
} 
$done({body: JSON.stringify(obj)});

