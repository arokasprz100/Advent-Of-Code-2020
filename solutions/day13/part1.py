from solutions.common.file_reader import FileReader

if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    timestamp = int(puzzle_input[0])
    buses = [int(x) for x in puzzle_input[1].split(',') if x != 'x']
    departure_timestamps = [timestamp if timestamp % bus == 0 else bus * (timestamp // bus + 1) for bus in buses]
    buses_and_waiting_times = list(zip(buses, [departure - timestamp for departure in departure_timestamps]))
    earliest_bus = min(buses_and_waiting_times, key=lambda x: x[1])
    print("Solution: {}".format(earliest_bus[0] * earliest_bus[1]))
