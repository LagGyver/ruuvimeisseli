from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

counter = 10
# RunFlag for stopping execution at desired time
run_flag = RunFlag()

def handle_data(found_data):
    print(f'MAC {found_data[0]}')
    print(f'Data {found_data[1]}')

    global counter
    counter = counter - 1
    if counter < 0:
        run_flag.running = False

# List of macs of sensors which will execute callback function
macs = ['F3:EF:D2:E0:39:CB', 'DC:B2:16:42:AC:47']

RuuviTagSensor.get_datas(handle_data, macs, run_flag)