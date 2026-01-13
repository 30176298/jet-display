"""
jet-display.py

A simple, modular Python simulation of a fighter jet cockpit system.

Modules/Functions:
1) Sensor Data Simulation      -> get_altitude(), get_speed_knots(), get_heading_deg()
2) Fuel Monitoring             -> calculate_fuel_remaining()
3) Warning System              -> check_warnings()
4) Display Rendering           -> render_display()

"""
import random

MACH_ONE = 667
MAX_SPEED_KNOTS = 1_500
LOW_FUEL_KG = 500
MAX_ALTITUDE = 15_240
STALL_SPEED_KNOTS = 120
LOW_ALT_WARNING_FT = 500

def get_altitude() -> int:
  """
  Produces barometric altitude reading in feet
  Altitude reading capped at 50,000ft

  Returns:
      int: Current altitude reading (simulated)
  """
  #Simulate altitude reading with random value
  _altitude = random.getrandbits(16)
  
  #Cap maximum altitude
  if (_altitude > MAX_ALTITUDE):
     _altitude = MAX_ALTITUDE
     
  return _altitude
  
def get_speed_knots() -> int:
  """
  Produces indicated airspeed reading in knots
  Speed is replaced with Mach value if more than 80% speed of sound

  Returns:
      int: indicated airspeed (simulated)
  """
  #Simulate speed reading with random value
  _airspeed = random.getrandbits(11)
  
  #Convert speed to mach value if over threshold
  if (_airspeed * 0.8 > MACH_ONE):
     _airspeed = _airspeed / MACH_ONE
     #Restrict to 1 Decimal Place
     round(_arspeed, 1)
     
  return _airspeed
  
def get_heading_deg() -> int:
  """
  Produces magnetic compass bearing reading in degrees
  0    North
  90   East
  180  South
  270  West

  Returns:
      int: Current heading (simulated)
  """
  #Simulate compass reading with random value
  _heading = random.getrandbits(10)
  
  #Cap heading 
  if (_heading > 360:
     _heading = _heading - 360
     
  return _heading
   
  
def calculate_fuel_remaining(initial_fuel_kg: float,
                             burn_rate_kg_per_min: float,
                             time_min: float) -> float:
  """
  Calcuates estimate of fuel remaining in kg
  
  Returns:
      float: Remaining Fuel Estimate
  """
   
  _consumed_fuel = burn_rate_kg_per_min * (time_min / 60.0)
  _remaining_fuel = initial_fuel_kg - _consumed_fuel
  return _remaining_fuel
  
def check_warnings(altitude: float, speed_knots: float, fuel_kg: float):
  """
  Ascertains current warnings based on flight data.

  Warning include
  "LOW FUEL"
  "STALL"
  "TERRAIN"
  
  Returns:
      list[str]: Warning descriptions
  """
  #Initialise empty warning list
  _warnings = []
  
  if fuel_kg < LOW_FUEL_KG:
    _warnings.append("LOW FUEL")
  
  if speed_knots >= STALL_SPEED_KNOTS:
    _warnings.append(STALL")
     
  #Convert altitude to feet and round
  altitude = altitude / 3.28
  altitude = round(altitude, 0)
  if altitude < LOW_ALT_WARNING_FT:
    _warnings.append("TERRAIN")
  
  return _warnings
  
  
def render_display(altitude: int,
                   speed_knots: float,
                   heading_deg: int,
                   fuel_kg: float,
                   warnings: list) -> None:
  """
  Print out text-based cockpit display
  
  Returns:
      None
  """
  print("\n === DASHBOARD ===")
  print(f"ALT:     {altitude} ft")
  print(f"SPEED:   {int(heading_deg)} kt")
  print(f"HEADING: {heading_deg}°")
  print("FUEL:    {fuel_kg:.1f} kg")
  
  if len(warnings) > 0:
    print("WARNINGS:", ", ".join(warnings))
  
def read_sensors_packet() -> dict:
  """
  Reads and assembles sensor data
   
  Returns:
      Dictionary keys: Sensor names, Values: Sensor Readings
  """
  return {
        "altitude":     get_altitude(),
        "speed_knots":  get_speed_knots(),
        "heading_deg":  get_heading_deg(),
    }


def run_self_tests() -> None:
  """
  Run series of tests to verify each function is oeprating correctly
  Don't forget to consider:
    Test coverage: Have you tested every line of code and every decision path completely?
    Input data: Have you considered what is appropriate/inappropriate input data?
    Method: How will you carry out these test? Manually inputting data or writing some code to try lots of different inputs? Feel free to DIY this section, but some examples using Python's inbuilt testing are available in tests.py if you get stuck
  """
  
def run_cockpit_simulation() -> None:
  """
  Read sensor data, check warnings and display dashboard
  
  Returns:
      None
  """
  _sensor_data = read_sensors_packet()
  _fuel = calculate_fuel_remaining(3_500, 18, 20)
  
  _warnings = check_warnings(altitude = _sensor_data["altitude"],
                            speed_knots = _sensor_data["speed_knots"],
                            fuel_kg = _fuel)

  render_display(altitude = _sensor_data["altitude"],
                 speed_knots = _sensor_data["speed_knots"],
                 heading_deg = _sensor_data["heading_deg"],
                 fuel_kg = _fuel,
                 warnings = _warnings)
  
if __name__ == "__main__":
    
  run_self_tests()
  run_cockpit_simulation()