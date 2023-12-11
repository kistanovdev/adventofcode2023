

def read_map_file(file_name):
  lines = []
  with open(file_name) as f:
    for line in f.readlines():
      lines.append([int(x) for x in line.strip().split()])

  return lines

def convert(conversion_map, value) -> int:

  for dest_range_start, source_range_start, range_length in conversion_map:

    source_range_end = source_range_start + range_length - 1

    if value >= source_range_start and value <= source_range_end:
      diff = value - source_range_start
      print(f'found bounds. value {value} is between values {source_range_start} and {source_range_end}')
      return dest_range_start + diff

  print('did not find bounds')
  return value
  

def main():

  seeds = [int(x) for x  in "".join([line.strip() for line in open("input.txt")]).split()]
  toy_map = read_map_file('toy-map.txt')
  seed_to_soil_map = read_map_file('seed-to-soil.txt')
  soil_to_fertilizer_map = read_map_file('soil-to-fertilizer.txt')
  fertilizer_to_water = read_map_file('fertilizer-to-water.txt')
  water_to_light = read_map_file('water-to-light.txt')
  light_to_temperature_map = read_map_file('light-to-temperature.txt')
  temperature_to_humidity_map = read_map_file('temperature-to-humidity.txt')
  humidity_to_location_map = read_map_file('humidity-to-location.txt')

  results = []
  for seed in seeds:
    soil = convert(seed_to_soil_map, seed)
    fertilizer = convert(soil_to_fertilizer_map, soil)
    water = convert(fertilizer_to_water, fertilizer)
    light = convert(water_to_light, water)
    temperature = convert(light_to_temperature_map, light)
    humidity = convert(temperature_to_humidity_map, temperature)
    location = convert(humidity_to_location_map, humidity)
    results.append(location)

  assert min(results) == 322500873


if __name__=="__main__":
  main()