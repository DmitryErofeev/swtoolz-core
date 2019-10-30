# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33',
                      '35', '37', '39', '41', '43', '45', '47', '49'],
                     ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34',
                      '36', '38', '40', '42', '44', '46', '48', '50']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть
# слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может
# начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
                 'SlotSize': '64',
                 'ShiftIndex': '0',
                 'ComboDefMedType': 'copper',
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
                'PortType',
                'BoardDescr',
                'cdLinkStatus',
                'cdPairStatus',
                'get_PortIndex',
            ],)

# ifType
MediumType = ({
                  '1': 'other',
                  '6': 'copper',
                  '24': 'loopback',
                  '53': 'virtual',
                  '117': 'copper',
                  '135': 'vlan',
                  '142': 'forward',
              },)

# swL2PortInfoLinkStatus
ActualStatus = ({
                    '1': 'other',
                    '2': 'linkup',
                    '3': 'linkdown',
                },)

# swL2PortInfoNwayStatus
ActualSpeed = ({
                   '1': 'linkdown',
                   '2': '10M-Full-8023x',
                   '3': '10M-Full',
                   '4': '10M-Half-backp',
                   '5': '10M-Half',
                   '6': '100M-Full-8023x',
                   '7': '100M-Full',
                   '8': '100M-Half-backp',
                   '9': '100M-Half',
                   '10': '1G-Full-8023x',
                   '11': '1G-Full',
                   '12': '1G-Half-backp',
                   '13': '1G-Half',
               },)

# swL2PortCtrlAdminState
AdminStatus = ({
                   '2': 'disabled',
                   '3': 'enabled',
               },)

# swL2PortCtrlNwayState
AdminSpeed = ({
                  '1': 'auto',
                  '2': '10M-Half',
                  '3': '10M-Full',
                  '4': '100M-Half',
                  '5': '100M-Full',
                  '7': '1G-Full',
              },)

# swL2PortCtrlFlowCtrlState
AdminFlow = ({
                 '1': 'other',
                 '2': 'disabled',
                 '3': 'enabled',
             },)

# ifType
PortType = ({
                '1': 'other',
                '6': 'fastEthernet',
                '117': 'gigaEthernet',
            },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'DES-3526',
              },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
                       '0': 'n/a',
                   },)

# swEtherCableDiagLinkStatus
cdLinkStatus = ({
                    '0': 'linkdown',
                    '1': 'linkup',
                    '2': 'other',
                },)

# swEtherCableDiagPairXStatus
cdPairStatus = ({
                    '0': 'ok',
                    '1': 'open',
                    '2': 'short',
                    '3': 'open-short',
                    '4': 'crosstalk',
                    '5': 'unknown',
                    '6': 'count',
                    '7': 'no-cable',
                    '8': 'other',
                },)

walk_PortIndex = {
    # PortIndex   .1.3.6.1.4.1.171.11.64.2.2.4.1.1.1		swL2PortInfoPortIndex
    'PortIndex': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1',
}

get_PortIndex = {
    # PortIndex      .1.3.6.1.4.1.171.11.64.2.2.4.1.1.1		swL2PortInfoPortIndex
    'PortIndex.1':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.1',
    'PortIndex.2':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.2',
    'PortIndex.3':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.3',
    'PortIndex.4':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.4',
    'PortIndex.5':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.5',
    'PortIndex.6':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.6',
    'PortIndex.7':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.7',
    'PortIndex.8':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.8',
    'PortIndex.9':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.9',
    'PortIndex.10': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.10',
    'PortIndex.11': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.11',
    'PortIndex.12': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.12',
    'PortIndex.13': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.13',
    'PortIndex.14': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.14',
    'PortIndex.15': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.15',
    'PortIndex.16': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.16',
    'PortIndex.17': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.17',
    'PortIndex.18': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.18',
    'PortIndex.19': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.19',
    'PortIndex.20': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.20',
    'PortIndex.21': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.21',
    'PortIndex.22': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.22',
    'PortIndex.23': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.23',
    'PortIndex.24': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.24',
    'PortIndex.25': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.25',
    'PortIndex.26': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.26',
    'PortIndex.27': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.27',
    'PortIndex.28': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.28',
    'PortIndex.29': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.29',
    'PortIndex.30': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.30',
    'PortIndex.31': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.31',
    'PortIndex.32': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.32',
    'PortIndex.33': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.33',
    'PortIndex.34': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.34',
    'PortIndex.35': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.35',
    'PortIndex.36': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.36',
    'PortIndex.37': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.37',
    'PortIndex.38': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.38',
    'PortIndex.39': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.39',
    'PortIndex.40': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.40',
    'PortIndex.41': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.41',
    'PortIndex.42': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.42',
    'PortIndex.43': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.43',
    'PortIndex.44': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.44',
    'PortIndex.45': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.45',
    'PortIndex.46': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.46',
    'PortIndex.47': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.47',
    'PortIndex.48': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.48',
    'PortIndex.49': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.49',
    'PortIndex.50': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.1.50',
}

get_ifAlias = {
    # PortDescr      .1.3.6.1.2.1.31.1.1.1.18			swL2PortCtrlDescription
    'PortDescr.1':  '.1.3.6.1.2.1.31.1.1.1.18.1',
    'PortDescr.2':  '.1.3.6.1.2.1.31.1.1.1.18.2',
    'PortDescr.3':  '.1.3.6.1.2.1.31.1.1.1.18.3',
    'PortDescr.4':  '.1.3.6.1.2.1.31.1.1.1.18.4',
    'PortDescr.5':  '.1.3.6.1.2.1.31.1.1.1.18.5',
    'PortDescr.6':  '.1.3.6.1.2.1.31.1.1.1.18.6',
    'PortDescr.7':  '.1.3.6.1.2.1.31.1.1.1.18.7',
    'PortDescr.8':  '.1.3.6.1.2.1.31.1.1.1.18.8',
    'PortDescr.9':  '.1.3.6.1.2.1.31.1.1.1.18.9',
    'PortDescr.10': '.1.3.6.1.2.1.31.1.1.1.18.10',
    'PortDescr.11': '.1.3.6.1.2.1.31.1.1.1.18.11',
    'PortDescr.12': '.1.3.6.1.2.1.31.1.1.1.18.12',
    'PortDescr.13': '.1.3.6.1.2.1.31.1.1.1.18.13',
    'PortDescr.14': '.1.3.6.1.2.1.31.1.1.1.18.14',
    'PortDescr.15': '.1.3.6.1.2.1.31.1.1.1.18.15',
    'PortDescr.16': '.1.3.6.1.2.1.31.1.1.1.18.16',
    'PortDescr.17': '.1.3.6.1.2.1.31.1.1.1.18.17',
    'PortDescr.18': '.1.3.6.1.2.1.31.1.1.1.18.18',
    'PortDescr.19': '.1.3.6.1.2.1.31.1.1.1.18.19',
    'PortDescr.20': '.1.3.6.1.2.1.31.1.1.1.18.20',
    'PortDescr.21': '.1.3.6.1.2.1.31.1.1.1.18.21',
    'PortDescr.22': '.1.3.6.1.2.1.31.1.1.1.18.22',
    'PortDescr.23': '.1.3.6.1.2.1.31.1.1.1.18.23',
    'PortDescr.24': '.1.3.6.1.2.1.31.1.1.1.18.24',
    'PortDescr.25': '.1.3.6.1.2.1.31.1.1.1.18.25',
    'PortDescr.26': '.1.3.6.1.2.1.31.1.1.1.18.26',
    'PortDescr.27': '.1.3.6.1.2.1.31.1.1.1.18.27',
    'PortDescr.28': '.1.3.6.1.2.1.31.1.1.1.18.28',
    'PortDescr.29': '.1.3.6.1.2.1.31.1.1.1.18.29',
    'PortDescr.30': '.1.3.6.1.2.1.31.1.1.1.18.30',
    'PortDescr.31': '.1.3.6.1.2.1.31.1.1.1.18.31',
    'PortDescr.32': '.1.3.6.1.2.1.31.1.1.1.18.32',
    'PortDescr.33': '.1.3.6.1.2.1.31.1.1.1.18.33',
    'PortDescr.34': '.1.3.6.1.2.1.31.1.1.1.18.34',
    'PortDescr.35': '.1.3.6.1.2.1.31.1.1.1.18.35',
    'PortDescr.36': '.1.3.6.1.2.1.31.1.1.1.18.36',
    'PortDescr.37': '.1.3.6.1.2.1.31.1.1.1.18.37',
    'PortDescr.38': '.1.3.6.1.2.1.31.1.1.1.18.38',
    'PortDescr.39': '.1.3.6.1.2.1.31.1.1.1.18.39',
    'PortDescr.40': '.1.3.6.1.2.1.31.1.1.1.18.40',
    'PortDescr.41': '.1.3.6.1.2.1.31.1.1.1.18.41',
    'PortDescr.42': '.1.3.6.1.2.1.31.1.1.1.18.42',
    'PortDescr.43': '.1.3.6.1.2.1.31.1.1.1.18.43',
    'PortDescr.44': '.1.3.6.1.2.1.31.1.1.1.18.44',
    'PortDescr.45': '.1.3.6.1.2.1.31.1.1.1.18.45',
    'PortDescr.46': '.1.3.6.1.2.1.31.1.1.1.18.46',
    'PortDescr.47': '.1.3.6.1.2.1.31.1.1.1.18.47',
    'PortDescr.48': '.1.3.6.1.2.1.31.1.1.1.18.48',
    'PortDescr.49': '.1.3.6.1.2.1.31.1.1.1.18.49',
    'PortDescr.50': '.1.3.6.1.2.1.31.1.1.1.18.50',
}

get_ifName = {
    # PortName      .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName.1':  '.1.3.6.1.2.1.31.1.1.1.1.1',
    'PortName.2':  '.1.3.6.1.2.1.31.1.1.1.1.2',
    'PortName.3':  '.1.3.6.1.2.1.31.1.1.1.1.3',
    'PortName.4':  '.1.3.6.1.2.1.31.1.1.1.1.4',
    'PortName.5':  '.1.3.6.1.2.1.31.1.1.1.1.5',
    'PortName.6':  '.1.3.6.1.2.1.31.1.1.1.1.6',
    'PortName.7':  '.1.3.6.1.2.1.31.1.1.1.1.7',
    'PortName.8':  '.1.3.6.1.2.1.31.1.1.1.1.8',
    'PortName.9':  '.1.3.6.1.2.1.31.1.1.1.1.9',
    'PortName.10': '.1.3.6.1.2.1.31.1.1.1.1.10',
    'PortName.11': '.1.3.6.1.2.1.31.1.1.1.1.11',
    'PortName.12': '.1.3.6.1.2.1.31.1.1.1.1.12',
    'PortName.13': '.1.3.6.1.2.1.31.1.1.1.1.13',
    'PortName.14': '.1.3.6.1.2.1.31.1.1.1.1.14',
    'PortName.15': '.1.3.6.1.2.1.31.1.1.1.1.15',
    'PortName.16': '.1.3.6.1.2.1.31.1.1.1.1.16',
    'PortName.17': '.1.3.6.1.2.1.31.1.1.1.1.17',
    'PortName.18': '.1.3.6.1.2.1.31.1.1.1.1.18',
    'PortName.19': '.1.3.6.1.2.1.31.1.1.1.1.19',
    'PortName.20': '.1.3.6.1.2.1.31.1.1.1.1.20',
    'PortName.21': '.1.3.6.1.2.1.31.1.1.1.1.21',
    'PortName.22': '.1.3.6.1.2.1.31.1.1.1.1.22',
    'PortName.23': '.1.3.6.1.2.1.31.1.1.1.1.23',
    'PortName.24': '.1.3.6.1.2.1.31.1.1.1.1.24',
    'PortName.25': '.1.3.6.1.2.1.31.1.1.1.1.25',
    'PortName.26': '.1.3.6.1.2.1.31.1.1.1.1.26',
    'PortName.27': '.1.3.6.1.2.1.31.1.1.1.1.27',
    'PortName.28': '.1.3.6.1.2.1.31.1.1.1.1.28',
    'PortName.29': '.1.3.6.1.2.1.31.1.1.1.1.29',
    'PortName.30': '.1.3.6.1.2.1.31.1.1.1.1.30',
    'PortName.31': '.1.3.6.1.2.1.31.1.1.1.1.31',
    'PortName.32': '.1.3.6.1.2.1.31.1.1.1.1.32',
    'PortName.33': '.1.3.6.1.2.1.31.1.1.1.1.33',
    'PortName.34': '.1.3.6.1.2.1.31.1.1.1.1.34',
    'PortName.35': '.1.3.6.1.2.1.31.1.1.1.1.35',
    'PortName.36': '.1.3.6.1.2.1.31.1.1.1.1.36',
    'PortName.37': '.1.3.6.1.2.1.31.1.1.1.1.37',
    'PortName.38': '.1.3.6.1.2.1.31.1.1.1.1.38',
    'PortName.39': '.1.3.6.1.2.1.31.1.1.1.1.39',
    'PortName.40': '.1.3.6.1.2.1.31.1.1.1.1.40',
    'PortName.41': '.1.3.6.1.2.1.31.1.1.1.1.41',
    'PortName.42': '.1.3.6.1.2.1.31.1.1.1.1.42',
    'PortName.43': '.1.3.6.1.2.1.31.1.1.1.1.43',
    'PortName.44': '.1.3.6.1.2.1.31.1.1.1.1.44',
    'PortName.45': '.1.3.6.1.2.1.31.1.1.1.1.45',
    'PortName.46': '.1.3.6.1.2.1.31.1.1.1.1.46',
    'PortName.47': '.1.3.6.1.2.1.31.1.1.1.1.47',
    'PortName.48': '.1.3.6.1.2.1.31.1.1.1.1.48',
    'PortName.49': '.1.3.6.1.2.1.31.1.1.1.1.49',
    'PortName.50': '.1.3.6.1.2.1.31.1.1.1.1.50',
}

get_SinglePort = {
    # MediumType      .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType.':   '.1.3.6.1.2.1.2.2.1.3.%s',
    # ActualStatus    .1.3.6.1.4.1.171.11.64.2.2.4.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus.': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.4.%s',
    # ActualSpeed     .1.3.6.1.4.1.171.11.64.2.2.4.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed.':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.5.%s',
    # AdminStatus     .1.3.6.1.4.1.171.11.64.2.2.4.2.1.3		swL2PortCtrlAdminState
    'AdminStatus.':  '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.3.%s',
    # AdminSpeed      .1.3.6.1.4.1.171.11.64.2.2.4.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed.':   '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.4.%s',
    # AdminFlow       .1.3.6.1.4.1.171.11.64.2.2.4.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow.':    '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.5.%s',
    # PortDescr       .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.':    '.1.3.6.1.2.1.31.1.1.1.18.%s',
    # PortType        .1.3.6.1.2.1.2.2.1.3				ifType
    'PortType.':     '.1.3.6.1.2.1.2.2.1.3.%s',
    # PortName        .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName.':     '.1.3.6.1.2.1.31.1.1.1.1.%s',
}

walk_AllPorts = {
    # MediumType     .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType':   '.1.3.6.1.2.1.2.2.1.3',
    # ActualStatus   .1.3.6.1.4.1.171.11.64.2.2.4.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus': '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.4',
    # ActualSpeed    .1.3.6.1.4.1.171.11.64.2.2.4.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed':  '.1.3.6.1.4.1.171.11.64.2.2.4.1.1.5',
    # AdminStatus    .1.3.6.1.4.1.171.11.64.2.2.4.2.1.3		swL2PortCtrlAdminState
    'AdminStatus':  '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.3',
    # AdminSpeed     .1.3.6.1.4.1.171.11.64.2.2.4.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed':   '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.4',
    # AdminFlow      .1.3.6.1.4.1.171.11.64.2.2.4.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow':    '.1.3.6.1.4.1.171.11.64.2.2.4.2.1.5',
}

walk_FDB_VLAN = {
    # FDB   .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    # VlanName                 .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName':               '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    # EgressPorts              .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanEgressPorts = {
    # VEP              .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanUntaggedPorts = {
    # VUP              .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'hex_string:VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

# Ключи массива специально изменены для соответствия стандартам TIA!
# При таком изменении распиновка по парам у новых и старых моделей D-Link выглядит одинаково.
get_CableDiag = {
    # cdLinkStatus     .1.3.6.1.4.1.171.12.58.1.1.1.3			swEtherCableDiagLinkStatus
    'cdLinkStatus.':  '.1.3.6.1.4.1.171.12.58.1.1.1.3.%s',
    # cdPair1Status    .1.3.6.1.4.1.171.12.58.1.1.1.4			swEtherCableDiagPair1Status
    'cdPair2Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.4.%s',
    # cdPair2Status    .1.3.6.1.4.1.171.12.58.1.1.1.5			swEtherCableDiagPair2Status
    'cdPair3Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.5.%s',
    # cdPair3Status    .1.3.6.1.4.1.171.12.58.1.1.1.6			swEtherCableDiagPair3Status
    'cdPair1Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.6.%s',
    # cdPair4Status    .1.3.6.1.4.1.171.12.58.1.1.1.7			swEtherCableDiagPair4Status
    'cdPair4Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.7.%s',
    # cdPair1Length    .1.3.6.1.4.1.171.12.58.1.1.1.8			swEtherCableDiagPair1Length
    'cdPair2Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.8.%s',
    # cdPair2Length    .1.3.6.1.4.1.171.12.58.1.1.1.9			swEtherCableDiagPair2Length
    'cdPair3Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.9.%s',
    # cdPair3Length    .1.3.6.1.4.1.171.12.58.1.1.1.10		swEtherCableDiagPair3Length
    'cdPair1Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.10.%s',
    # cdPair4Length    .1.3.6.1.4.1.171.12.58.1.1.1.11		swEtherCableDiagPair4Length
    'cdPair4Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.11.%s',
}

get_Errors = {
    # CRC                   .1.3.6.1.2.1.16.1.1.1.8			etherStatsCRCAlignErrors
    'CRC.':                '.1.3.6.1.2.1.16.1.1.1.8.%s',
    # Undersize             .1.3.6.1.2.1.16.1.1.1.9			etherStatsUndersizePkts
    'Undersize.':          '.1.3.6.1.2.1.16.1.1.1.9.%s',
    # Oversize              .1.3.6.1.2.1.16.1.1.1.10			etherStatsOversizePkts
    'Oversize.':           '.1.3.6.1.2.1.16.1.1.1.10.%s',
    # Fragment              .1.3.6.1.2.1.16.1.1.1.11			etherStatsFragments
    'Fragment.':           '.1.3.6.1.2.1.16.1.1.1.11.%s',
    # Jabber                .1.3.6.1.2.1.16.1.1.1.12			etherStatsJabbers
    'Jabber.':             '.1.3.6.1.2.1.16.1.1.1.12.%s',
    # ExcessiveDefferal     .1.3.6.1.2.1.10.7.2.1.7			dot3StatsDeferredTransmissions
    'ExcessiveDefferal.':  '.1.3.6.1.2.1.10.7.2.1.7.%s',
    # LateCollision         .1.3.6.1.2.1.10.7.2.1.8			dot3StatsLateCollisions
    'LateCollision.':      '.1.3.6.1.2.1.10.7.2.1.8.%s',
    # ExcessiveCollision    .1.3.6.1.2.1.10.7.2.1.9			dot3StatsExcessiveCollisions
    'ExcessiveCollision.': '.1.3.6.1.2.1.10.7.2.1.9.%s',
    # SingleCollision       .1.3.6.1.2.1.10.7.2.1.4			dot3StatsSingleCollisionFrames
    'SingleCollision.':    '.1.3.6.1.2.1.10.7.2.1.4.%s',
    # Collision             .1.3.6.1.2.1.16.1.1.1.13			etherStatsCollisions
    'Collision.':          '.1.3.6.1.2.1.16.1.1.1.13.%s',
}

get_InOutOctets = {
    # InOctets     .1.3.6.1.2.1.31.1.1.1.6			ifHCInOctets
    'InOctets.':  '.1.3.6.1.2.1.31.1.1.1.6.%s',
    # OutOctets    .1.3.6.1.2.1.31.1.1.1.10			ifHCOutOctets
    'Outoctets.': '.1.3.6.1.2.1.31.1.1.1.10.%s',
}

set_AdminStatus = [
    # .1.3.6.1.4.1.171.11.63.3.2.2.2.1.2				swL2PortCtrlAdminState
    ['.1.3.6.1.4.1.171.11.63.3.2.2.2.1.2.%s', '', '%s', 'INTEGER'],
]

set_AdminSpeed = [
    # .1.3.6.1.4.1.171.11.63.3.2.2.2.1.3				swL2PortCtrlNwayState
    ['.1.3.6.1.4.1.171.11.63.3.2.2.2.1.3.%s', '', '%s', 'INTEGER'],
]

set_CableDiagInit = [
    # .1.3.6.1.4.1.171.12.58.1.1.1.12					swEtherCableDiagAction
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '%s', '1', 'INTEGER'],
]

set_SaveConfig = [
    # .1.3.6.1.4.1.171.12.1.2.6						agentSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.6', '0', '2', 'INTEGER'],
]

set_CreateVlan = [
    # .1.3.6.1.2.1.17.7.1.4.3.1.1					dot1qVlanStaticName
    ['.1.3.6.1.2.1.17.7.1.4.3.1.1', '{1}', '{2}', 'OCTETSTR'],
    # .1.3.6.1.2.1.17.7.1.4.3.1.2					dot1qVlanStaticEgressPorts
    ['.1.3.6.1.2.1.17.7.1.4.3.1.2', '{1}', '{3}', 'OCTETSTR'],
    # .1.3.6.1.2.1.17.7.1.4.3.1.5					dot1qVlanStaticRowStatus
    ['.1.3.6.1.2.1.17.7.1.4.3.1.5', '{1}', '4', 'INTEGER'],
]

set_IpifCfg = [
    # .1.3.6.1.4.1.171.11.63.3.2.1.2.2					swL2DevCtrlSystemIP
    ['.1.3.6.1.4.1.171.11.63.3.2.1.2.2', '0', '{1}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.63.3.2.1.2.3					swL2DevCtrlSubnetMask
    ['.1.3.6.1.4.1.171.11.63.3.2.1.2.3', '0', '{2}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.63.3.2.1.2.4					swL2DevCtrlDefaultGateway
    ['.1.3.6.1.4.1.171.11.63.3.2.1.2.4', '0', '{3}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.63.3.2.1.2.5					swL2DevCtrlManagementVlanId
    ['.1.3.6.1.4.1.171.11.63.3.2.1.2.5', '0', '{4}', 'INTEGER'],
]
