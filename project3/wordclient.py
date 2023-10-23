import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    global packet_buffer
        
    while True:
        #checking to make sure we have a valid word packet
        if len(packet_buffer) >= 2: 
            encoded_word_length = packet_buffer[:2] 
            packet_length =  int.from_bytes(encoded_word_length, "big") + 2 #decode passed packet length

            #check to ensure there is a full word packet in there
            if len(packet_buffer) >= (packet_length):
                word_packet = packet_buffer[:packet_length]#extract the packet data
                packet_buffer = packet_buffer[packet_length:]# strip the packet data off the front of the buffer
                return word_packet
        
        d = s.recv(20) 
        packet_buffer += d

        if d == b'': #close connection if no more data is being streamed
            return None
        else: #len(packet_buffer) <= 2:
            continue

    

#passed in a word packet containing the length and the letters.
def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """
    cutpacket = word_packet[2:] #cut out the length part of packet
    decodedword = cutpacket.decode() #decode word into string
    return decodedword


# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
