"""
file: airit_simulation.py
description: This program simulates the rit airline system using data structures like stack, queue and linked node
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
        Ashwath Sreedhar Halemane, ah7387@rit.edu
"""

import sys

from cs_queue import Queue
from cs_stack import Stack


class Passenger:
    """
    Passenger class
    """
    __slots__ = 'name', 'ticket_number', 'carry_on'

    def __init__(self, name, tn, carry) -> None:
        self.name = name
        self.ticket_number = tn
        self.carry_on = carry

    def __repr__(self) -> str:
        return repr(self.name) + " " + repr(self.ticket_number) + " " + repr(self.carry_on)


class AirCraft:
    """
    Aircraft class
    """

    __slots__ = 'max_capacity', 'present_capacity', 'passengers'

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.present_capacity = 0
        self.passengers = [Stack(), Stack()]

    def embark(self, gate):
        if self.present_capacity >= self.max_capacity:
            return False

        for i in range(3, -1, -1):
            while not gate.boarding_q[i].is_empty() and self.present_capacity < self.max_capacity:
                print(gate.boarding_q[i].peek())
                gate.present_capacity -= 1
                self.present_capacity += 1

                if gate.present_capacity == 0:
                    gate.is_passengers_present = False
                passenger = gate.boarding_q[i].peek()
                gate.boarding_q[i].dequeue()
                if passenger.carry_on == 'True':
                    self.passengers[0].push(passenger)
                else:
                    self.passengers[1].push(passenger)

    def deplane(self):
        for passengers in self.passengers:
            while not passengers.is_empty():
                print(passengers.peek())
                passengers.pop()
        self.present_capacity = 0


class Gate:
    """
    Gate Class
    """

    __slots__ = 'boarding_q', 'maximum_capacity', 'present_capacity', 'is_passengers_present'

    def __init__(self, max_capacity):
        self.boarding_q = [Queue(), Queue(), Queue(), Queue()]
        self.maximum_capacity = max_capacity
        self.present_capacity = 0
        self.is_passengers_present = False

    def board(self, passenger):
        if self.present_capacity == self.maximum_capacity:
            return False

        self.is_passengers_present = True
        boarding_gate_no = int(passenger.ticket_number[0])
        self.boarding_q[boarding_gate_no - 1].enqueue(passenger)
        self.present_capacity += 1
        return True


def process_file(file_name: str):
    """
    Pushes all the strings into an array
    :param file_name: file name which has to be processed
    :return: returns array of strings
    """
    try:
        file_values = []
        with open(file_name) as f:
            for line in f:
                file_values.append(line.rstrip().split(","))

        return file_values
    except FileNotFoundError:
        print("Given file not found")


def board_passengers_recursively(all_passengers, boading_gate, air_craft, board_passengers):
    """
    function to board passengers
    :param all_passengers: all the passengers in stack data structure
    :param boading_gate: boarding gate Gate class
    :param air_craft: aircraft class
    :param board_passengers: flag to check if we can board passengers in the gate
    :return:
    """
    if all_passengers.is_empty():
        pass
    else:
        print("Passengers are lining up at the gate...")
        while board_passengers and not all_passengers.is_empty():
            print(all_passengers.peek())
            boading_gate.board(all_passengers.peek())
            if boading_gate.maximum_capacity == boading_gate.present_capacity:
                board_passengers = False
            all_passengers.pop()
        print("The gate is full; remaining passengers must wait.")
        print("Passengers are boarding the aircraft...")
        air_craft.embark(boading_gate)
        print('The aircraft is full.')
        print('Ready for taking off ...')
        print('The aircraft has landed.')
        print('Passengers are disembarking...')
        air_craft.deplane()
        board_passengers_recursively(all_passengers, boading_gate, air_craft, boading_gate.present_capacity == 0)


def run_simulation(gate_capacity, passenger_capacity, file_name):
    boading_gate = Gate(gate_capacity)
    air_craft = AirCraft(passenger_capacity)
    passengers = process_file(file_name)
    all_passengers = Stack()
    for passenger in passengers:
        all_passengers.push(Passenger(passenger[0], passenger[1], passenger[2]))

    board_passengers_recursively(all_passengers, boading_gate, air_craft, True)


def simulation():
    if len(sys.argv) > 2:
        print("Please pass correct arguments")
    else:
        file_name = sys.argv[1]

        while True:
            try:
                gate_capacity = input("Gate capacity:")
                gate_capacity = int(gate_capacity)
                break
            except ValueError:
                print("Value must be an integer. You entered: " + str(type(gate_capacity)))

        while True:
            try:
                passenger_capacity = input("Aircraft capacity:")
                passenger_capacity = int(passenger_capacity)
                break
            except ValueError:
                print("Value must be an integer. You entered: " + str(type(passenger_capacity)))

        run_simulation(gate_capacity, passenger_capacity, file_name)


if __name__ == "__main__":
    simulation()
