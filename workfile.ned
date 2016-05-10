simple Source
{
	gates:
		output out;
		input in;
}
network Reseau
{
	submodules : 
		Router1 : Source {}
		Router3 : Source {}
		Router2 : Source {}
	connections :
		Router1.out --> {datarate = 100000kbps; delay = 50ms;} --> Router2.in;
		Router3.out --> {datarate = 100000kbps; delay = 50ms;} --> Router1.in;
		Router2.out --> {datarate = 10000kbps; delay = 100ms;} --> Router3.in;
}