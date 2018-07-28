# start register of meter.
# This is not generic offset. This depends on meter used.
# I have used Elmeasure eNavigator meter.
READ_OFFSET = 100

# No of parameters to read.
READ_COUNT = 31

# Hostname/IP of Wiznet device 
WIZNET_HOST = "192.168.2.2"

# TCP Port no of Wiznet device 
WIZNET_PORT = 5000

# URL of telegraf where collected data will be posted. Telegraf is configured for HTTP based input plugin.
TELEGRAF_URL = "http://localhost:8186/write"

# List of parameter fetched from Meter. Sequence is dependent on Register mapping of meter.
PARAMETER_TYPE = {
"1",   "Watts Total",
"2",   "Watts R phase",
"3",   "Watts Y phase",
"4",   "Watts B phase",
"5",   "VAR Total",
"6",   "VAR R phase",
"7",   "VAR Y phase",
"8",   "VAR B phase",
"9",   "PF Ave.",
"10",  "PF R phase",
"11",  "PF Y phase",
"12",  "PF B phase",
"13",  "VA Total",
"14",  "VA R phase",
"15",  "VA Y phase",
"16",  "VA B phase",
"17",  "VLL average",
"18",  "Vry phase",
"19",  "Vyb phase",
"20",  "Vbr phase",
"21",  "VLN average",
"22",  "V R phase",
"23",  "V Y phase",
"24",  "V B phase",
"25",  "Current Total",
"26",  "Current R phase",
"27",  "Current Y phase",
"28",  "Current B phase",
"29",  "Frequency",
"30",  "Wh Received",
"31",  "VAh Received",
}
