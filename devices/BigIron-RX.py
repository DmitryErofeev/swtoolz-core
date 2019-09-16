# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1/1','1/2','1/3','1/4','1/5','1/6','1/7','1/8','1/9','1/10','1/11','1/12'],['1/13','1/14','1/15','1/16','1/17','1/18','1/19','1/20','1/21','1/22','1/23','1/24']
    ],
    [
	['2/1','2/2','2/3','2/4','2/5','2/6','2/7','2/8','2/9','2/10','2/11','2/12'],['2/13','2/14','2/15','2/16','2/17','2/18','2/19','2/20','2/21','2/22','2/23','2/24']
    ],
    [
	['3/1','3/2','3/3','3/4','3/5','3/6','3/7','3/8','3/9','3/10','3/11','3/12'],['3/13','3/14','3/15','3/16','3/17','3/18','3/19','3/20','3/21','3/22','3/23','3/24']
    ],
    [
	['4/1','4/2','4/3','4/4','4/5','4/6','4/7','4/8','4/9','4/10','4/11','4/12'],['4/13','4/14','4/15','4/16','4/17','4/18','4/19','4/20','4/21','4/22','4/23','4/24']
    ],
    [
	['5/1','5/2','5/3','5/4','5/5','5/6','5/7','5/8','5/9','5/10','5/11','5/12'],['5/13','5/14','5/15','5/16','5/17','5/18','5/19','5/20','5/21','5/22','5/23','5/24']
    ],
    [
	['6/1','6/2','6/3','6/4','6/5','6/6','6/7','6/8','6/9','6/10','6/11','6/12'],['6/13','6/14','6/15','6/16','6/17','6/18','6/19','6/20','6/21','6/22','6/23','6/24']
    ],
    [
	['7/1','7/2','7/3','7/4','7/5','7/6','7/7','7/8','7/9','7/10','7/11','7/12'],['7/13','7/14','7/15','7/16','7/17','7/18','7/19','7/20','7/21','7/22','7/23','7/24']
    ],
    [
	['8/1','8/2','8/3','8/4','8/5','8/6','8/7','8/8','8/9','8/10','8/11','8/12'],['8/13','8/14','8/15','8/16','8/17','8/18','8/19','8/20','8/21','8/22','8/23','8/24']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
    'SlotSize'   : '64',
    'ShiftIndex' : '0',
    'MaxIndex'   : '1024',
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
    'BoardDescrShort',
    'PortName',
    'walk_PortIndex',
    'walk_BoardDescr',
#    'walk_ifName',
    ],)

# snSwIfInfoConnectorType
MediumType = ({
    '1' : 'other',
    '2' : 'copper',
    '3' : 'fiber',
    },)

# snSwIfInfoLinkStatus
ActualStatus = ({
    '1' : 'linkup',
    '2' : 'linkdown',
    },)

# snSwIfInfoSpeed
ActualSpeed = ({
    '0'  : 'linkdown',
    '1'  : 'auto',
    '2'  : '10M',
    '3'  : '100M',
    '4'  : '1G',
    '5'  : '1G-master',
    '6'  : '155G',
    '7'  : '10G',
    },)

# snSwIfInfoAdminStatus
AdminStatus = ({
    '1' : 'enabled',
    '2' : 'disabled',
    },)

# snSwIfInfoSpeed (placeholder)
AdminSpeed = ({
    '0'  : 'linkdown',
    '1'  : 'auto',
    '2'  : '10M',
    '3'  : '100M',
    '4'  : '1G',
    '5'  : '1G-master',
    '6'  : '155G',
    '7'  : '10G',
    },)

# snSwIfInfoFlowControl
AdminFlow = ({
    '0' : 'disabled',
    '1' : 'enabled',
    },)

# Пользовательские сокращения названий плат (модулей)
BoardDescrShort = ({
    'RX-BI-4XG 4-port 10GbE Module' : 'RX-BI-4XG (4x10G)',
    'BigIron RX Management Module' : '',
    'RX-BI-24HF 24-port 1 GbE Hybrid Module' : 'RX-BI-24HF (24x1G)',
    '' : '',
    },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
    '0' : 'n/a',
    },)

# walk_VlanEgressPorts (placeholder for Slava's Hardcode. not working but necessary)
walk_VlanEgressPorts = ({
    '0' : '',
    },)

# ifName (placeholder)
PortName = ({
     '1' :  '1/1',  '65' :  '2/1',  '129' :  '3/1',  '193' :  '4/1',  '257' :  '5/1',  '321' :  '6/1',  '385' :  '7/1',  '449' :  '8/1',
     '2' :  '1/2',  '66' :  '2/2',  '130' :  '3/2',  '194' :  '4/2',  '258' :  '5/2',  '322' :  '6/2',  '386' :  '7/2',  '450' :  '8/2',
     '3' :  '1/3',  '67' :  '2/3',  '131' :  '3/3',  '195' :  '4/3',  '259' :  '5/3',  '323' :  '6/3',  '387' :  '7/3',  '451' :  '8/3',
     '4' :  '1/4',  '68' :  '2/4',  '132' :  '3/4',  '196' :  '4/4',  '260' :  '5/4',  '324' :  '6/4',  '388' :  '7/4',  '452' :  '8/4',
     '5' :  '1/5',  '69' :  '2/5',  '133' :  '3/5',  '197' :  '4/5',  '261' :  '5/5',  '325' :  '6/5',  '389' :  '7/5',  '453' :  '8/5',
     '6' :  '1/6',  '70' :  '2/6',  '134' :  '3/6',  '198' :  '4/6',  '262' :  '5/6',  '326' :  '6/6',  '390' :  '7/6',  '454' :  '8/6',
     '7' :  '1/7',  '71' :  '2/7',  '135' :  '3/7',  '199' :  '4/7',  '263' :  '5/7',  '327' :  '6/7',  '391' :  '7/7',  '455' :  '8/7',
     '8' :  '1/8',  '72' :  '2/8',  '136' :  '3/8',  '200' :  '4/8',  '264' :  '5/8',  '328' :  '6/8',  '392' :  '7/8',  '456' :  '8/8',
     '9' :  '1/9',  '73' :  '2/9',  '137' :  '3/9',  '201' :  '4/9',  '265' :  '5/9',  '329' :  '6/9',  '393' :  '7/9',  '457' :  '8/9',
    '10' : '1/10',  '74' : '2/10',  '138' : '3/10',  '202' : '4/10',  '266' : '5/10',  '330' : '6/10',  '394' : '7/10',  '458' : '8/10',
    '11' : '1/11',  '75' : '2/11',  '139' : '3/11',  '203' : '4/11',  '267' : '5/11',  '331' : '6/11',  '395' : '7/11',  '459' : '8/11',
    '12' : '1/12',  '76' : '2/12',  '140' : '3/12',  '204' : '4/12',  '268' : '5/12',  '332' : '6/12',  '396' : '7/12',  '460' : '8/12',
    '13' : '1/13',  '77' : '2/13',  '141' : '3/13',  '205' : '4/13',  '269' : '5/13',  '333' : '6/13',  '397' : '7/13',  '461' : '8/13',
    '14' : '1/14',  '78' : '2/14',  '142' : '3/14',  '206' : '4/14',  '270' : '5/14',  '334' : '6/14',  '398' : '7/14',  '462' : '8/14',
    '15' : '1/15',  '79' : '2/15',  '143' : '3/15',  '207' : '4/15',  '271' : '5/15',  '335' : '6/15',  '399' : '7/15',  '463' : '8/15',
    '16' : '1/16',  '80' : '2/16',  '144' : '3/16',  '208' : '4/16',  '272' : '5/16',  '336' : '6/16',  '400' : '7/16',  '464' : '8/16',
    '17' : '1/17',  '81' : '2/17',  '145' : '3/17',  '209' : '4/17',  '273' : '5/17',  '337' : '6/17',  '401' : '7/17',  '465' : '8/17',
    '18' : '1/18',  '82' : '2/18',  '146' : '3/18',  '210' : '4/18',  '274' : '5/18',  '338' : '6/18',  '402' : '7/18',  '466' : '8/18',
    '19' : '1/19',  '83' : '2/19',  '147' : '3/19',  '211' : '4/19',  '275' : '5/19',  '339' : '6/19',  '403' : '7/19',  '467' : '8/19',
    '20' : '1/20',  '84' : '2/20',  '148' : '3/20',  '212' : '4/20',  '276' : '5/20',  '340' : '6/20',  '404' : '7/20',  '468' : '8/20',
    '21' : '1/21',  '85' : '2/21',  '149' : '3/21',  '213' : '4/21',  '277' : '5/21',  '341' : '6/21',  '405' : '7/21',  '469' : '8/21',
    '22' : '1/22',  '86' : '2/22',  '150' : '3/22',  '214' : '4/22',  '278' : '5/22',  '342' : '6/22',  '406' : '7/22',  '470' : '8/22',
    '23' : '1/23',  '87' : '2/23',  '151' : '3/23',  '215' : '4/23',  '279' : '5/23',  '343' : '6/23',  '407' : '7/23',  '471' : '8/23',
    '24' : '1/24',  '88' : '2/24',  '152' : '3/24',  '216' : '4/24',  '280' : '5/24',  '344' : '6/24',  '408' : '7/24',  '472' : '8/24',
    },)

walk_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.1991.1.1.3.3.4.1.1		snIfIndexLookupIfIndex
    'PortIndex'       : '.1.3.6.1.4.1.1991.1.1.3.3.4.1.1',
    }

walk_BoardDescr = {
#    BoardBescr          .1.3.6.1.4.1.1991.1.1.2.2.1.1.2		snAgentBrdMainBrdDescription
    'BoardDescr'      : '.1.3.6.1.4.1.1991.1.1.2.2.1.1.2',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.4.1.1991.1.1.3.3.5.1.9		snSwIfInfoConnectorType
    'MediumType.'     : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.9.%s',
#    ActualStatus        .1.3.6.1.4.1.1991.1.1.3.3.5.1.11		snSwIfInfoLinkStatus
    'ActualStatus.'   : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.11.%s',
#    ActualSpeed         .1.3.6.1.4.1.1991.1.1.3.3.5.1.7		snSwIfInfoSpeed
    'ActualSpeed.'    : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.7.%s',
#    AdminStatus         .1.3.6.1.4.1.1991.1.1.3.3.5.1.10		snSwIfInfoAdminStatus
    'AdminStatus.'    : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.10.%s',
#    AdminSpeed          .1.3.6.1.4.1.1991.1.1.3.3.5.1.7		snSwIfInfoSpeed (placeholder)
    'AdminSpeed.'     : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.7.%s',
#    AdminFlow           .1.3.6.1.4.1.1991.1.1.3.3.5.1.20		snSwIfInfoFlowControl
    'AdminFlow.'      : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.20.%s',
#    PortDescr           .1.3.6.1.4.1.1991.1.1.3.3.5.1.17		snSwIfName
    'PortDescr.'      : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.17.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.1991.1.1.3.3.5.1.9		snSwIfInfoConnectorType
    'MediumType'      : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.9',
#    ActualStatus        .1.3.6.1.4.1.1991.1.1.3.3.5.1.11		snSwIfInfoLinkStatus
    'ActualStatus'    : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.11',
#    ActualSpeed         .1.3.6.1.4.1.1991.1.1.3.3.5.1.7		snSwIfInfoSpeed
    'ActualSpeed'     : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.7',
#    AdminStatus         .1.3.6.1.4.1.1991.1.1.3.3.5.1.10		snSwIfInfoAdminStatus
    'AdminStatus'     : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.10',
#    AdminSpeed          .1.3.6.1.4.1.1991.1.1.3.3.5.1.7		snSwIfInfoSpeed (placeholder)
    'AdminSpeed'      : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.7',
#    AdminFlow           .1.3.6.1.4.1.1991.1.1.3.3.5.1.20		snSwIfInfoFlowControl
    'AdminFlow'       : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.20',
#    PortDescr           .1.3.6.1.4.1.1991.1.1.3.3.5.1.17		snSwIfName
    'PortDescr'       : '.1.3.6.1.4.1.1991.1.1.3.3.5.1.17',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_ifName = {
#    PortName            .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName'        : '.1.3.6.1.2.1.31.1.1.1.1',
    }

walk_VlanMap = {
#    VLanId              .1.3.6.1.4.1.1991.1.1.3.2.1.1.2		snVLanByPortVLanId
    'VLanId'          : '.1.3.6.1.4.1.1991.1.1.3.2.1.1.2',
#    VLanName            .1.3.6.1.4.1.1991.1.1.3.2.1.1.25		snVLanByPortVLanName
    'VLanName'        : '.1.3.6.1.4.1.1991.1.1.3.2.1.1.25',
#    RouterIntf          .1.3.6.1.4.1.1991.1.1.3.2.1.1.26		snVLanByPortRouterIntf
    'RouterIntf'      : '.1.3.6.1.4.1.1991.1.1.3.2.1.1.26',
#    PortList            .1.3.6.1.4.1.1991.1.1.3.2.1.1.28		snVLanByPortPortList
    'PortList'        : '.1.3.6.1.4.1.1991.1.1.3.2.1.1.28',
#    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName'        : '.1.3.6.1.2.1.17.7.1.4.3.1.1',
#    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts'     : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_IPifMap = {
#    ipIfIndex           .1.3.6.1.2.1.4.20.1.2				ipAdEntIfIndex
    'ipIfIndex'       : '.1.3.6.1.2.1.4.20.1.2',
#    ipNetMask           .1.3.6.1.2.1.4.20.1.3				ipAdEntNetMask
    'ipNetMask'       : '.1.3.6.1.2.1.4.20.1.3',
    }
