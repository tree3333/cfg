/*
 * Quantumult X 脚本:
 * */

let obj = JSON.parse($response.body);
obj = {
    "msg" : "ok",
    "data" : {
      "member_trial_status" : 0,
      "enabled_device_count" : 10,
      "pending_member_info_list" : [

      ],
      "nickname" : "31870495@qq.com",
      "member_status" : 0,
      "member_additional_desc" : "",
      "member_expired_at" : 0,
      "current_device" : {
        "alias" : "li的Mac mini",
        "device_id" : "aeawq6ezqqaafflz",
        "trial_status" : 1,
        "last_binded_at" : 1752734137,
        "platform" : 104,
        "required_member_types" : [
          1
        ],
        "member_privilege_enable" : 0,
        "trial_end_at" : 1783338946
      },
      "user_id" : "aecwq6ezxeabiqf6",
      "current_device_status" : 1,
      "member_type" : 0
    },
    "code" : 0
}
$done({body: JSON.stringify(obj)});

