import pwn

# Connect to the server
conn = pwn.remote('localhost', 4000)

# Read until it errors out
while True:
    try:
        # Read the line
        line = conn.recvline().decode().strip()
        # Print the line
        print(line)
        # Split the line into the two numbers
        nums = line.split(' ')
        # Convert the numbers to integers

        reverse = nums[1][::-1]
        print(reverse)
        conn.sendline(reverse)
        recv = conn.recvline()
        print(recv)

    except:
        # If we get an error, we are done

        break
