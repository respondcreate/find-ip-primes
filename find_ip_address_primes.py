import argparse, itertools

def is_prime(num):
    """
    Returns 'True' if passed integer `num` is prime, 'False' if it isn't.
    Found here: http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python/4117879#4117879
    """
    return all(num % x for x in xrange(2, num))

def construct_ip_address_range(start='10.0.0.0', end='10.255.255.255'):
    """
    Returns a list of IP (as strings).
    Takes two strings (`start` and `end`) that are formatted like an IP address
    (i.e. 'int.int.int.int') that represent a range of IP addresses
    """
    ip_start_split = start.split('.')
    ip_end_split = end.split('.')

    # Ensure IP addresses pair together (i.e. they have the same number of 'segments' once split)
    if len(ip_start_split) != len(ip_end_split):
        raise Exception('The IP addresses passed to `start` (%s) and end (%s) represent an invalid IP range.' % (start, end))
    else:
        # Now, ensure IP address segments are ready for processing
        # i.e. the string passed to `start` is lower in the IP range
        # than the string passed to `end`
        for counter, ip_segment in enumerate(ip_start_split):
            if int(ip_segment) > int(ip_end_split[counter]):
                raise Exception('A segment (%s) passed to `start` (%s) is higher than its corresponding segment (%s) passed to `end` (%s)' % (ip_segment, start, ip_end_split[counter], end))

        return [
            # Here's where the magic happens.
            # `segments` is a tuple of ip address segments as created by itertools.product()
            '.'.join([str(segment) for segment in segments])
            # itertools.product() produces a cartesian product of iterables passed to it
            # More info here: http://docs.python.org/2/library/itertools.html#itertools.product
            for segments in itertools.product(*[
                # Here's the list of iterables we're passing to itertools.product()
                # It is constructed by creating a list (via `range()`) of all numbers
                # between the corresponding segments in `start` and `end`
                range(int(ip_segment), int(ip_end_split[counter])+1)
                for counter, ip_segment in enumerate(ip_start_split)
            ])
        ]

def find_primes_in_ip_range(list_of_ip_strings, start, end):
    """
    Returns a list of prime IP addresses from a list of IP addresses (`list_of_ip_strings`).
    `start` and `end` provide slicing capability since prime calculation is processor intensive
    """
    try:
        x = list_of_ip_strings[end]
    except (IndexError, TypeError):
        end = len(list_of_ip_strings)-1

    index_of_primes = [
        # This list will be comprised of indexes for where a prime IP appears in
        # in the list passed to `list_of_ip_strings`
        counter 
        # Iterate over the counter (provided by enumerate)
        # `start` and `end` allow slicing the list since prime calculation
        # for a large set of numbers can take quite a long time (or a lot of horsepower) to process
        for counter, ip_as_string in enumerate(list_of_ip_strings[start:end])
        if is_prime(int(ip_as_string.replace('.', '')))
    ]
    return [
        string
        for index, string in enumerate(list_of_ip_strings)
        if index in index_of_primes
    ]

############ Command Line Scripting Support ############
# Define the arguments that can be passed to this script from the command line
parser = argparse.ArgumentParser(description='Find primes in a range of IP addresses.')
parser.add_argument(
    'ip_range_start',
    type=str,
    help='The start of the IP range'
)
parser.add_argument(
    'ip_range_end',
    type=str,
    help='The end of the IP range'
)
parser.add_argument(
    '-s',
    '--slice-start',
    type=int,
    default=0,
    help='The point in the IP range list where prime processing should start.'
)
parser.add_argument(
    '-e',
    '--slice-end',
    type=int,
    default=None,
    help='The point in the IP range list where prime processing should end.'
)

# Process any arguments passed by the user from the command line
args = parser.parse_args()

# Figure out what range of IP addresses needs to be processed
ip_range = construct_ip_address_range(args.ip_range_start, args.ip_range_end)

# Ensure the values passed to `slice_start` and `slice_end` are valid
# indexes in the `ip_range` list.
try:
    slice_start = ip_range[args.slice_start]
except (IndexError, TypeError):
    slice_start = 0
else:
    slice_start = args.slice_start

try:
    slice_end = ip_range[args.slice_end]
except (IndexError, TypeError):
    slice_end = -1
else:
    slice_end = args.slice_end

# Construct the output title
output_title = "Prime IP Addresses Between %s and %s" % (ip_range[slice_start], ip_range[slice_end])

# Build a horizontal rule that's the same length as the output title
horizontal_rule = "="*len(output_title)

# Print out the title and rule
print horizontal_rule
print output_title
# Ascertain whether or not the slice range of IP addresses is different than the IP
# addresses originally passed to `args.ip_range_start` and `args.ip_range_end`
if (ip_range[slice_start] != args.ip_range_start) or (ip_range[slice_end] != args.ip_range_end):
    # If they are, print an appropriate 'sub title' since the output range is different
    # Than the values passed to `args.ip_range_start` and `args.ip_range_end`
    print '-'*len(output_title)
    print "(A Slice From IP Range: %s - %s)" % (args.ip_range_start, args.ip_range_end)
print horizontal_rule
# Finally, print out the range of prime IPs
for ip in find_primes_in_ip_range(
        ip_range,
        args.slice_start,
        args.slice_end
    ):
    print ip