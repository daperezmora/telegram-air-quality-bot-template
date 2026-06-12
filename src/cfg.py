import yaml

def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

class Cfg:
    def __init__(self, sensors_path: str = "cfg/sensors.yaml"):
        self.raw = load_yaml(sensors_path)
        self.sensors = self.raw.get("sensors", {})     # {9: "pm25", ...}
        self.labels = self.raw.get("labels", {})       # {"pm25": "PM2.5", ...}
        self.units = self.raw.get("units", {})         # {"pm25": "µg/m³", ...}

    def alias(self, sensor_id: int) -> str:
        return self.sensors.get(sensor_id) or self.sensors.get(str(sensor_id)) or str(sensor_id)

    def label(self, sensor_id: int) -> str:
        a = self.alias(sensor_id)
        return self.labels.get(a, f"Sensor {sensor_id}")

    def unit(self, sensor_id: int) -> str:
        a = self.alias(sensor_id)
        return self.units.get(a, "")
