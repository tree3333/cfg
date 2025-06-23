/*
 * Quantumult X 脚本:
 * */

let obj = JSON.parse($response.body);

obj = {
    "errcode": 0,   
    "errmsg": "success",   
    "data": {    
        "loginWay": "DEVICE_MANAGE",
        "account": "LLK15419182",
        "lastModifyAccount": "",
        "id": "1927247357921058818",
        "isd": "+86",
        "level": 4,
        "mobile": "18980622145",
        "email": "",
        "avatarUrl": "",
        "memberLevelName": "专业版",
        "memberLevelId": "1711730222647160838",
        "endTime": "2075-06-05"
    } 
}
$done({body: JSON.stringify(obj)});

