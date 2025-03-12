class SystemInfo:
    def __init__(self, data):
        self.system_name = data.get("system_name")
        self.version = data.get("version")
        self.description = data.get("description")
        self.device_count_total = data.get("device_count_total")
        self.battery_count = data.get("battery_count")
        self.wind_count = data.get("wind_count")
        self.solar_count = data.get("solar_count")
        self.grid_count = data.get("grid_count")
        self.vsc_count = data.get("vsc_count")
        self.bus_count = data.get("bus_count")
        self.load_count = data.get("load_count")
        self.wire_count = data.get("wire_count")
        self.x = data.get("x")
        self.y = data.get("y")

class Device:
    def __init__(self, data):
        self.d_id = data.get("d_id")
        self.d_type = data.get("d_type")
        self.d_name = data.get("d_name")
        self.d_dispname = data.get("d_dispname")
        self.x = int(data.get("x", 0))
        self.y = int(data.get("y", 0))
        self.parameters = data.get("parameters", {})

class Wire:
    def __init__(self, data):
        self.w_id = data.get("w_id")
        self.start_d = data.get("start_d")
        self.start_side = data.get("start_side")
        self.end_d = data.get("end_d")
        self.end_side = data.get("end_side")
        self.parameters = data.get("parameters", {})

class AC_DC_System:
    def __init__(self, json_data):
        self.system_info = SystemInfo(json_data.get("system_info"))
        self.devices = [Device(d) for d in json_data.get("devices", [])]
        self.wires = [Wire(w) for w in json_data.get("wires", [])]

    def get_devices_by_type(self, d_type):
        return [device for device in self.devices if device.d_type == d_type]

    def display_info(self):
        print(f"System: {self.system_info.system_name}, Version: {self.system_info.version}")
        print(f"Devices: {len(self.devices)}, Wires: {len(self.wires)}")
        for device in self.devices:
            print(f"{device.d_dispname} ({device.d_type}) at ({device.x}, {device.y})")
