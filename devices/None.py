# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# ------- Этот модуль предназначен для режима 'FORCED' -------

Commands = ([
                'OfflineDeviceMaps',
            ],)

OfflineDeviceMaps = ({
                         '16': [[['0', '0', '0', '1', '2', '0', '0']], ],
                         '21': [[['0', '0', '0', '1', '0', '0', '0']], ],
                         '24': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                 ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                  '28']], ],
                         '205': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28']], ],
                         '206': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24']],
                                 [[' 51', '53', '55', '57', '59', '61', '63', '65', '67', '69', '71', '73'],
                                  ['52', '54', '56', '58', '60', '62', '64', '66', '68', '70', '72', '74']],
                                 [['101', '103', '105', '107', '109', '111', '113', '115', '117', '119', '121', '123'],
                                  ['102', '104', '106', '108', '110', '112', '114', '116', '118', '120', '122', '124']],
                                 [['151', '153', '155', '157', '159', '161', '163', '165', '167', '169', '171', '173'],
                                  ['152', '154', '156', '158', '160', '162', '164', '166', '168', '170', '172', '174']],
                                 [['201', '203', '205', '207', '209', '211', '213', '215', '217', '219', '221', '223'],
                                  ['202', '204', '206', '208', '210', '212', '214', '216', '218', '220', '222', '224']],
                                 [['251', '253', '255', '257', '259', '261', '263', '265', '267', '269', '271', '273'],
                                  ['252', '254', '256', '258', '260', '262', '264', '266', '268', '270', '272',
                                   '274']], ],
                         '208': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26',
                                   '27']], ],
                         '209': [[['1', '3', '5', '7', '9', '11', '13', '15'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '17', '18']], ],
                         '210': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '211': [[['0', '0', '0', '2', '0', '0', '0']], ],
                         '213': [[['0', '0', '0', '1', '0', '0', '0']], ],
                         '215': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24']], ],
                         '216': [[['1', '3', '5', '7', '9', '11', '13', '15'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '17', '18']], ],
                         '217': [[['1', '3', '5', '7', '9', '11', '13', '15'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '17', '18']], ],
                         '218': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '219': [[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '25', '27'],
                                  ['13', '14', '15', '17', '17', '18', '19', '20', '21', '22', '23', '24', '26',
                                   '28']], ],
                         '220': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26']], ],
                         '221': [[['1', '3', '5', '7', ], ['2', '4', '6', '8', '9', '10']], ],
                         '222': [[['1/1', '1/3', '1/5', '1/7', '1/9', '1/11', '1/13', '1/15', '1/17', '1/19', '1/21',
                                   '1/23', '1/25'],
                                  ['1/2', '1/4', '1/6', '1/8', '1/10', '1/12', '1/14', '1/16', '1/18', '1/20', '1/22',
                                   '1/24', '1/26']],
                                 [['2/1', '2/3', '2/5', '2/7', '2/9', '2/11', '2/13', '2/15', '2/17', '2/19', '2/21',
                                   '2/23', '2/25'],
                                  ['2/2', '2/4', '2/6', '2/8', '2/10', '2/12', '2/14', '2/16', '2/18', '2/20', '2/22',
                                   '2/24', '2/26']],
                                 [['3/1', '3/3', '3/5', '3/7', '3/9', '3/11', '3/13', '3/15', '3/17', '3/19', '3/21',
                                   '3/23', '3/25'],
                                  ['3/2', '3/4', '3/6', '3/8', '3/10', '3/12', '3/14', '3/16', '3/18', '3/20', '3/22',
                                   '3/24', '3/26']],
                                 [['4/1', '4/3', '4/5', '4/7', '4/9', '4/11', '4/13', '4/15', '4/17', '4/19', '4/21',
                                   '4/23', '4/25'],
                                  ['4/2', '4/4', '4/6', '4/8', '4/10', '4/12', '4/14', '4/16', '4/18', '4/20', '4/22',
                                   '4/24', '4/26']],
                                 [['5/1', '5/3', '5/5', '5/7', '5/9', '5/11', '5/13', '5/15', '5/17', '5/19', '5/21',
                                   '5/23', '5/25'],
                                  ['5/2', '5/4', '5/6', '5/8', '5/10', '5/12', '5/14', '5/16', '5/18', '5/20', '5/22',
                                   '5/24', '5/26']],
                                 [['6/1', '6/3', '6/5', '6/7', '6/9', '6/11', '6/13', '6/15', '6/17', '6/19', '6/21',
                                   '6/23', '6/25'],
                                  ['6/2', '6/4', '6/6', '6/8', '6/10', '6/12', '6/14', '6/16', '6/18', '6/20', '6/22',
                                   '6/24', '6/26']], ],
                         '224': [[['0', '0', '0', '1', '0', '0', '0']], ],
                         '225': [[['0', '0', '0', '2', '0', '0', '0']], ],
                         '226': [[['0', '0', '0', '2', '0', '0', '0']], ],
                         '227': [[['0', '0', '0', '2', '0', '0', '0']], ],
                         '228': [[['0', '0', '0', '2', '0', '0', '0']], ],
                         '230': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '1/101',
                                   '1/102']], ],
                         '231': [[['0', '0', '0', '1', '0', '0', '0']], ],
                         '232': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28']], ],
                         '233': [[['1/1', '1/3', '1/5', '1/7', '1/9', '1/11', '1/13', '1/15', '1/17', '1/19', '1/21',
                                   '1/23', '1/25', '1/27'],
                                  ['1/2', '1/4', '1/6', '1/8', '1/10', '1/12', '1/14', '1/16', '1/18', '1/20', '1/22',
                                   '1/24', '1/26', '1/28']],
                                 [['2/1', '2/3', '2/5', '2/7', '2/9', '2/11', '2/13', '2/15', '2/17', '2/19', '2/21',
                                   '2/23', '2/25', '2/27'],
                                  ['2/2', '2/4', '2/6', '2/8', '2/10', '2/12', '2/14', '2/16', '2/18', '2/20', '2/22',
                                   '2/24', '2/26', '2/28']],
                                 [['3/1', '3/3', '3/5', '3/7', '3/9', '3/11', '3/13', '3/15', '3/17', '3/19', '3/21',
                                   '3/23', '3/25', '3/27'],
                                  ['3/2', '3/4', '3/6', '3/8', '3/10', '3/12', '3/14', '3/16', '3/18', '3/20', '3/22',
                                   '3/24', '3/26', '3/28']],
                                 [['4/1', '4/3', '4/5', '4/7', '4/9', '4/11', '4/13', '4/15', '4/17', '4/19', '4/21',
                                   '4/23', '4/25', '4/27'],
                                  ['4/2', '4/4', '4/6', '4/8', '4/10', '4/12', '4/14', '4/16', '4/18', '4/20', '4/22',
                                   '4/24', '4/26', '4/28']],
                                 [['5/1', '5/3', '5/5', '5/7', '5/9', '5/11', '5/13', '5/15', '5/17', '5/19', '5/21',
                                   '5/23', '5/25', '5/27'],
                                  ['5/2', '5/4', '5/6', '5/8', '5/10', '5/12', '5/14', '5/16', '5/18', '5/20', '5/22',
                                   '5/24', '5/26', '5/28']],
                                 [['6/1', '6/3', '6/5', '6/7', '6/9', '6/11', '6/13', '6/15', '6/17', '6/19', '6/21',
                                   '6/23', '6/25', '6/27'],
                                  ['6/2', '6/4', '6/6', '6/8', '6/10', '6/12', '6/14', '6/16', '6/18', '6/20', '6/22',
                                   '6/24', '6/26', '6/28']], ],
                         '234': [[['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11',
                                   '1/12', '1/13', '1/14', '1/15', '1/16']],
                                 [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11',
                                   '2/12', '2/13', '2/14', '2/15', '2/16']],
                                 [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11',
                                   '3/12', '3/13', '3/14', '3/15', '3/16']],
                                 [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11',
                                   '4/12', '4/13', '4/14', '4/15', '4/16']], ],
                         '235': [
                             [['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                              ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23',
                               '1/24']],
                             [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12'],
                              ['2/13', '2/14', '2/15', '2/16', '2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23',
                               '2/24']],
                             [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11', '3/12'],
                              ['3/13', '3/14', '3/15', '3/16', '3/17', '3/18', '3/19', '3/20', '3/21', '3/22', '3/23',
                               '3/24']],
                             [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12'],
                              ['4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23',
                               '4/24']],
                             [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11', '5/12'],
                              ['5/13', '5/14', '5/15', '5/16', '5/17', '5/18', '5/19', '5/20', '5/21', '5/22', '5/23',
                               '5/24']],
                             [['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12'],
                              ['6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23',
                               '6/24']],
                             [['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11', '7/12'],
                              ['7/13', '7/14', '7/15', '7/16', '7/17', '7/18', '7/19', '7/20', '7/21', '7/22', '7/23',
                               '7/24']],
                             [['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11', '8/12'],
                              ['8/13', '8/14', '8/15', '8/16', '8/17', '8/18', '8/19', '8/20', '8/21', '8/22', '8/23',
                               '8/24']], ],
                         '236': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29',
                                   '31', '33', '35', '37', '39', '41', '43', '45', '47'],
                                  ['2', '4', '5', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30',
                                   '32', '34', '36', '38', '40', '42', '44', '46', '48'], ['49', '50']], ],
                         '237': [[['1/1', '1/3', '1/5', '1/7', '1/9', '1/11', '1/13', '1/15', '1/17', '1/19', '1/21',
                                   '1/23'],
                                  ['1/2', '1/4', '1/6', '1/8', '1/10', '1/12', '1/14', '1/16', '1/18', '1/20', '1/22',
                                   '1/24']],
                                 [['2/1', '2/3', '2/5', '2/7', '2/9', '2/11', '2/13', '2/15', '2/17', '2/19', '2/21',
                                   '2/23'],
                                  ['2/2', '2/4', '2/6', '2/8', '2/10', '2/12', '2/14', '2/16', '2/18', '2/20', '2/22',
                                   '2/24']],
                                 [['3/1', '3/3', '3/5', '3/7', '3/9', '3/11', '3/13', '3/15', '3/17', '3/19', '3/21',
                                   '3/23'],
                                  ['3/2', '3/4', '3/6', '3/8', '3/10', '3/12', '3/14', '3/16', '3/18', '3/20', '3/22',
                                   '3/24']],
                                 [['4/1', '4/3', '4/5', '4/7', '4/9', '4/11', '4/13', '4/15', '4/17', '4/19', '4/21',
                                   '4/23'],
                                  ['4/2', '4/4', '4/6', '4/8', '4/10', '4/12', '4/14', '4/16', '4/18', '4/20', '4/22',
                                   '4/24']],
                                 [['5/1', '5/3', '5/5', '5/7', '5/9', '5/11', '5/13', '5/15', '5/17', '5/19', '5/21',
                                   '5/23'],
                                  ['5/2', '5/4', '5/6', '5/8', '5/10', '5/12', '5/14', '5/16', '5/18', '5/20', '5/22',
                                   '5/24']],
                                 [['6/1', '6/3', '6/5', '6/7', '6/9', '6/11', '6/13', '6/15', '6/17', '6/19', '6/21',
                                   '6/23'],
                                  ['6/2', '6/4', '6/6', '6/8', '6/10', '6/12', '6/14', '6/16', '6/18', '6/20', '6/22',
                                   '6/24']], ],
                         '238': [[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']], ],
                         '239': [
                             [['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                              ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23',
                               '1/24']],
                             [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12'],
                              ['2/13', '2/14', '2/15', '2/16', '2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23',
                               '2/24']],
                             [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11', '3/12'],
                              ['3/13', '3/14', '3/15', '3/16', '3/17', '3/18', '3/19', '3/20', '3/21', '3/22', '3/23',
                               '3/24']],
                             [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12'],
                              ['4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23',
                               '4/24']],
                             [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11', '5/12'],
                              ['5/13', '5/14', '5/15', '5/16', '5/17', '5/18', '5/19', '5/20', '5/21', '5/22', '5/23',
                               '5/24']],
                             [['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12'],
                              ['6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23',
                               '6/24']],
                             [['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11', '7/12'],
                              ['7/13', '7/14', '7/15', '7/16', '7/17', '7/18', '7/19', '7/20', '7/21', '7/22', '7/23',
                               '7/24']],
                             [['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11', '8/12'],
                              ['8/13', '8/14', '8/15', '8/16', '8/17', '8/18', '8/19', '8/20', '8/21', '8/22', '8/23',
                               '8/24']], ],
                         '240': [[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '57', '59'],
                                  ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '58',
                                   '60']], ],
                         '241': [
                             [['1/1', '1/2', '1/3', '1/4'], ['2/1', '2/2', '2/3', '2/4'], ['3/1', '3/2', '3/3', '3/4'],
                              ['4/1', '4/2', '4/3', '4/4'], ['5/1', '5/2', '5/3', '5/4'], ['6/1', '6/2', '6/3', '6/4'],
                              ['7/1', '7/2', '7/3', '7/4'], ['8/1', '8/2', '8/3', '8/4']], ],
                         '242': [[['1', '2', '3', '4', '5', '6']], ],
                         '243': [[['1', '3', '5', '7', '9', '11'], ['2', '4', '6', '8', '10', '12']], ],
                         '244': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '201', '203'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '202', '204',
                                   '301', '302']], ],
                         '245': [[['1/1', '1/3', '1/5', '1/7', '1/9', '1/11', '1/13', '1/15', '1/17', '1/19', '1/21',
                                   '1/23', '1/25', '1/27', '1/29', '1/31', '1/33', '1/35', '1/37', '1/39', '1/41',
                                   '1/43', '1/45', '1/47', '1/101', '1/103'],
                                  ['1/2', '1/4', '1/6', '1/8', '1/10', '1/12', '1/14', '1/16', '1/18', '1/20', '1/22',
                                   '1/24', '1/26', '1/28', '1/30', '1/32', '1/34', '1/36', '1/38', '1/40', '1/42',
                                   '1/44', '1/46', '1/48', '1/102', '1/104']],
                                 [['2/1', '2/3', '2/5', '2/7', '2/9', '2/11', '2/13', '2/15', '2/17', '2/19', '2/21',
                                   '2/23', '2/25', '2/27', '2/29', '2/31', '2/33', '2/35', '2/37', '2/39', '2/41',
                                   '2/43', '2/45', '2/47', '2/101', '2/103'],
                                  ['2/2', '2/4', '2/6', '2/8', '2/10', '2/12', '2/14', '2/16', '2/18', '2/20', '2/22',
                                   '2/24', '2/26', '2/28', '2/30', '2/32', '2/34', '2/36', '2/38', '2/40', '2/42',
                                   '2/44', '2/46', '2/48', '2/102', '2/104']], ],
                         '246': [[['1', '3', '5', '7', '9', '11', '13', '15'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '101']], ],
                         '247': [[['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11',
                                   '1/12', '1/13', '1/14', '1/15', '1/16']],
                                 [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11',
                                   '2/12', '2/13', '2/14', '2/15', '2/16']],
                                 [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11',
                                   '3/12', '3/13', '3/14', '3/15', '3/16']],
                                 [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11',
                                   '4/12', '4/13', '4/14', '4/15', '4/16']],
                                 [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11',
                                   '5/12', '5/13', '5/14', '5/15', '5/16']],
                                 [['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11',
                                   '6/12', '6/13', '6/14', '6/15', '6/16']],
                                 [['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11',
                                   '7/12', '7/13', '7/14', '7/15', '7/16']],
                                 [['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11',
                                   '8/12', '8/13', '8/14', '8/15', '8/16']], ],
                         '248': [[['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11',
                                   '1/12', '1/13', '1/14', '1/15', '1/16']],
                                 [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11',
                                   '2/12', '2/13', '2/14', '2/15', '2/16']],
                                 [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11',
                                   '3/12', '3/13', '3/14', '3/15', '3/16']],
                                 [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11',
                                   '4/12', '4/13', '4/14', '4/15', '4/16']], ],
                         '249': [[['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11',
                                   '1/12', '1/13', '1/14', '1/15', '1/16']],
                                 [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11',
                                   '2/12', '2/13', '2/14', '2/15', '2/16']],
                                 [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11',
                                   '3/12', '3/13', '3/14', '3/15', '3/16']],
                                 [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11',
                                   '4/12', '4/13', '4/14', '4/15', '4/16']],
                                 [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11',
                                   '5/12', '5/13', '5/14', '5/15', '5/16']],
                                 [['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11',
                                   '6/12', '6/13', '6/14', '6/15', '6/16']],
                                 [['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11',
                                   '7/12', '7/13', '7/14', '7/15', '7/16']],
                                 [['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11',
                                   '8/12', '8/13', '8/14', '8/15', '8/16']], ],
                         '250': [[['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11',
                                   '1/12', '1/13', '1/14', '1/15', '1/16']],
                                 [['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11',
                                   '2/12', '2/13', '2/14', '2/15', '2/16']],
                                 [['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11',
                                   '3/12', '3/13', '3/14', '3/15', '3/16']],
                                 [['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11',
                                   '4/12', '4/13', '4/14', '4/15', '4/16']],
                                 [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11',
                                   '5/12', '5/13', '5/14', '5/15', '5/16']],
                                 [['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11',
                                   '6/12', '6/13', '6/14', '6/15', '6/16']],
                                 [['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11',
                                   '7/12', '7/13', '7/14', '7/15', '7/16']],
                                 [['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11',
                                   '8/12', '8/13', '8/14', '8/15', '8/16']], ],
                         '251': [[['1/1', '1/3', '1/5', '1/7', '1/9', '1/11', '1/13', '1/15', '1/17', '1/19', '1/21',
                                   '1/23', '1/25', '1/27'],
                                  ['1/2', '1/4', '1/6', '1/8', '1/10', '1/12', '1/14', '1/16', '1/18', '1/20', '1/22',
                                   '1/24', '1/26', '1/28']],
                                 [['2/1', '2/3', '2/5', '2/7', '2/9', '2/11', '2/13', '2/15', '2/17', '2/19', '2/21',
                                   '2/23', '2/25', '2/27'],
                                  ['2/2', '2/4', '2/6', '2/8', '2/10', '2/12', '2/14', '2/16', '2/18', '2/20', '2/22',
                                   '2/24', '2/26', '2/28']],
                                 [['3/1', '3/3', '3/5', '3/7', '3/9', '3/11', '3/13', '3/15', '3/17', '3/19', '3/21',
                                   '3/23', '3/25', '3/27'],
                                  ['3/2', '3/4', '3/6', '3/8', '3/10', '3/12', '3/14', '3/16', '3/18', '3/20', '3/22',
                                   '3/24', '3/26', '3/28']],
                                 [['4/1', '4/3', '4/5', '4/7', '4/9', '4/11', '4/13', '4/15', '4/17', '4/19', '4/21',
                                   '4/23', '4/25', '4/27'],
                                  ['4/2', '4/4', '4/6', '4/8', '4/10', '4/12', '4/14', '4/16', '4/18', '4/20', '4/22',
                                   '4/24', '4/26', '4/28']],
                                 [['5/1', '5/3', '5/5', '5/7', '5/9', '5/11', '5/13', '5/15', '5/17', '5/19', '5/21',
                                   '5/23', '5/25', '5/27'],
                                  ['5/2', '5/4', '5/6', '5/8', '5/10', '5/12', '5/14', '5/16', '5/18', '5/20', '5/22',
                                   '5/24', '5/26', '5/28']],
                                 [['6/1', '6/3', '6/5', '6/7', '6/9', '6/11', '6/13', '6/15', '6/17', '6/19', '6/21',
                                   '6/23', '6/25', '6/27'],
                                  ['6/2', '6/4', '6/6', '6/8', '6/10', '6/12', '6/14', '6/16', '6/18', '6/20', '6/22',
                                   '6/24', '6/26', '6/28']], ],
                         '252': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26']], ],
                         '253': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '254': [[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '25', '26'],
                                  ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '27',
                                   '28']], ],
                         '255': [[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '25', '27'],
                                  ['13', '14', '15', '17', '17', '18', '19', '20', '21', '22', '23', '24', '26',
                                   '28']], ],
                         '256': [[['0', '0', '0', '1', '2', '0', '0', '0']], ],
                         '257': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26']], ],
                         '258': [[['1', '2', '3', '4', '5', '6', '7', '8']], ],
                         '259': [
                             [['49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '105', '107'],
                              ['61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '106',
                               '108']], ],
                         '260': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '265': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28']], ],
                         '266': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '267': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26']], ],
                         '268': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20']], ],
                         '269': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26', '27',
                                   '28']], ],
                         '270': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29',
                                   '31', '33', '35', '37', '39', '41', '43', '45', '47'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30',
                                   '32', '34', '36', '38', '40', '42', '44', '46', '48', '49', '50', '51', '52']], ],
                         '273': [[['4194304000', '4194304256', '4194304512', '4194304768', '4194305024', '4194305280',
                                   '4194305536', '4194305792', '4194306048', '4194306304', '4194306560', '4194306816',
                                   '4194307072', '4194307328', '4194307584', '4194307840']],
                                 [['4194312192', '4194312448', '4194312704', '4194312960', '4194313216', '4194313472',
                                   '4194313728', '4194313984', '4194314240', '4194314496', '4194314752', '4194315008',
                                   '4194315264', '4194315520', '4194315776', '4194316032']],
                                 [['234930176', '234930240', '234930304', '234930368']],
                                 [['234938368', '234938432', '234938496', '234938560']],
                                 [['234946560', '234946624']],
                                 [['234954752', '234954816']], ],
                         '280': [[['4194304000', '4194304256', '4194304512', '4194304768', '4194305024', '4194305280',
                                   '4194305536', '4194305792', '4194306048', '4194306304', '4194306560', '4194306816',
                                   '4194307072', '4194307328', '4194307584', '4194307840']],
                                 [['4194312192', '4194312448', '4194312704', '4194312960', '4194313216', '4194313472',
                                   '4194313728', '4194313984', '4194314240', '4194314496', '4194314752', '4194315008',
                                   '4194315264', '4194315520', '4194315776', '4194316032']],
                                 [['234930176', '234930240', '234930304', '234930368']],
                                 [['234938368', '234938432', '234938496', '234938560']],
                                 [['234946560', '234946624']],
                                 [['234954752', '234954816']], ],
                         '282': [[['1', '2', '3', '4', '5', '6', '7', '8', '9'], ], ],
                         '283': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28']], ],
                         '290': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35', '37', '39', '41', '43', '45', '47', '49', '51'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36', '38', '40', '42', '44', '46', '48', '50', '52']], ],
                         '291': [[['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                                  ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26']], ],
                         '296': [[['1', '3', '5', '7', '9'],
                                  ['2', '4', '6', '8', '10']], ],
                         '297': [[['1', '3', '5', '7'],
                                  ['2', '4', '6', '8', '9', '10']], ],
                     },)

set_CreateVlan = [
    #     .1.3.6.1.2.1.17.7.1.4.3.1.1					dot1qVlanStaticName
    ['.1.3.6.1.2.1.17.7.1.4.3.1.1', '{1}', '{2}', 'OCTETSTR'],
    #     .1.3.6.1.2.1.17.7.1.4.3.1.2					dot1qVlanStaticEgressPorts
    ['.1.3.6.1.2.1.17.7.1.4.3.1.2', '{1}', '{3}', 'OCTETSTR'],
    #     .1.3.6.1.2.1.17.7.1.4.3.1.5					dot1qVlanStaticRowStatus
    ['.1.3.6.1.2.1.17.7.1.4.3.1.5', '{1}', '4', 'INTEGER'],
]

set_IpifCfg = [
    #     .1.3.6.1.2.1.16.19.11.1.1						netConfigIPAddress
    ['.1.3.6.1.2.1.16.19.11.1.1', '5121', '{1}', 'IPADDR'],
    #     .1.3.6.1.2.1.16.19.11.1.2						netConfigSubnetMask
    ['.1.3.6.1.2.1.16.19.11.1.2', '5121', '{2}', 'IPADDR'],
    #     .1.3.6.1.2.1.16.19.12						netDefaultGateway
    ['.1.3.6.1.2.1.16.19.12', '0', '{3}', 'IPADDR'],
]
