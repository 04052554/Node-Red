[
    {
        "id": "567a8eee.69288",
        "type": "tab",
        "label": "Flow 3"
    },
    {
        "id": "bb0cf486.504058",
        "type": "inject",
        "z": "567a8eee.69288",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 150,
        "y": 121,
        "wires": [
            [
                "41e0ed0c.61de24",
                "7e349430.687a6c"
            ]
        ]
    },
    {
        "id": "41e0ed0c.61de24",
        "type": "function",
        "z": "567a8eee.69288",
        "name": "payload",
        "func": "msg.headers=\n{\n    deviceKey: \"escuO2o0lthaDdJ0\"\n};\nmsg.payload= \"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 80,
        "wires": [
            [
                "56d00ada.7c36b4"
            ]
        ]
    },
    {
        "id": "7e349430.687a6c",
        "type": "function",
        "z": "567a8eee.69288",
        "name": "payload",
        "func": "msg.headers=\n{\n    deviceKey: \"escuO2o0lthaDdJ0\"\n};\n    msg.payload= \"Humidity,,35\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 160,
        "wires": [
            [
                "90aa6b63.26c248"
            ]
        ]
    },
    {
        "id": "56d00ada.7c36b4",
        "type": "http request",
        "z": "567a8eee.69288",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DVpHlUin/datapoints.csv",
        "tls": "",
        "x": 530,
        "y": 80,
        "wires": [
            [
                "aab129e2.5f7988",
                "69f67fac.39f1c"
            ]
        ]
    },
    {
        "id": "aab129e2.5f7988",
        "type": "http response",
        "z": "567a8eee.69288",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 80,
        "wires": []
    },
    {
        "id": "69f67fac.39f1c",
        "type": "debug",
        "z": "567a8eee.69288",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 750,
        "y": 160,
        "wires": []
    },
    {
        "id": "90aa6b63.26c248",
        "type": "http request",
        "z": "567a8eee.69288",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DVpHlUin/datapoints.csv",
        "tls": "",
        "x": 530,
        "y": 160,
        "wires": [
            [
                "aab129e2.5f7988",
                "69f67fac.39f1c"
            ]
        ]
    }
]
