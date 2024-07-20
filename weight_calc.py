#!/usr/bin/python3

import argparse

class Weight:
    def __init__(self, current_weight):
        self.current_weight = current_weight
    
    def gaining(self, gain_amount, gain_duration): 
        initial_weight = self.current_weight
        for week in range(0, gain_duration):
            self.current_weight += (self.current_weight / 100) * gain_amount
            print(f"Weight after gaining on week {int(week)+1} = {self.current_weight:.2f}")
        
        print(f"Total amount gained: {(self.current_weight-initial_weight):.2f}")
        return self.current_weight
    
    def losing(self, lose_amount, lose_duration):
        initial_weight = self.current_weight
        for week in range(0, lose_duration):
            self.current_weight -= (self.current_weight / 100) * lose_amount
            print(f"Weight after losing on week {int(week)+1} = {self.current_weight:.2f}")
        
        print(f"Total amount lost: {(self.current_weight-initial_weight):.2f}")
        return self.current_weight
    
    def cycle(self, gain_amount, lose_amount, gain_duration, lose_duration, cycles, which_first):
        for cycle in range(0, cycles):
            print(f"*****Start of cycle {cycle+1}*****")    
            if (gain_amount and gain_duration) and which_first == "gain":
                self.gaining(gain_amount, gain_duration)
                if lose_amount or lose_duration:
                    self.losing(lose_amount, lose_duration)
            elif (lose_amount and lose_duration) and which_first == "lose":
                self.losing(lose_amount, lose_duration)
                if gain_amount or gain_duration:
                    self.gaining(gain_amount, gain_duration)
        
        return self.current_weight
            
    

parser = argparse.ArgumentParser()

parser.add_argument("-cw", "--current-weight", help="Current weight in pounds", required=True, type=float)
parser.add_argument("-ga", "--gain-amount", help="Gaining percentage", type=float)
parser.add_argument("-la", "--lose-amount", help="Losing percentage", type=float)
parser.add_argument("-gd", "--gain-duration", help="Gaining duration", type=int)
parser.add_argument("-ld", "--lose-duration", help="Losing duration", type=int)
parser.add_argument("-c", "--cycles", help="How many gain/loss cycles to run", default=1, type=int)
parser.add_argument("-wf", "--which-first", help="Which to do first, gain or lose", 
                    default="gain", choices=["gain", "lose"])

args = parser.parse_args()

w = Weight(current_weight=args.current_weight)
print(f"\nOutcome:\nStarting Weight: {w.current_weight}\nFinishing Weight: {w.cycle(args.gain_amount, args.lose_amount, args.gain_duration, 
                          args.lose_duration, args.cycles, args.which_first):.2f}")
