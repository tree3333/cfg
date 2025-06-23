/*
 * Quantumult X 脚本:
 * */

let obj = JSON.parse($response.body);

obj = {
  "errcode" : 0,
  "errmsg" : "success",
  "data" : {
    "loginWay" : "DEVICE_MANAGE",
    "userLevel" : 4,
    "benefits" : [ {
      "memberLevel" : 1,
      "benefitCode" : "ts_line",
      "havePermission" : true,
      "permissionData" : "1",
      "priceId" : "1705787940135686145",
      "title" : "中转线路"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "max_quality",
      "havePermission" : true,
      "permissionData" : "3200",
      "priceId" : "1705787940135686145",
      "title" : "最高画质"
    }, {
      "memberLevel" : 3,
      "benefitCode" : "original_quality",
      "havePermission" : true,
      "permissionData" : "12800",
      "priceId" : "1705787940135686149",
      "title" : "直连原画"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "max_frames",
      "havePermission" : true,
      "permissionData" : "165",
      "priceId" : "1705787940135686145",
      "title" : "最高帧数"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "max_resolution",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "最大分辨率"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "remote_audio",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "高保真远程音频"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "mouse_rate",
      "havePermission" : true,
      "permissionData" : "500",
      "priceId" : "1705787940135686145",
      "title" : "鼠标回报率"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "hardware_acceleration",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "硬件加速"
    }, {
      "memberLevel" : 4,
      "benefitCode" : "YCbCr",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1783043478431830017",
      "title" : "YCbCr 4:4:4色彩空间"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "same_time_remote_channel",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "同时远控通道数（限免）"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "id_fast_remote_device",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "远程协助"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "channel_labels",
      "havePermission" : true,
      "permissionData" : "50",
      "priceId" : "1705787940135686145",
      "title" : "会话标签"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "pc_control",
      "havePermission" : true,
      "permissionData" : "{\"number\":15}",
      "priceId" : "1705787940135686145",
      "title" : "桌面控制端"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "mobile_control",
      "havePermission" : true,
      "permissionData" : "{\"number\":4}",
      "priceId" : "1705787940135686145",
      "title" : "移动控制端"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "device_number",
      "havePermission" : true,
      "permissionData" : "{\"number\":800}",
      "priceId" : "1705787940135686145",
      "title" : "Windows被控端"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "m_c_os",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "控制操作系统"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "p_c_os",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "被控操作系统"
    }, {
      "memberLevel" : 3,
      "benefitCode" : "desktop_game_mouse_modes",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686149",
      "title" : "桌面端多种鼠标模式Beta"
    }, {
      "memberLevel" : 3,
      "benefitCode" : "platform_game_controller_mapping",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686149",
      "title" : "全平台游戏控制器映射"
    }, {
      "memberLevel" : 3,
      "benefitCode" : "gamepad_support",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686149",
      "title" : "移动端虚拟手柄键盘Beta"
    }, {
      "memberLevel" : 2,
      "benefitCode" : "driverlevel_input",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "驱动级键鼠"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "safe_account_check",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "账号级远协验证"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "temp_password",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "临时密码"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "long_password",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "长效密码"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "disables_id_remote",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "禁止来自ID的远协请求"
    }, {
      "memberLevel" : 2,
      "benefitCode" : "end_session_lock_screen",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "远程会话结束锁屏"
    }, {
      "memberLevel" : 2,
      "benefitCode" : "privacy_sscreen",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "隐私屏Beta"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "save_remote_history",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "保存协助历史"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "clipboard_sync",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "剪切板同步"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "more_to_more_remote_control",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "多对多远控"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "power_management",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "电源管理"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "shortcut_key",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "快捷键"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "file_transfer_speed",
      "havePermission" : true,
      "permissionData" : "32",
      "priceId" : "1705787940135686145",
      "title" : "文件传输速度"
    }, {
      "memberLevel" : 2,
      "benefitCode" : "multiple_display_support",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "多显示器支持"
    }, {
      "memberLevel" : 2,
      "benefitCode" : "virtual_display",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "虚拟显示器Beta"
    }, {
      "memberLevel" : 4,
      "benefitCode" : "multi_window_background_audio",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1783043478431830017",
      "title" : "多窗口后台音频"
    }, {
      "memberLevel" : 4,
      "benefitCode" : "remote_cmd",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1783043478431830017",
      "title" : "远程CMD指令"
    }, {
      "memberLevel" : 1,
      "benefitCode" : "batch_add_device",
      "havePermission" : true,
      "permissionData" : "",
      "priceId" : "1705787940135686145",
      "title" : "批量添加设备Beta"
    } ]
  }
}
$done({body: JSON.stringify(obj)});

