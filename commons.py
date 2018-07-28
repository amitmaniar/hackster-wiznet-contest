import crc16

def u16_to_bestr( u):
    """Given word, return as big-endian binary string"""
    u = (int(u) & 0xFFFF)
    return( chr(u>>8) + chr(u&0xFF) )

def bestr_to_u16( st, start=0):
    """Given big-endian binary string, return bytes[0-1] as int"""
    return( (ord(st[start])<<8) + ord(st[start+1]))

# Generate Modbus RTU request from slave_id, function code, register offset and no of registers.
def mb_rtu_make_request( slave_id, func_code, read_offset, read_count ):

    command = None

    if((slave_id < 0) or (slave_id >255)):
        raise "Bad Slave Address"

    if(func_code in [1,2,3,4]):
        command = chr(slave_id) + chr(func_code) + u16_to_bestr(read_offset) + u16_to_bestr(read_count)
    else:
       raise "Wrong Function code"

    # Calculate CRC16 for given command
    crc = crc16.calc_string( command, 0xFFFF)
    # We need to add the CRC as LittleEndian
    command += chr(crc&0xFF) + chr(crc>>8)
    return command
