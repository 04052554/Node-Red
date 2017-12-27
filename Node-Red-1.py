[
    {
        "id": "7999159e.e7b22c",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "3fcda031.fe3b9",
        "type": "rpi-gpio in",
        "z": "7999159e.e7b22c",
        "name": "button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 110,
        "y": 220,
        "wires": [
            [
                "9ca554ee.5fb628",
                "f78c54ae.3b3148"
            ]
        ]
    },
    {
        "id": "f5686004.c3349",
        "type": "rpi-gpio out",
        "z": "7999159e.e7b22c",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 650,
        "y": 280,
        "wires": []
    },
    {
        "id": "9ca554ee.5fb628",
        "type": "debug",
        "z": "7999159e.e7b22c",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 550,
        "y": 120,
        "wires": []
    },
    {
        "id": "f78c54ae.3b3148",
        "type": "switch",
        "z": "7999159e.e7b22c",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 290,
        "y": 280,
        "wires": [
            [
                "f6247a35.4b9078"
            ],
            [
                "c94e92b.e0d8e7"
            ]
        ]
    },
    {
        "id": "c94e92b.e0d8e7",
        "type": "change",
        "z": "7999159e.e7b22c",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 320,
        "wires": [
            [
                "f5686004.c3349"
            ]
        ]
    },
    {
        "id": "f6247a35.4b9078",
        "type": "change",
        "z": "7999159e.e7b22c",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 260,
        "wires": [
            [
                "f5686004.c3349"
            ]
        ]
    }
]
