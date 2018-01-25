import time
import Parameters
from Plotting import Graph
from scapy.all import *


class Effect:
    """Class that generally defines what an effect should contain """

    def __init__(self,
                 accept_packets=True,
                 show_output=True,
                 graphing=False,
                 graph_type_num=0):

        self.accept_packet = accept_packets
        self.show_output = show_output
        self.graphing = graphing
        self.graph_type_num = graph_type_num

        if self.graphing:

            self.graph = Graph()
            self.default_graphing_setup()

            if show_output:
                description = self.check_for_graph_type()
                print("""[*] Graph number is \'{}\' and the description is: \n[*]\t\"{}\"""".
                      format(self.graph_type_num, description))

        # --- Universal stats --- #
        # Every effect has a starting time
        self.start_time = time.time()
        self.total_packets = 0  # Number of total packets processed

        self.tcp_flags = []

    def effect(self, packet):
        """The first method run for all effects - Here custom code will be added
        to collate information"""

        # TCP tracking
        self.track_TCP_stats(packet)

        # Shared functionality between all effects
        self.print_stats()
        self.total_packets += 1
        self.default_graphing(packet)
        self.custom_effect(packet)

    def custom_effect(self, packet):
        """Each effect will need it's own custom effect"""
        raise Exception('NotImplemented: Please add \'custom_effect()\' to your class')

    def print_stats(self):
        """[Blueprint] - Should print the custom stats for each method.
        Note Print_stats should call 'self.print()' to show any output """
        pass

    def check_for_graph_type(self):
        """This method checks for the graph number provided is valid"""
        class_name = self.__class__.__name__

        for x in Parameters.graph_descriptions:
            graph = x

            if graph.effect_name is class_name or graph.effect_name is None:
                if graph.number is self.graph_type_num:
                    return graph.description

        # If a graph cannot be found
        print('\n[ERROR] Invalid graph number provided\n')
        exit(0)

    def get_elapsed_time(self):
        """Used to find out how long ago the effect started"""
        return time.time() - self.start_time

    def print(self, message, end='\n', force=False):
        """General print method"""
        if self.show_output or force:
            print(message, end=end, flush=True)

    @staticmethod
    def print_clear():
        """Method that is used to clear the output line, this is
        so no fragments are left after a stat print refresh"""
        print(' ' * 70, end='\r', flush=True)

    def accept(self, packet):
        """Center point for accepting packets"""
        self.total_packets += 1

        if self.accept_packet:
            packet.accept()

    def default_graphing(self, packet):
        """The main functionality for all the effects, where graphing is available"""

        if self.graphing:
            # Graph that tracks types of packets in the session
            if self.graph_type_num is 0:
                sections = str(packet).split(' ')
                self.graph.increment_catagory(sections[0])

            # Graph that processes total number of packets over time
            elif self.graph_type_num is 10:
                self.graph.add_points(self.get_elapsed_time(), self.total_packets)

            # Each effects custom graphing
            else:
                self.graphing_effect(packet)

    def default_graphing_setup(self):
        """Used to init all axis and other variables required"""

        if self.graphing:
            # Graph that tracks types of packets in the session
            if self.graph_type_num is 0:
                self.graph.set_y_axis_label('Number of packets')

            # Graph that processes total number of packets over time
            elif self.graph_type_num is 10:
                self.graph.set_x_axis_label('Time (s)')
                self.graph.set_y_axis_label('Total Packets')
            else:
                self.graphing_setup()

    def show_default_graphs(self):
        # Graph that tracks types of packets in the session
        if self.graph_type_num is 0:
            self.graph.bar()

        # Graph that processes total number of packets over time
        elif self.graph_type_num is 10:
            self.graph.plot('g,-')

        else:
            self.show_custom_graph()

    def show_graph(self):
        """Called to display any type of graph"""
        self.show_default_graphs()

    def save_graph(self):
        """Will just save the graph to file"""
        self.graph.save()

    def graphing_setup(self):
        """[Blueprint] - Custom code for each effects graph setup"""
        pass

    def graphing_effect(self, packet):
        """[Blueprint] - Function that contains custom graph effects"""
        pass

    def show_custom_graph(self):
        """[Blueprint] - Each effect will change the behavior of this method to add it's own affects"""
        pass

    def stop(self):
        """[Blueprint] - Called to stop the object"""
        pass

    # Variance
    def increase_effect(self):
        """[Blueprint] - Used to make the degradation higher """
        pass

    def decrease_effect(self):
        """[Blueprint] - Used to make the degradation lower"""
        pass

    def check_packet_type(self, packet, target_packet):
        """Checks if the packet is of a certain type"""

        # Grabs the first section of the Packet
        packet_string = str(packet)
        split = packet_string.split(' ')

        # Checks for the target packet type
        if target_packet == split[0]:
            return True
        else:
            return False

    # Stats
    def track_TCP_stats(self, packet):
        """Method that tracks characteristics of the TCP packets """

        try:
            FIN = 0x01
            SYN = 0x02
            RST = 0x04
            PSH = 0x08
            ACK = 0x10
            URG = 0x20
            ECE = 0x40
            CWR = 0x80

            if self.check_packet_type(packet, 'TCP'):
                pkt = IP()/TCP(packet.get_payload())
                flags = pkt['TCP'].flags

                # Saves the flags
                active_flags = ['***'] * 8
                if flags & FIN:
                    active_flags[0] = 'FIN'
                if flags & SYN:
                    active_flags[1] = 'SYN'
                if flags & RST:
                    active_flags[2] = 'RST'
                if flags & PSH:
                    active_flags[3] = 'PSH'
                if flags & ACK:
                    active_flags[4] = 'ACK'
                if flags & URG:
                    active_flags[5] = 'URG'
                if flags & ECE:
                    active_flags[6] = 'ECE'
                if flags & CWR:
                    active_flags[7] = 'CWR'

                # Saves the TCP flags
                self.tcp_flags.append(active_flags)
        except Exception as e:
            print(e)
