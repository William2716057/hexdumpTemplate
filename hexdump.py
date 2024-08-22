def hexdump():
    file_path = 'output.bmp'
    output_path = 'hex.txt'

    try: # open file in binary mode and output in write mode
        with open(file_path, 'rb') as file, open(output_path, 'w') as output_file:
            offset = 0 #initialise byte offset (position in file) to zero
            chunk = file.read(16)  
            while chunk: 
                hex_part = ' '.join(f'{byte:02x}' for byte in chunk)
                ascii_part = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk)
                output_file.write(f'{offset:08x}  {hex_part:<47}  {ascii_part}\n')
                offset += len(chunk)
                chunk = file.read(16) 
        print(f"Hexdump written to {output_path}")
    except IOError as e:
        print(f"Error reading file: {e}")

# function call
hexdump()