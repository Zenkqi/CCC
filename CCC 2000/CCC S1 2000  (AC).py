# CCC '00 S1 - Slot Machines
import sys
input = sys.stdin.readline

quarters = int(input())

first = int(input())
second = int(input())
third = int(input())

counter = 0

while quarters > 0:
    quarters -= 1
    counter += 1
    first += 1
    if first % 35 == 0:
        quarters += 30
    elif quarters <= 0: break

    quarters -= 1
    counter += 1
    second += 1
    if second % 100 == 0:
        quarters += 60
    elif quarters <= 0: break

    quarters -= 1
    counter += 1
    third += 1
    if third % 10 == 0:
        quarters += 9
    elif quarters <= 0: break

print("Martha plays", counter,"times before going broke.")
