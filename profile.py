# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node router1
node_router1 = request.RawPC('router1')
node_router1.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/router1.sh'))
iface8 = node_router1.addInterface(
    'interface-7', pg.IPv4Address('192.168.1.2', '255.255.255.0'))
iface9 = node_router1.addInterface(
    'interface-9', pg.IPv4Address('192.168.3.2', '255.255.255.0'))

# Node server
node_server = request.RawPC('server')
node_server.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/server.sh'))
iface6 = node_server.addInterface(
    'interface-10', pg.IPv4Address('192.168.3.1', '255.255.255.0'))
iface7 = node_server.addInterface(
    'interface-12', pg.IPv4Address('192.168.4.1', '255.255.255.0'))

# Node client1
node_client1 = request.RawPC('client1')
node_client1.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client.sh'))
iface0 = node_client1.addInterface(
    'interface-0', pg.IPv4Address('192.168.10.2', '255.255.255.0'))

# Node client2
node_client2 = request.RawPC('client2')
node_client2.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client.sh'))
iface1 = node_client2.addInterface(
    'interface-1', pg.IPv4Address('192.168.10.3', '255.255.255.0'))

# Node client3
node_client3 = request.RawPC('client3')
node_client3.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client.sh'))
iface2 = node_client3.addInterface(
    'interface-2', pg.IPv4Address('192.168.10.4', '255.255.255.0'))

# Node client4
node_client4 = request.RawPC('client4')
node_client4.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client.sh'))
iface3 = node_client4.addInterface(
    'interface-3', pg.IPv4Address('192.168.10.5', '255.255.255.0'))

# Link link-1 (Connect clients to router)
link_1 = request.Link('link-1')
link_1.addInterface(iface0)
link_1.addInterface(iface1)
link_1.addInterface(iface2)
link_1.addInterface(iface3)
link_1.addInterface(iface8)

# Link link-4 (Connect router to server)
link_4 = request.Link('link-4')
link_4.addInterface(iface9)
link_4.addInterface(iface6)

# Print the generated rspec
pc.printRequestRSpec(request)
