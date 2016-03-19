SWToolz-Core - перерождение [SWToolz](https://github.com/xcme/swtoolz), старого, доброго, лампового и теплого одновременно.


## Предназначение сервиса

Сервис был разработан для облегчения управления сетевыми устройствами как в мультивендорной среде, так и в среде с разнообразным модельным рядом одного вендора. При работе с протоколом SNMP для получения определенных параметров приходится обращаться к идентификаторам этих параметров (или объектов) - OID. Очень часто одни и те же параметры для разных моделей устройств имеют уникальные OID, не совпадающие с аналогичными OID для других моделей. SWToolz-Core предоставляет единый интерфейс управления сетевым оборудованием, благодаря которому не приходится задумываться о таких мелочах. Любой метод, например set_AdminStatus, будет работать для любой модели любого вендора.

Это позволяет использовать swtoolz-core для интеграции с биллингом и системами отслеживания заявок, а также упрощает разработку собственного WEB-интерфейса для управления сетевым оборудованием.

Ниже приведен скриншот web-страницы проекта PortViewer 2.0, основанного на swtoolz-core:
<p align="center">
  <img src="https://github.com/xcme/swtoolz-core/blob/master/portviewer2.png?raw=true" alt="PortViewer 2.0 based on swtoolz-core"/>
</p>

## Возможности swtoolz-core

- Автоопределение устройства и соответствующего файла конфигурации
- Классификация моделей как по sysDescr, так и по sysName
- Определение произвольного набора методов Get/Walk/Set для каждой модели устройства
- Подстановка произвольного числа пользовательских параметров в любой OID
- Одновременный вызов сразу нескольких методов
- Упаковка нескольких запросов в один пакет

## Особенности работы и отличия от swtoolz

- Работа системным сервисом (daemon) под FreeBSD/Linux
- Отсутствие привязки к конкретному оборудованию или вендору
- Гибкая система конфигурирования
- Изменение модулей не требует перезагрузки сервиса
- Взаимодействие с сервисом осуществляется через API путем запроса соответствующего URL
- Результат опроса возвращается в JSON

## Требования

- Операционная система FreeBSD или Linux
- Python2 с модулем netsnmp. Может потребоваться установка python-pynetsnmp и python-netsnmp

## Принцип работы

SWToolz-Core запускается системных сервисом и начинает опрашивать порт 7377 (по умолчанию). При подключении клиента и получении HTTP GET запроса, полученный URL разбирается на параметры. Минимальный набор параметров - имя пользователя, IP-адрес устройства, идентификатор SNMP-community, соответствующий пользователю, и вызываемый метод. К примеру, были получены такие параметры:

Параметр         | Описание
---------------- | --------
Имя пользователя | default
IP-адрес         | 10.90.90.90
Индекс community | 1
Метод            | walk_ifAlias

При этом произойдет следующее:

- SWToolz-Core разберет запрос, посмотрит в основной файл конфигурации и извлечет SNMP-community с индексом **1** из набора возможных community для пользователя **default**.
- После этого демон запустит отдельный поток в котором будет происходить вся дальнейшая работа:
  - Сервис запросит *sysDescr* и *sysName* (одним пакетом будут запрошены все параметры из **default_info**) у устройства с IP-адресом **10.90.90.90**, обратившись к нему с полученным SNMP-community.
  - После получения ответа выполняется классификация устройства на основе параметров *sysDescr* и *sysName* и пользовательских настроек
  - Импортируется модуль (файл с настройками), соответствующий данному классу устройств
  - Из этого модуля выбирается объект **walk_ifAlias**
  - Объект интерпретируется и в него помещаются пользовательские параметры (если заданы)
  - Выполняется опрос устройства
  - Пользователю возвращается результат в JSON
- Независимо от полученных результатов поток завершает свою работу

## Конфигурирование сервиса 
### Описание параметров в файле swconfig.py

Параметр         |  Описание
---------------- | --------
interface        | Интерфейс, на котором демон будет слушать сокет.
port             | TCP-порт для прослушки (по умолчанию 7377).
sleep_int        | Пауза при опросе сокета в секундах (отсутствие паузы приведет к 100% загрузке CPU).
stats_int        | Интервал для статистики в файле журнала
set_iter_delay   | Пауза в секундах после set-операций
snmp_timeout     | Таймаут ожидания ответа для SNMP-запроса (в микросекундах)
snmp_retries     | Количество дополнительных попыток для SNMP-запроса. Значение '1' означает, что всего будет предпринято 2 попытки
no_retries       | Список методов, для которых значение snmp_retries будет всегда считаться равным нулю
logfile          | Файл журнала
users            | Пользователи и их наборы snmp-community
default_info     | Имена и OID'ы параметров, запрашиваемых у устройства в обязательном порядке
models_by_desc   | Соответствие описаний моделей их названиям. Список проверяется до первого соответствия
http_header      | Шаблон HTTP-заголовка для ответа клиенту
debug_mode       | Режим отладки. Если включен, то в лог-файл будет отправляться дополнительная информация

#### Описание параметра 'users'

Параметр *users* представлен в виде словаря Python. Значение каждого элемента этого словаря, в свою очередь, тоже является словарем. В нем хранится соответствие SNMP-community определенному индексу.

```
users = {
    'default'  : {'1' : 'public', '2' : 'private'},
    'test'     : {'6' : 'my_read', '7' : 'my_write'},
    }
```

Благодаря *users* значение SNMP-community не передается открытым текстом в запросах.

#### Описание параметра 'default_info'

Параметр *default_info* представлен в виде словаря Python, в котором ключ содержит имя параметра, а значение - соответствующий ему OID.
```
default_info = {
    'sys_descr'    : '.1.3.6.1.2.1.1.1.0',
    'sys_uptime'   : '.1.3.6.1.2.1.1.3.0',
    'sys_name'     : '.1.3.6.1.2.1.1.5.0',
    'sys_location' : '.1.3.6.1.2.1.1.6.0',
    }
```
Все эти параметры будут запрошены у устройства при первом обращении. Параметры *sys_name* и *sys_descr* зарезервированы и используются для определения модели устройства

#### Описание параметра 'models_by_desc'

Параметр *models_by_desc* представлен в виде списка словарей. Ключом словаря является подстрока, входящая в строки в *sysDescr* или *sysName*. При этом *sysName* имеет приоритет над *sysDescr*. Значением словаря является локально значимое имя модели и соответствующего ей файла в директории **./devices**.

Пример:
```
models_by_desc = [
    {'DES-3200-28'    : 'DES-3200-28'},
    {'DES-3200-28/C1' : 'DES-3200-28_C1'},
    {'DES-3028'       : 'DES-3028'},
    {'DES-3200-18'    : 'DES-3200-18'},
    {'DES-3200-18/C1' : 'DES-3200-18_C1'},
    {'DGS-3100-24TG'  : 'DGS-3100-24TG'},
    {'DGS-3120-24SC'  : 'DGS-3120-24SC'},
    {'DGS-3120-24SC/B': 'DGS-3120-24SC_B'},
    {'DGS-3000-28SC'  : 'DGS-3000-28SC'},
    {'DGS-3000-24TC'  : 'DGS-3000-24TC'},
    {'DGS-3612G'      : 'DGS-3612G'},
    {'DGS-3627G'      : 'DGS-3627G'},
    {'BigIron 4000'   : 'Foundry'},
    {'FastIron 800'   : 'Foundry'},
    {'FastIron SX 800': 'Foundry'},
    {'BigIron RX'     : 'BigIron-RX'},
    {'c2950-MGMT'     : 'WS-C2950G-48-EI'},
    {'Cat3550-12G'    : 'WS-C3550-12G'},
    {'GGC-3750G-16TD' : 'WS-C3750G-16TD'},
    {'MES2124'        : 'MES-2124'},
    {'MES3124F'       : 'MES-3124F'},
    ]
```

Данный список проверяется до первого соответствия. Если ключ входит в значение *sysName* или *sysDescr*, то проверка прекращается и названием модели считается значение ключа словаря. К примеру, если было найдено вхождение **FastIron SX 800** в параметр *sysName* или *sysDescr*, то названием модели будет **Foundry** и при обращении к устройству будет импортирован модуль с именем **Foundry**.

## Конфигурирование модулей

Модули хранятся в директории **./devices**. Каждый модуль содержит описания методов, которые могут быть вызваны для данного устройства. Метод с точки зрения Python является объектом и может быть представлен в виде **кортежа**, **словаря** или **списка**. Тип объекта указывает swtoolz-core на то, как надо интерпретировать объект.

### Кортежи (неизменяемые объекты)

Пример объекта, являющегося кортежем:
```
# swL2PortInfoMediumType
MediumType = ({
    '1' : 'copper',
    '2' : 'fiber',
    },)
```
Когда swtoolz-core обнаруживает такой объект, он возвращает его 'как есть'. Это удобно использовать для получения расшифровки параметров в виде JSON. В данном случае смысл здесь примерно такой же, как и в подключении MIB - если при помощи одного метода мы получаем численные значения параметров, то сразу после этого (или одновременно) мы можем сразу же получить и расшифровку этих параметров.

Это решает одну серьезную проблему, которая может возникнуть при использовании MIB. К примеру, мы получили значение актуальной скорости порта коммутатора, которое говорит о том, что линк поднят в режиме 100 мегабит/фуллдуплекс. При этом в различных MIB для различных моделей это значение может расшифровываться как '100M-Full', так и '100M Full' или '100 Mb Full' или '100M fullduplex' и т.д. Человеку понятно, а программе не очень. Используя кортежи можно легко привести все к "одному знаменателю", получая расшифровку параметра в удобном для своих сервисов виде.

**ВНИМАНИЕ! Чтобы объект считался кортежем, он должен содержать запятую!**

### Словари (наборы для snmpwalk- и snmpget-операций)

Пример объекта, являющегося словарем (snmpwalk):
```
walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.2          swL2PortInfoMediumType
    'MediumType'      : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.5          swL2PortInfoLinkStatus
    'ActualStatus'    : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.5',
#    ActualSpeed         .1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.6          swL2PortInfoNwayStatus
    'ActualSpeed'     : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.6',
#    AdminStatus         .1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4          swL2PortCtrlAdminState
    'AdminStatus'     : '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4',
#    AdminSpeed          .1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.5          swL2PortCtrlNwayState
    'AdminSpeed'      : '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.5',
#    AdminFlow           .1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.6          swL2PortCtrlFlowCtrlState
    'AdminFlow'       : '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.6',
    }
```

Когда swtoolz-core обнаруживает такой объект, он интерпретирует его как набор метрик, для которых надо выполнить операции **snmpwalk** или **snmpget**. По умолчанию типом операции считается **snmpwalk**, но если хотя бы в одном имени метрики присутствует точка, то для всех OID в словаре будет выполнена операция **snmpget**.

Пример объекта, являющегося словарем (snmpget):
```
get_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1          swL2PortInfoPortIndex
    'PortIndex..1'    : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.1.1',
    'PortIndex..2'    : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.2.1',
....
....
    'PortIndex..24'   : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.24.1',
    'PortIndex..25c'  : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.25.1',
    'PortIndex..25f'  : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.25.2',
    'PortIndex..26c'  : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.26.1',
    'PortIndex..26f'  : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.26.2',
    'PortIndex..27'   : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.27.2',
    'PortIndex..28'   : '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.1.28.2',
    }


```

Тип операции оказывает влияние на имя метрики, возвращаемой в ответе клиенту. В случае *snmpwalk* имя метрики будет получено по следующей формуле:
```
имя_метрики = результат - значение_ключа
```

Например, для параметра *ActualStatus* оно будет вычислено так:
```
.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.5.25.1 - .1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.5 = 25.1
```

В случае *snmpget* имя метрики будет получено по формуле:
```
имя_метрики = последние № чисел из результата (где № - количество точек в имени ключа)
```

Например, для параметра *PortIndex* имена ключей из примера выше будут такими:
```
'1.1',
'2.1',
....
....
'24.1',
'25.1',
'25.2',
'26.1',
'26.2',
'27.2',
'28.2',
```

Поскольку в имени ключа содержатся две точки (PortIndex..1), то из результирующего OID используются 2 последних числа.

Значения после первой точки игнорируются. То есть нет разницы задавать ли имена 'PortIndex..26c' и 'PortIndex..26f' или же 'PortIndex..abcd' и 'PortIndex..dcba' - все равно ключи метрик будут, в данном случае, '26.1' и '26.2'.

Само же имя метрики из словаря в ответе будет являться ключом словаря результатов. Ниже приведен пример вызова метода **get_SinglePort** с параметром **25**:
```
"data": {
    "AdminStatus": {
	"25.100": "3",
	"25.101": "3"
    },
    "ActualStatus": {
	"25.100": "2",
	"25.101": "3"
    },
    "ActualSpeed": {
	"25.100": "7",
	"25.101": "1"
    },
    "MediumType": {
	"25.100": "100",
	"25.101": "101"
	},
    "AdminFlow": {
	"25.100": "2",
	"25.101": "2"
    },
    "PortType": {
	"25": "2"
    },
    "AdminSpeed": {
	"25.100": "1",
	"25.101": "1"
    },
    "PortDescr": {
	"25": "Uplink"
    }
}
```

В общем и целом работа с именами метрик идентична поведению [Briseis](https://github.com/xcme/briseis).

### Списки (наборы для snmpset-операций)

Пример объекта, являющегося списком:
```
set_AdminStatus = [
#     .1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4                             swL2PortCtrlAdminState
    ['.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4.%s', '1', '%s', 'INTEGER'],
    ]
```

Когда swtoolz-core обнаруживает такой объект, он интерпретирует его как набор параметров, для которых надо выполнить операцию **snmpset**.

Параметр | Описание
-------- | --------
tag  | fully qualified, dotted-decimal, numeric OID
iid  | the dotted-decimal, instance identifier
val  | the SNMP data value
type | SNMP data type

Пример: **['.1.3.6.1.2.1.17.7.1.4.3.1.2','777','\x00\x00\x00\xf0\x00\x00\x00\x00','OCTETSTR']**  
Эквивалентная команда: **snmpset -v2c -c \<WComm\> \<IP\> .1.3.6.1.2.1.17.7.1.4.3.1.2.777 x 000000f000000000**

Результат команды snmpset будет либо 1 (успех) либо 0 (неудача). Пример:

```
"data":	{
    "set_AdminStatus": 1
    }
```


## Пояснения к работе swtoolz-core

### Использование сервиса

Для вызова необходимого метода достаточно обратиться к соответствующему URL. Пример:

```
http://my.host:7377/default/10.90.90.905/1/walk_ifAlias
```

Чтобы передать сервису определенный параметр, нужно указать его после имени метода через символ '**/**':
```
http://my.host:7377/default/10.90.90.905/1/get_SinglePort/25
```

Можно вызывать несколько методов одновременно, разделяя их знаком '**+**':

```
http://my.host:7377/default/10.90.90.905/1/get_SinglePort/25+/get_SinglePort/26
```

Можно одновременно вызывать несколько методов с разными типами и разным количеством параметров:
```
http://my.host:7377/default/10.90.90.90/2/get_SinglePort/25+/walk_ifAlias+/set_AdminStatus/1/2
```

**ВНИМАНИЕ! Перед названием каждого метода и перед каждым параметром должен стоять знак '/'**!

### Использование пользовательских параметров при опросе устройств

SWToolz-Core позволяет использовать внутри OID параметры, передаваемые в URL. В случае, если ожидается подстановка параметра, следует использовать зарезервированные символы '**%s**'. Выше, в описании метода '*set_AdminStatus*', приведен пример их использования. Параметры указываются в URL после имени метода и затем последовательно подставляются вместо символов '**%s**'. Таким образом, в случае вызова метода '*set_AdminStatus*' с параметрами *1* и *2*, результатом будет:
```
['.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4.1', '1', '2', 'INTEGER'],
```

Напомню, что изначально объект был описан так:
```
['.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4.%s', '1', '%s', 'INTEGER'],
```

### Обратная связь с пользователем

Сервис возвращает в ответе информацию о том, с каким устройством ведется работа и как был распознан запрос. Пример:
```
"request": {
    "errors": [0],
    "comm_index": "2",
    "data": [{
	"0": "set_AdminStatus",
	"1": "1",
	"2": "2"
    }],
    "user": "default",
    "target": "10.90.90.90"
}
```

Параметр '*errors*' содержит код возможных ошибок. Ниже приведена расшифровка кодов:

Параметр | Описание
-------- | --------
0 | OK
1 | Missing mandatory parameters: /user, /target, /comm_index
2 | User is not found
3 | Snmp-community is not defined for this index
4 | IP-address is not correct

Таким образом, код **0** сообщает о том, что ошибок в запросе не обнаружено.

### Одновременный запрос нескольких параметров

Все параметры, находящиеся внутри одного объекта (кортежа, словаря или списка) опрашиваются одновременно. Для *snmpget* и *snmpset* запросов это означает, что для каждого объекта будет отправлен всего один пакет. Ответ при этом тоже поступит в одном пакете. Так, например, метрики *PortIndex* (из примера выше) при вызове метода *get_PortIndex* будут получены одновременно.

Если же используется *snmpwalk*, то запросы также выполняются одновременно, а их число соответствует длине самой короткой ветви с OID. Например, при вызове метода *walk_AllPorts* одновременно придут результаты '*MediumType*', '*ActualStatus*', '*ActualSpeed*', '*AdminStatus*',  '*AdminSpeed*' и '*AdminFlow*' для порта №1. В следующем пакете - для порта №2 и так далее. Когда одна из веток закончится, опрос будет прекращен. Поэтому, чтобы были получены все необходимые параметры, **ветки должны быть одинаковой длины**. Иными словами, нельзя одним методом получить и список описаний портов и список MAC-адресов, так как длина этих списков различна. А вот свойства порта, находящиеся в одном разделе MIB, будут иметь одинаковую длину, поэтому есть смысл опрашивать их вместе.

Данная методика увеличивает скорость и надежность получения данных.

### Опрос недоступного оборудования и неправильные запросы

Опрос устройства выполняется только в том случае, если пришел ответ на первый запрос (где запрашиваются параметры из *default_info*). Если ответ получен не был, то опрос считается завершенным, а пользователь получит ответ, где поле 'data' в ответе будет пустым.

Если же сервис не распознал запрос пользователя, то поле 'data' в ответе также будет пустым. При этом, если само устройство доступно, параметры из *default_info* будут содержать ответ устройства.

При ошибках импортирования модулей или при вызове несуществующих параметров информация об этом попадает в лог сервиса.

## Установка под FreeBSD
+ Скопируйте файл **swtoolz-core** из директории '*freebsd*' в '*/usr/local/etc/rc.d/*', а остальные файлы в '*/usr/local/etc/swtoolz-core/*'.  
+ Добавьте строку **swtoolz_core_enable="YES"** в файл '*/etc/rc.conf*'.
+ Убедитесь, что firewall разрешает SNMP-запросы.
+ Запустите сервис командой **service swtoolz-core start**.

## Установка под Lunix
+ Скопируйте файл **swtoolz-core** из директории '*linux*'  в '*/etc/init.d/*', а остальные файлы в '*/usr/local/etc/swtoolz-core/*'.  
+ Убедитесь, что firewall разрешает SNMP-запросы.
+ Запустите сервис командой **service swtoolz-core start**.


## Список изменений

### [1.0.0] - 2015.03.18

Релиз версии 1.0.0

## P.S.

Обсудить проект можно в конференции ccna@conference.jabber.ru