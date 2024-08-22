def hexdump():
    file_path = 'path/to/file' #edit here
    output_path = 'hex.txt' #can edit filename 

    try: # open file in binary mode and output in write mode
        with open(file_path, 'rb') as file, open(output_path, 'w') as output_file:
            offset = 0 #initialise byte offset (position in file) to zero
            chunk = file.read(16)  #chunk is first 16 bytes
            #keep looping until no more data found
            while chunk: 
                #each byte in chunk is converted to hexadecimal representation
                hex_part = ' '.join(f'{byte:02x}' for byte in chunk)
                # ascii column 
                ascii_part = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk) # '.' means non printable
                output_file.write(f'{offset:08x}  {hex_part:<47}  {ascii_part}\n') # combine parts
                offset += len(chunk)
                chunk = file.read(16) 
                #read each chunk to the file
        print(f"Hexdump written to {output_path}")
    except IOError as e:
        print(f"Error reading file: {e}")

# function call
hexdump()