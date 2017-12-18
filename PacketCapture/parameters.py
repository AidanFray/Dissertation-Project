"""Changes made here will effect the parameters taken for each effect"""

cmd_latency = '-l'
cmd_packetloss = '-pl'
cmd_target_packet = '-tp'
cmd_print = '-p'
cmd_bandwidth = '-b'
cmd_throttle = '-t'
cmd_duplicate = '-d'
cmd_simulate = '-s'
cmd_ratelimit = '-rl'
cmd_combination = '-c'
cmd_outoforder = '-o'
cmd_arp = '-a'


def Usage():
    return"""
Effects:
--print, -p                                  
    * Prints all the packets
    
--display-bandwidth, -b                     
    * Displays information on the transfer rate
      
--latency, -l <delay_ms>            
    * Applies latency on the connection   
    
--packet-loss, -pl  <loss_percentage>  
    * Performs packet loss on the connection

--throttle, -t      <delay_ms> 
    * Throttles the connection by the given delay 
    
--duplicate, -d     <factor>                 
    * Duplicates a packet by the specified factor

--simulate, -s      <connection_name>        
    * Simulates real world connections e.g. 3G
    
--rate-limit, -rl   <rate_bytes>            
    * Limits the throughput of the program
                                
--combination, -c   <latency_ms> <packet-loss> <bandwidth_bytes>
    * Performs latency and packet loss at the same time
    
--out-of-order, -o 
    * Sets the mode to out of order that alters the order of incoming packets
                                
Extra Optionals:

--target-packet, -tp    <packet-type>        
    * Only performs an affect on the specified packet type

--arp, -a               <victimIP> <routerIP> <interface>       
    * Performs arp spoofing with the passed parameters
    """

