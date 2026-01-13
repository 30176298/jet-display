def test_fuel():
  remaining_fuel = calculate_fuel_remaining(initial_fuel_kg = 1000,
                                            burn_rate_kg_per_min = 10,
                                            time_min = 50)
  #Expecting 1000 - (10 * 50) -> 500 kg of fuel remaining
  #Format is like this -> assert {expectation}, {message if expectation is false}
  assert remaining_fuel == 500, f"Expected 500 kg, got {remaining_fuel:.2f} kg"

def test_stall_warning():
  warnings = check_warnings(altitude = 10_000,
                            speed_knots = 100,
                            fuel_kg = 2000)
  assert "STALL" in warnings, f"Expected STALL warning at 100 kt, got {warnings}"

def run_self_tests() -> None:
  test_fuel()
  test_stall_warning()
