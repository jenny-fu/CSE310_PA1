Jenny Fu
JENFU
112203722

Assuming you are in the correct directory:
To run the server, simply open the terminal and run the "webserver.py" file.
You are able to see the IP address of the host and the port number it is listening to (12000). With this information, you can connect to a browser using the following format:

	http://[IP_address]:[port_number]/[filename]

To run the client, open up another terminal and run "client.py" using the following format:

	client.py [IP_address] [server_port] [filename]

If the format is wrong or if the server is unable to connect, you will get an error message.
The filename should be inputted without the forward slash.