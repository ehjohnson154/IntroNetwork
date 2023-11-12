import sys
import json
import math  # If you want to use math.inf for infinity


def ipv4_to_value(ipv4_addr):
    """
    Convert a dots-and-numbers IP address to a single 32-bit numeric
    value of integer type. Returns an integer type.

    Example:

    ipv4_addr: "255.255.0.0"
    return:    4294901760  (Which is 0xffff0000 hex)

    ipv4_addr: "1.2.3.4"
    return:    16909060  (Which is 0x01020304 hex)
    """
    sip = ipv4_addr.split(".")
    part0 = int(sip[0])
    part1 = int(sip[1])
    part2 = int(sip[2])
    part3 = int(sip[3])
    num = (part0 << 24) | (part1 << 16) | (part2 << 8) | part3
	
    return num


def value_to_ipv4(addr):
    """
    Convert a single 32-bit numeric value of integer type to a
    dots-and-numbers IP address. Returns a string type.

    Example:

    There is only one input value, but it is shown here in 3 bases.

    addr:   0xffff0000 0b11111111111111110000000000000000 4294901760
    return: "255.255.0.0"

    addr:   0x01020304 0b00000001000000100000001100000100 16909060
    return: "1.2.3.4"
    """

    #convert addr to hex
    #8 bits?   hex = int(addr).to_bytes(8, "big")
    # = int(addr) #its already int but just to be safe

    pos1 = (addr >> 24) & 0xff
    pos2 = (addr >> 16) & 0xff
    pos3 = (addr >> 8) & 0xff
    pos4 = (addr >> 0) & 0xff

    ipv4 = f"{pos1}.{pos2}.{pos3}.{pos4}"
    #   print(hex(addr))
    return ipv4

def get_subnet_mask_value(slash):
    """
    Given a subnet mask in slash notation, return the value of the mask
    as a single number of integer type. The input can contain an IP
    address optionally, but that part should be discarded.

    Returns an integer type.

    Example:

    There is only one return value, but it is shown here in 3 bases.

    slash:  "/16"
    return: 0xffff0000 0b11111111111111110000000000000000 4294901760

    slash:  "10.20.30.40/23"
    return: 0xfffffe00 0b11111111111111111111111000000000 4294966784
    """

    #grab just the number
    entry = slash.split("/")
 
    count = int(entry[1])
    #print(count)
    #for /subnet_value, return a run of 1's equal to the slash value
    #see bitwise operation
    #what is this doing exactly?
    subnet_val = (1 << count) - 1
    shift = (subnet_val << 32 - count)
    #print(hex(shift))


    return shift

def ips_same_subnet(ip1, ip2, slash):
    """
    Given two dots-and-numbers IP addresses and a subnet mask in slash
    notataion, return true if the two IP addresses are on the same
    subnet.

    Returns a boolean.

    FOR FULL CREDIT: this must use your get_subnet_mask_value() and
    ipv4_to_value() functions. Don't do it with pure string
    manipulation.

    This needs to work with any subnet from /1 to /31

    Example:

    ip1:    "10.23.121.17"
    ip2:    "10.23.121.225"
    slash:  "/23"
    return: True
    
    ip1:    "10.23.230.22"
    ip2:    "10.24.121.225"
    slash:  "/16"
    return: False
    """

    subnet_mask = get_subnet_mask_value(slash)
    dec1 = ipv4_to_value(ip1)
    dec2 = ipv4_to_value(ip2)

    val1 = subnet_mask & dec1
    val2 = subnet_mask & dec2

    if val1 == val2:
        return True
    else:
        # print(subnet_mask)
        # print(val1, val2)
        return False



def get_network(ip_value, netmask):
    """
    Return the network portion of an address value as integer type.

    Example:

    ip_value: 0x01020304
    netmask:  0xffffff00
    return:   0x01020300
    """

    #bitwise and on IP and netmask?
    network = ip_value & netmask
    return network


def find_router_for_ip(routers, ip):
    """
    Search a dictionary of routers (keyed by router IP) to find which
    router belongs to the same subnet as the given IP.

    Return None if no routers is on the same subnet as the given IP.

    FOR FULL CREDIT: you must do this by calling your ips_same_subnet()
    function.

    Example:

    [Note there will be more data in the routers dictionary than is
    shown here--it can be ignored for this function.]

    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.3.5"
    return: "1.2.3.1"


    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.5.6"
    return: None
    """

    for x in routers:
        subnet = routers[x]["netmask"]

        if ips_same_subnet(x, ip, subnet) == True:
            return x
    
    return None


def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """

    #plan:

# dijkstra’s Algorithm to compute all shortest paths over a graph from a source point:

    src_router = find_router_for_ip(routers, src_ip) 
    dest_router = find_router_for_ip(routers, dest_ip) 


# Initialization:
#  Create an empty to_visit set. This is the set of all nodes we still need to visit.
    to_visit = set()
#  Create a distance dictionary. For any given node (as a key), it will hold the distance from that node to the starting node
    #??? Does this start empty ???#
    distance = {}
# Create a parent dictionary. For any given node (as a key), 
# it lists the key for the that leads back to the starting node (along the shortest path).
#         For every node:
#             Set its parent to None.
#             Set its distance to infinity. (Python has infinity in math.inf, but you could also use just a very large number, e.g. 4 billion.)
#             Add the node to the to_visit set.

#Are we going through the router dictionary and pointing to every router key inside the parent dictionary?
    parent = {}

    #assuming each one has its key
    for x in routers:
        #how to add x key in distance, parent, and to_visit?

        distance[x] = math.inf
        parent[x] = None
        to_visit.add(x)

    #set initial node:
    distance[src_router] = 0
    
    # print("TESTING INIT")
    # print(distance)
    # print(parent)
    # print(to_visit)
    # print ("END TESTING INIT")
    #iterate through keys to get routers
    #don't need to add connections



# Running:

#     While to_visit isn’t empty:
    while(len(to_visit) != 0):
#         Find the node in to_visit with the smallest distance. Call this the “current node”.
        current_node = find_current_node(to_visit, distance)

#         Remove the current node from the to_visit set.
        to_visit.remove(current_node)
#         For each one of the current node’s neighbors still in to_visit:
        neighbors = routers[current_node]["connections"]
        for x in neighbors:
#             Compute the distance from the starting node to the neighbor. 
            #grab weight of node, add to dist of current node
            #print(routers[current_node])
            weight = distance[current_node] + routers[current_node]["connections"][x]["ad"]
            

# This is the distance of the current node plus the edge weight to the neighbor.
            if weight < distance[x]:
                
                distance[x] = weight
                parent[x] = current_node
#             If the computed distance is less than the neighbor’s current value in distance:
#                 Set the neighbor’s value in distance to the computed distance.
#                 Set the neighbor’s parent to the current node.
#             [This process is called “relaxing”. The node distances start at infinity and “relax” down to their shortest distances.]

    path = get_shortest_path(parent, distance, src_router, src_ip, dest_router)
    #print(path)
    return(path)
    


def find_current_node(visit, dist):
    node = None
    curr = 1111111111
    for x in visit:
        if dist[x] < curr:
            node = x
    return node


def get_shortest_path(parent, distance, src_rout, src_node, dest_rout):
    cur = dest_rout
    path = []
    while cur != src_rout:
        path.append(cur)
        cur = parent[cur]
    if src_rout == dest_rout:
        return path
    if cur == src_rout:
        path.reverse()
        path.append(src_rout)


    path.reverse()
    return path

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
