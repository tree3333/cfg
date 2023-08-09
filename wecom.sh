#!/bin/sh
conf="./wecom.conf"
conf_json=`cat $conf`
get_json() {
    [ ! "$2" ] && return
    result=`echo $1 | sed "s/,/\n/g" | grep "$2" | sed "s/:/\n/g" | sed "1d" | sed 's/"//g'`
    echo $result
}

getAccessToken() {
    corpid=`get_json "$conf_json" "corpid"`
    corpsecret=`get_json "$conf_json" "corpsecret"`
    # Get AccessToken
    access_json=`curl -k -s -G -d "corpid=${corpid}" -d "corpsecret=${corpsecret}" https://qyapi.weixin.qq.com/cgi-bin/gettoken`
    errorCode=`get_json "$access_json" "errcode"`
    if [ $errorCode -eq 0 ]; then
        #echo "Get accessCode success"
        accessToken=`get_json "$access_json" "access_token"`
        echo $accessToken
    else
        errorMsg=`get_json "$access_json" "errmsg"`
        echo "Get accessCode failed, errorCode is "$errorCode", errorMsg: "$errorMsg
    fi
}

sendMsg() {
    # Get AgentId=
    AgentId=`get_json "$conf_json" "AgentId"`
    token=$1
    toUser=$2
    shift 3
    msg="$@"
    send_json=`curl -k -s -X POST -H "Content-Type: application/json" -d "{\"touser\": \"$toUser\", \"msgtype\": \"text\", \"agentid\": \"$AgentId\", \"text\": {\"content\": \"$msg\"}, \"safe\": 0}" https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$token`
    if [ $? -ne 0 ]; then
        echo "Send error"
    else
        errorCode=`get_json "$send_json" "errcode"`
        if [ $errorCode -eq 0 ]; then
            echo "Send success"
        else
            errorMsg=`get_json "$send_json" "errmsg"`
            echo "Send error, error message: $errorMsg [$errorCode]"
        fi
    fi
}

# Check curl
curl bing.com
if [ $? -ne 0 ]; then
	echo "You musy install curl first, in debian, run: apt install curl -y"
	exit
fi

# Check config file exists
if [ -f $conf ]; then
    if [ $# -lt 1 ]; then
        echo "You must input user and message you wanna to send, eg:"
        echo "./wecom.sh userid Hello"
    else
        accessToken=`getAccessToken`
        if [ $? -eq 0 ]; then
            sendMsg $accessToken $1 $*
        fi
    fi
else
    echo "Creating sample config file"
    echo '{
    "corpid": "wwabcddzxdkrsdv",
    "corpsecret": "vQT_03RDVA3uE6JDASDASDAiXUvccqV8mDgLdLI",
    "AgentId": "1000002",
    "dataRecord": 1' > $conf
    echo "}" >> $conf
fi
