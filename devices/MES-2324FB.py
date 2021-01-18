# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 5

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд
# содержит список портов.
DeviceMap = ([
                 [
                     ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12', '105',
                      '107'],
                     ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24',
                      '106', '108']
                 ],
                 [
                     ['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12', '2/25',
                      '2/27'],
                     ['2/13', '2/14', '2/15', '2/16', '2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23', '2/24',
                      '2/26', '216']
                 ],
                 [
                     ['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11', '3/12', '3/25',
                      '3/27'],
                     ['3/13', '3/14', '3/15', '3/16', '3/17', '3/18', '3/19', '3/20', '3/21', '3/22', '3/23', '3/24',
                      '3/26', '3/28']
                 ],
                 [
                     ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12', '4/25',
                      '4/27'],
                     ['4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23', '4/24',
                      '4/26', '4/28']
                 ],
                 [
                     ['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11', '5/12', '5/25',
                      '5/27'],
                     ['5/13', '5/14', '5/15', '5/16', '5/17', '5/18', '5/19', '5/20', '5/21', '5/22', '5/23', '5/24',
                      '5/26', '5/28']
                 ],
                 [
                     ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/25',
                      '6/27'],
                     ['6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24',
                      '6/26', '6/28']
                 ],
                 [
                     ['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11', '7/12', '7/25',
                      '7/27'],
                     ['7/13', '7/14', '7/15', '7/16', '7/17', '7/18', '7/19', '7/20', '7/21', '7/22', '7/23', '7/24',
                      '7/26', '7/28']
                 ],
                 [
                     ['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11', '8/12', '8/25',
                      '8/27'],
                     ['8/13', '8/14', '8/15', '8/16', '8/17', '8/18', '8/19', '8/20', '8/21', '8/22', '8/23', '8/24',
                      '8/26', '8/28']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть
# слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться,
# например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
                 'SlotSize': '108',
                 'ShiftIndex': '48',
                 #'MaxIndex': '216',
             },)

# Список рекомендуемых команд
Commands = ([
                'DeviceMap',
                'StackInfo',
                'MediumType',
                'ActualStatus',
                'ActualSpeed',
                'AdminStatus',
                'AdminSpeed',
                'AdminFlow',
                'BoardDescr',
                'get_PortIndex',
                'PortName',
                'walk_syslog',
                'get_deviceMac',
            ],)

# ifType
MediumType = ({
                  '1': 'other',
                  '6': 'copper',
                  '24': 'loopback',
                  '53': 'virtual',
                  '131': 'tunnel',
              },)

# ifOperStatus
ActualStatus = ({
                    '1': 'linkup',
                    '2': 'linkdown',
                    '3': 'testing',
                    '4': 'unknown',
                    '5': 'dormant',
                    '6': 'notPresent',
                    '7': 'lowerLayerDown',
                },)

# ifHighSpeed
ActualSpeed = ({
                   '0': 'linkdown',
                   '10': '10M',
                   '100': '100M',
                   '1000': '1G',
                   '10000': '10G',
               },)

# ifAdminStatus
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
               },)

# ifType (placeholder)
AdminSpeed = ({
                  '1': 'other',
                  '6': 'other',
                  '24': 'other',
                  '53': 'other',
              },)

# ifType (placeholder)
AdminFlow = ({
                 '1': 'disabled',
                 '6': 'disabled',
                 '24': 'disabled',
                 '53': 'disabled',
             },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'Eltex MES2324FB',
              },)

# ifName (placeholder)
PortName = ({
                '49': 'gi1/0/1',
                '50': 'gi1/0/2',
                '51': 'gi1/0/3',
                '52': 'gi1/0/4',
                '53': 'gi1/0/5',
                '54': 'gi1/0/6',
                '55': 'gi1/0/7',
                '56': 'gi1/0/8',
                '57': 'gi1/0/9',
                '58': 'gi1/0/10',
                '59': 'gi1/0/11',
                '60': 'gi1/0/12',
                '61': 'gi1/0/13',
                '62': 'gi1/0/14',
                '63': 'gi1/0/15',
                '64': 'gi1/0/16',
                '65': 'gi1/0/17',
                '66': 'gi1/0/18',
                '67': 'gi1/0/19',
                '68': 'gi1/0/20',
                '69': 'gi1/0/21',
                '70': 'gi1/0/22',
                '71': 'gi1/0/23',
                '72': 'gi1/0/24',
                '105': 'te1/0/1',
                '106': 'te1/0/2',
                '107': 'te1/0/3',
                '108': 'te1/0/4',
                '157': 'gi2/0/1',
                '158': 'gi2/0/2',
                '159': 'gi2/0/3',
                '160': 'gi2/0/4',
                '161': 'gi2/0/5',
                '162': 'gi2/0/6',
                '163': 'gi2/0/7',
                '164': 'gi2/0/8',
                '165': 'gi2/0/9',
                '166': 'gi2/0/10',
                '167': 'gi2/0/11',
                '168': 'gi2/0/12',
                '169': 'gi2/0/13',
                '170': 'gi2/0/14',
                '171': 'gi2/0/15',
                '172': 'gi2/0/16',
                '173': 'gi2/0/17',
                '174': 'gi2/0/18',
                '175': 'gi2/0/19',
                '176': 'gi2/0/20',
                '177': 'gi2/0/21',
                '178': 'gi2/0/22',
                '179': 'gi2/0/23',
                '180': 'gi2/0/24',
                '213': 'te2/0/1',
                '214': 'te2/0/2',
                '215': 'te2/0/3',
                '216': 'te2/0/4',
            },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
                       '0': 'n/a',
                   },)

walk_PortIndex = {
    #    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex': '.1.3.6.1.2.1.2.2.1.1',
}

get_deviceMac = {
    'hex_string:dot1dBaseBridgeAddress' : '1.3.6.1.2.1.17.1.1',

}

walk_syslog = {
    'rlSyslogGlobalEnable'          : '1.3.6.1.4.1.89.82.2.1',
    'hex_ip:SyslogCollectorAddress'       : '.1.3.6.1.4.1.89.82.1.2.4.1.4',
    'SyslogCollectorUdpPort'       : '.1.3.6.1.4.1.89.82.1.2.4.1.5',
    'SyslogCollectorSeverity'       : '.1.3.6.1.4.1.89.82.1.2.4.1.7',

    }

get_PortIndex = {
    #    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex.1': '.1.3.6.1.2.1.2.2.1.1.49',
    'PortIndex.2': '.1.3.6.1.2.1.2.2.1.1.50',
    'PortIndex.3': '.1.3.6.1.2.1.2.2.1.1.51',
    'PortIndex.4': '.1.3.6.1.2.1.2.2.1.1.52',
    'PortIndex.5': '.1.3.6.1.2.1.2.2.1.1.53',
    'PortIndex.6': '.1.3.6.1.2.1.2.2.1.1.54',
    'PortIndex.7': '.1.3.6.1.2.1.2.2.1.1.55',
    'PortIndex.8': '.1.3.6.1.2.1.2.2.1.1.56',
    'PortIndex.9': '.1.3.6.1.2.1.2.2.1.1.57',
    'PortIndex.10': '.1.3.6.1.2.1.2.2.1.1.58',
    'PortIndex.11': '.1.3.6.1.2.1.2.2.1.1.59',
    'PortIndex.12': '.1.3.6.1.2.1.2.2.1.1.60',
    'PortIndex.13': '.1.3.6.1.2.1.2.2.1.1.61',
    'PortIndex.14': '.1.3.6.1.2.1.2.2.1.1.62',
    'PortIndex.15': '.1.3.6.1.2.1.2.2.1.1.63',
    'PortIndex.16': '.1.3.6.1.2.1.2.2.1.1.64',
    'PortIndex.17': '.1.3.6.1.2.1.2.2.1.1.65',
    'PortIndex.18': '.1.3.6.1.2.1.2.2.1.1.66',
    'PortIndex.19': '.1.3.6.1.2.1.2.2.1.1.67',
    'PortIndex.20': '.1.3.6.1.2.1.2.2.1.1.68',
    'PortIndex.21': '.1.3.6.1.2.1.2.2.1.1.69',
    'PortIndex.22': '.1.3.6.1.2.1.2.2.1.1.70',
    'PortIndex.23': '.1.3.6.1.2.1.2.2.1.1.71',
    'PortIndex.24': '.1.3.6.1.2.1.2.2.1.1.72',
    'PortIndex.25': '.1.3.6.1.2.1.2.2.1.1.105',
    'PortIndex.26': '.1.3.6.1.2.1.2.2.1.1.106',
    'PortIndex.27': '.1.3.6.1.2.1.2.2.1.1.107',
    'PortIndex.28': '.1.3.6.1.2.1.2.2.1.1.108',
    'PortIndex.157': '.1.3.6.1.2.1.2.2.1.1.157',
    'PortIndex.158': '.1.3.6.1.2.1.2.2.1.1.158',
    'PortIndex.159': '.1.3.6.1.2.1.2.2.1.1.159',
    'PortIndex.160': '.1.3.6.1.2.1.2.2.1.1.160',
    'PortIndex.161': '.1.3.6.1.2.1.2.2.1.1.161',
    'PortIndex.162': '.1.3.6.1.2.1.2.2.1.1.162',
    'PortIndex.163': '.1.3.6.1.2.1.2.2.1.1.163',
    'PortIndex.164': '.1.3.6.1.2.1.2.2.1.1.164',
    'PortIndex.165': '.1.3.6.1.2.1.2.2.1.1.165',
    'PortIndex.166': '.1.3.6.1.2.1.2.2.1.1.166',
    'PortIndex.167': '.1.3.6.1.2.1.2.2.1.1.167',
    'PortIndex.168': '.1.3.6.1.2.1.2.2.1.1.168',
    'PortIndex.169': '.1.3.6.1.2.1.2.2.1.1.169',
    'PortIndex.170': '.1.3.6.1.2.1.2.2.1.1.170',
    'PortIndex.171': '.1.3.6.1.2.1.2.2.1.1.171',
    'PortIndex.172': '.1.3.6.1.2.1.2.2.1.1.172',
    'PortIndex.173': '.1.3.6.1.2.1.2.2.1.1.173',
    'PortIndex.174': '.1.3.6.1.2.1.2.2.1.1.174',
    'PortIndex.175': '.1.3.6.1.2.1.2.2.1.1.175',
    'PortIndex.176': '.1.3.6.1.2.1.2.2.1.1.176',
    'PortIndex.177': '.1.3.6.1.2.1.2.2.1.1.177',
    'PortIndex.178': '.1.3.6.1.2.1.2.2.1.1.178',
    'PortIndex.179': '.1.3.6.1.2.1.2.2.1.1.179',
    'PortIndex.180': '.1.3.6.1.2.1.2.2.1.1.180',
    'PortIndex.213': '.1.3.6.1.2.1.2.2.1.1.213',
    'PortIndex.214': '.1.3.6.1.2.1.2.2.1.1.214',
    'PortIndex.215': '.1.3.6.1.2.1.2.2.1.1.215',
    'PortIndex.216': '.1.3.6.1.2.1.2.2.1.1.216',
}

get_SinglePort = {
    #    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType.': '.1.3.6.1.2.1.2.2.1.3.%s',
    #    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.': '.1.3.6.1.2.1.2.2.1.8.%s',
    #    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.': '.1.3.6.1.2.1.31.1.1.1.15.%s',
    #    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.': '.1.3.6.1.2.1.2.2.1.7.%s',
    #    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
    #    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminFlow.'      : '.1.3.6.1.2.1.2.2.1.3.%s',
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.': '.1.3.6.1.2.1.31.1.1.1.18.%s',
}

walk_AllPorts = {
    #    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType': '.1.3.6.1.2.1.2.2.1.3',
    #    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus': '.1.3.6.1.2.1.2.2.1.8',
    #    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed': '.1.3.6.1.2.1.31.1.1.1.15',
    #    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus': '.1.3.6.1.2.1.2.2.1.7',
    #    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
    #    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminFlow'       : '.1.3.6.1.2.1.2.2.1.3',
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifAlias = {
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifName = {
    #    PortName            .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
}

walk_FDB_VLAN = {
    #    FDB                 .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    #    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName': '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    #    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanEgressPorts = {
    #    VEP                 .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanUntaggedPorts = {
    #    VUP                 .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'hex_string:VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

set_AdminStatus = [
    #     .1.3.6.1.2.1.2.2.1.7						ifAdminStatus
    ['.1.3.6.1.2.1.2.2.1.7.%s', '', '%s', 'INTEGER'],
]
