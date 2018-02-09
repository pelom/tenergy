
from pyepsolartracer.client import EPsolarTracerClient
#from pyepsolartracer.registers import registers,coils
from pyepsolartracer.registers2 import coils, registersChargingEquipment, registersChargingEquipmentRealTime, registersChargingEquipmentRealTimeStatus, registersChargingEquipmentRealTimeStatics
from test.testdata import ModbusMockClient as ModbusClient

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

serialclient = ModbusClient()
#serialclient = None

client = EPsolarTracerClient(serialclient = serialclient)
client.connect()

response = client.read_device_info()

print response.information[0]
print "Manufacturer:", repr(response.information[0])
print "Model:", repr(response.information[1])
print "Version:", repr(response.information[2])

response = client.read_input("Charging equipment rated input voltage")
print str(response)

print 'Controlador de carga'
for reg in registersChargingEquipment:
    print '[Name - ' + reg.name + '] ', '[Description - ' + reg.description + ']'
    print client.read_input(reg.name)

print ''
print 'Controlador de carga - Tempo Real'
for reg in registersChargingEquipmentRealTime:
    print '[Name - ' + reg.name + '] ', '[Description - ' + reg.description + ']'
    print client.read_input(reg.name)

print ''
print 'Controlador de carga - Tempo Real Status'
for reg in registersChargingEquipmentRealTimeStatus:
    statusList = reg.description.split(',')
    print '[Name - ' + reg.name + '] ', '[Description - ' + reg.description + ']'
    print 'Status - List'
    for status in  statusList:
        print status.strip()
    print ''

print ''
print 'Controlador de carga - Tempo Real Estatisticas'
for reg in registersChargingEquipmentRealTimeStatics:
    print '[Name - ' + reg.name + '] ', '[Description - ' + reg.description + ']'

#print 'Registers'
#for reg in registers:
    #print
    #print reg
    #value = client.read_input(reg.name)
    #print value
#    print 'Name ', reg.name
#    print 'Description', reg.description
    #if value.value is not None:
    #    print client.write_output(reg.name,value.value)

print ''
print 'Coils'
for reg in coils:
    #print
    #print reg
    value = client.read_input(reg.name)
    print value
    #print client.write_output(reg.name,value.value)

client.close()
