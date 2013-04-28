# Find Prime IP Addresses #

## About ##

A simple Python script by Jonathan Ellenberger that finds prime IP addresses.

## Arguments ##

### Required Arguments ###

* `ip_range_start`: The start of the IP range to check for primes.
* `ip_range_end`: The end of the IP range to check for primes

### Optional Arguments ###
 
* `--slice-start`/`-s`: The start of the 'slice range' to calculate prime IPs from the overall IP range that was originally created `slice_start` and `slice_end`.
* `--slice-end`/`-e`: The end of the 'slice range' to calculate prime IPs from the overall IP range that was originally created `slice_start` and `slice_end`.

## Example Usage ##

To find prime IP addresses within a particular range of IPs, just past a start and end IP address:

```bash
$ python find_ip_address_primes.py 10.0.0.0 10.0.1.255
==================================================
Prime IP Addresses Between 10.0.0.0 and 10.0.1.255
==================================================
10.0.0.7
10.0.0.9
10.0.0.19
10.0.0.43
10.0.0.49
10.0.0.57
10.0.0.69
10.0.0.117
10.0.0.121
10.0.0.133
10.0.0.151
10.0.0.159
10.0.0.171
10.0.0.183
10.0.0.187
10.0.0.193
10.0.0.199
10.0.0.211
10.0.0.213
10.0.0.231
10.0.0.249
10.0.0.253
10.0.1.29
10.0.1.51
10.0.1.53
10.0.1.69
10.0.1.83
10.0.1.89
10.0.1.93
10.0.1.107
10.0.1.123
10.0.1.153
10.0.1.159
10.0.1.173
10.0.1.177
10.0.1.191
10.0.1.197
10.0.1.219
10.0.1.237
```

### Slicing the IP Range ###

Unless you've got a super computer, large IP ranges will take a _LOOONG_ time to calculate. In order to get a smaller slice from a large IP range you can pass the two optional arguments `--slice-start` and `--slice-end` to only calculate primes within a 'window' of the overall range:

```bash
$ python find_ip_address_primes.py 10.0.0.0 10.255.255.255 --slice-start=500 --slice-end=600
===================================================
Prime IP Addresses Between 10.0.1.244 and 10.0.2.88
---------------------------------------------------
(A Slice From IP Range: 10.0.0.0 - 10.255.255.255)
===================================================
10.0.0.25
10.0.0.49
10.0.0.79
10.0.0.83
10.0.0.91
```