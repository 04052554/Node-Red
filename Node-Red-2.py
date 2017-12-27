[
    {
        "id": "4f25441c.3c530c",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "2e57d1b.6f2602e",
        "type": "inject",
        "z": "4f25441c.3c530c",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 110,
        "y": 140,
        "wires": [
            [
                "5eb16d08.e28e04",
                "6e13a3f5.adb9dc"
            ]
        ]
    },
    {
        "id": "5eb16d08.e28e04",
        "type": "function",
        "z": "4f25441c.3c530c",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"escuO2o0lthaDdJ0\"\n    };\n    \nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 272,
        "y": 103,
        "wires": [
            [
                "65864053.faa7f"
            ]
        ]
    },
    {
        "id": "65864053.faa7f",
        "type": "http request",
        "z": "4f25441c.3c530c",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DVpHlUin/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 470,
        "y": 100,
        "wires": [
            [
                "2ef2ec8c.315de4",
                "6ccb9a24.19e004"
            ]
        ]
    },
    {
        "id": "2ef2ec8c.315de4",
        "type": "http response",
        "z": "4f25441c.3c530c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 670,
        "y": 100,
        "wires": []
    },
    {
        "id": "6e13a3f5.adb9dc",
        "type": "function",
        "z": "4f25441c.3c530c",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"escuO2o0lthaDdJ0\"\n    };\n    \nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 272,
        "y": 179,
        "wires": [
            [
                "6f341990.557fb8"
            ]
        ]
    },
    {
        "id": "6f341990.557fb8",
        "type": "http request",
        "z": "4f25441c.3c530c",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DVpHlUin/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 470,
        "y": 180,
        "wires": [
            [
                "2ef2ec8c.315de4",
                "6ccb9a24.19e004"
            ]
        ]
    },
    {
        "id": "6ccb9a24.19e004",
        "type": "debug",
        "z": "4f25441c.3c530c",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 690,
        "y": 180,
        "wires": []
    }
]
