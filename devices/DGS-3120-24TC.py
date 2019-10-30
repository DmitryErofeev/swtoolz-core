# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1/1','1/3','1/5','1/7','1/9', '1/11','1/13','1/15','1/17','1/19','1/21','1/23'],
	['1/2','1/4','1/6','1/8','1/10','1/12','1/14','1/16','1/18','1/20','1/22','1/24']
    ],
    [
	['2/1','2/3','2/5','2/7','2/9', '2/11','2/13','2/15','2/17','2/19','2/21','2/23'],
	['2/2','2/4','2/6','2/8','2/10','2/12','2/14','2/16','2/18','2/20','2/22','2/24']
    ],
    [
	['3/1','3/3','3/5','3/7','3/9', '3/11','3/13','3/15','3/17','3/19','3/21','3/23'],
	['3/2','3/4','3/6','3/8','3/10','3/12','3/14','3/16','3/18','3/20','3/22','3/24']
    ],
    [
	['4/1','4/3','4/5','4/7','4/9', '4/11','4/13','4/15','4/17','4/19','4/21','4/23'],
	['4/2','4/4','4/6','4/8','4/10','4/12','4/14','4/16','4/18','4/20','4/22','4/24']
    ],
    [
	['5/1','5/3','5/5','5/7','5/9', '5/11','5/13','5/15','5/17','5/19','5/21','5/23'],
	['5/2','5/4','5/6','5/8','5/10','5/12','5/14','5/16','5/18','5/20','5/22','5/24']
    ],
    [
	['6/1','6/3','6/5','6/7','6/9', '6/11','6/13','6/15','6/17','6/19','6/21','6/23'],
	['6/2','6/4','6/6','6/8','6/10','6/12','6/14','6/16','6/18','6/20','6/22','6/24']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
    'SlotSize'        : '64',
    'ShiftIndex'      : '0',
#    'MaxIndex'        : '64',
    'ComboDefMedType' : 'fiber',
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
    'BoardDescrShort',
    'PortName',
    'walk_PortIndex',
    'walk_BoardDescr',
    'get_HardwareRev',
    'walk_ifAlias',
    ],)

# swL2PortInfoMediumType
MediumType = ({
    '1' : 'copper',
    '2' : 'fiber',
    },)

# swL2PortInfoLinkStatus
ActualStatus = ({
    '1' : 'other',
    '2' : 'linkup',
    '3' : 'linkdown',
    },)

# swL2PortInfoNwayStatus
ActualSpeed = ({
    '0'  : 'linkdown',
    '1'  : '10M-Full-8023x',
    '2'  : '10M-Full',
    '3'  : '10M-Half-backp',
    '4'  : '10M-Half',
    '5'  : '100M-Full-8023x',
    '6'  : '100M-Full',
    '7'  : '100M-Half-backp',
    '8'  : '100M-Half',
    '9'  : '1G-Full-8023x',
    '10' : '1G-Full',
    '11' : '1G-Half-backp',
    '12' : '1G-Half',
    '13' : '10G-Full-8023x',
    '14' : '10G-Full',
    '15' : '10G-Half-8023x',
    '16' : '10G-Half',
    '17' : 'empty',
    '18' : 'err-disabled',
    },)

# swL2PortCtrlAdminState
AdminStatus = ({
    '2' : 'disabled',
    '3' : 'enabled',
    },)

# swL2PortCtrlNwayState
AdminSpeed = ({
    '2' : 'auto',
    '3' : '10M-Half',
    '4' : '10M-Full',
    '5' : '100M-Half',
    '6' : '100M-Full',
    '7' : '1G-Half',
    '8' : '1G-Full',
    '9' : '1G-Full-master',
    '10': '1G-Full-slave',
    },)

# swL2PortCtrlFlowCtrlState
AdminFlow = ({
    '1' : 'other',
    '2' : 'disabled',
    '3' : 'enabled',
    },)

# ifType
PortType = ({
    '1'   : 'other',
    '6'   : 'fastEthernet',
    '117' : 'gigaEthernet',
    },)

BoardDescrShort = ({
    'NOT_EXIST' : '',
    },)

# ifName (placeholder)
PortName = ({
     '1' :  '1/1',  '65' :  '2/1',  '129' :  '3/1',  '193' :  '4/1',  '257' :  '5/1',  '321' :  '6/1',
     '2' :  '1/2',  '66' :  '2/2',  '130' :  '3/2',  '194' :  '4/2',  '258' :  '5/2',  '322' :  '6/2',
     '3' :  '1/3',  '67' :  '2/3',  '131' :  '3/3',  '195' :  '4/3',  '259' :  '5/3',  '323' :  '6/3',
     '4' :  '1/4',  '68' :  '2/4',  '132' :  '3/4',  '196' :  '4/4',  '260' :  '5/4',  '324' :  '6/4',
     '5' :  '1/5',  '69' :  '2/5',  '133' :  '3/5',  '197' :  '4/5',  '261' :  '5/5',  '325' :  '6/5',
     '6' :  '1/6',  '70' :  '2/6',  '134' :  '3/6',  '198' :  '4/6',  '262' :  '5/6',  '326' :  '6/6',
     '7' :  '1/7',  '71' :  '2/7',  '135' :  '3/7',  '199' :  '4/7',  '263' :  '5/7',  '327' :  '6/7',
     '8' :  '1/8',  '72' :  '2/8',  '136' :  '3/8',  '200' :  '4/8',  '264' :  '5/8',  '328' :  '6/8',
     '9' :  '1/9',  '73' :  '2/9',  '137' :  '3/9',  '201' :  '4/9',  '265' :  '5/9',  '329' :  '6/9',
    '10' : '1/10',  '74' : '2/10',  '138' : '3/10',  '202' : '4/10',  '266' : '5/10',  '330' : '6/10',
    '11' : '1/11',  '75' : '2/11',  '139' : '3/11',  '203' : '4/11',  '267' : '5/11',  '331' : '6/11',
    '12' : '1/12',  '76' : '2/12',  '140' : '3/12',  '204' : '4/12',  '268' : '5/12',  '332' : '6/12',
    '13' : '1/13',  '77' : '2/13',  '141' : '3/13',  '205' : '4/13',  '269' : '5/13',  '333' : '6/13',
    '14' : '1/14',  '78' : '2/14',  '142' : '3/14',  '206' : '4/14',  '270' : '5/14',  '334' : '6/14',
    '15' : '1/15',  '79' : '2/15',  '143' : '3/15',  '207' : '4/15',  '271' : '5/15',  '335' : '6/15',
    '16' : '1/16',  '80' : '2/16',  '144' : '3/16',  '208' : '4/16',  '272' : '5/16',  '336' : '6/16',
    '17' : '1/17',  '81' : '2/17',  '145' : '3/17',  '209' : '4/17',  '273' : '5/17',  '337' : '6/17',
    '18' : '1/18',  '82' : '2/18',  '146' : '3/18',  '210' : '4/18',  '274' : '5/18',  '338' : '6/18',
    '19' : '1/19',  '83' : '2/19',  '147' : '3/19',  '211' : '4/19',  '275' : '5/19',  '339' : '6/19',
    '20' : '1/20',  '84' : '2/20',  '148' : '3/20',  '212' : '4/20',  '276' : '5/20',  '340' : '6/20',
    '21' : '1/21',  '85' : '2/21',  '149' : '3/21',  '213' : '4/21',  '277' : '5/21',  '341' : '6/21',
    '22' : '1/22',  '86' : '2/22',  '150' : '3/22',  '214' : '4/22',  '278' : '5/22',  '342' : '6/22',
    '23' : '1/23',  '87' : '2/23',  '151' : '3/23',  '215' : '4/23',  '279' : '5/23',  '343' : '6/23',
    '24' : '1/24',  '88' : '2/24',  '152' : '3/24',  '216' : '4/24',  '280' : '5/24',  '344' : '6/24',
    '25' : '1/25',  '89' : '2/25',  '153' : '3/25',  '217' : '4/25',  '281' : '5/25',  '345' : '6/25',
    '26' : '1/26',  '90' : '2/26',  '154' : '3/26',  '218' : '4/26',  '282' : '5/26',  '346' : '6/26',
    },)

get_HardwareRev = {
#    HardwareRev         .1.3.6.1.2.1.16.19.3.0				probeHardwareRev
    'HardwareRev.'    : '.1.3.6.1.2.1.16.19.3.0',
    }

walk_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1		swL2PortInfoPortIndex
    'PortIndex'       : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1',
    }

walk_BoardDescr = {
#    BoardBescr          .1.3.6.1.4.1.171.12.11.1.9.4.1.9		swUnitMgmtModuleName
    'BoardDescr'      : '.1.3.6.1.4.1.171.12.11.1.9.4.1.9',
    }

get_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1		swL2PortInfoPortIndex
#    PortIndex           .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1		swL2PortInfoPortIndex
    'PortIndex..1c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.1.1',
    'PortIndex..1f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.1.2',
    'PortIndex..2c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.2.1',
    'PortIndex..2f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.2.2',
    'PortIndex..3c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.3.1',
    'PortIndex..3f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.3.2',
    'PortIndex..4c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.4.1',
    'PortIndex..4f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.4.2',
    'PortIndex..5c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.5.1',
    'PortIndex..5f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.5.2',
    'PortIndex..6c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.6.1',
    'PortIndex..6f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.6.2',
    'PortIndex..7c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.7.1',
    'PortIndex..7f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.7.2',
    'PortIndex..8c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.8.1',
    'PortIndex..8f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.8.2',
    'PortIndex..9'    : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.9.2',
    'PortIndex..10'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.10.2',
    'PortIndex..11'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.11.2',
    'PortIndex..12'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.12.2',
    'PortIndex..13'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.13.2',
    'PortIndex..14'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.14.2',
    'PortIndex..15'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.15.2',
    'PortIndex..16'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.16.2',
    'PortIndex..17'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.17.2',
    'PortIndex..18'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.18.2',
    'PortIndex..19'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.19.2',
    'PortIndex..20'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.20.2',
    'PortIndex..21'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.21.2',
    'PortIndex..22'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.22.2',
    'PortIndex..23'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.23.2',
    'PortIndex..24'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.24.2',
    'PortIndex..25'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.25.1',
    'PortIndex..26'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.1.26.1',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2		swL2PortInfoMediumType
    'MediumType..c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2.%s.1',
    'MediumType..f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2.%s.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5		swL2PortInfoLinkStatus
    'ActualStatus..c' : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5.%s.1',
    'ActualStatus..f' : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5.%s.2',
#    ActualSpeed         .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6		swL2PortInfoNwayStatus
    'ActualSpeed..c'  : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6.%s.1',
    'ActualSpeed..f'  : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6.%s.2',
#    AdminStatus         .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4		swL2PortCtrlAdminState
    'AdminStatus..c'  : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4.%s.1',
    'AdminStatus..f'  : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4.%s.2',
#    AdminSpeed          .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5		swL2PortCtrlNwayState
    'AdminSpeed..c'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5.%s.1',
    'AdminSpeed..f'   : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5.%s.2',
#    AdminFlow           .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6		swL2PortCtrlFlowCtrlState
    'AdminFlow..c'    : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6.%s.1',
    'AdminFlow..f'    : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6.%s.2',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
#    PortType            .1.3.6.1.2.1.2.2.1.3				ifType
    'PortType.'       : '.1.3.6.1.2.1.2.2.1.3.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2		swL2PortInfoMediumType
    'MediumType'      : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5		swL2PortInfoLinkStatus
    'ActualStatus'    : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5',
#    ActualSpeed         .1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6		swL2PortInfoNwayStatus
    'ActualSpeed'     : '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6',
#    AdminStatus         .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4		swL2PortCtrlAdminState
    'AdminStatus'     : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4',
#    AdminSpeed          .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5		swL2PortCtrlNwayState
    'AdminSpeed'      : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5',
#    AdminFlow           .1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6		swL2PortCtrlFlowCtrlState
    'AdminFlow'       : '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_FDB_VLAN = {
#    FDB                 .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB'             : '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
    }

walk_VlanMap = {
#    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName'        : '.1.3.6.1.2.1.17.7.1.4.3.1.1',
#    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts'     : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_VlanEgressPorts = {
#    VEP                 .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:VEP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_VlanUntaggedPorts = {
#    VUP                 .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'hex_string:VUP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.4',
    }

set_SaveConfig = [
#     .1.3.6.1.4.1.171.12.1.2.18.4					agentBscFileSystemSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.18.4', '0', '2', 'INTEGER'],
    ]
