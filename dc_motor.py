#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi as pi
import sys

class DC_Motor_DRV8835:
    '''
    MODE:IN/IN１を想定
    '''

    def __init__(self, a_phase, a_enbl):
        pi.wiringPiSetupGpio()
        self.a_phase = a_phase
        self.a_enbl = a_enbl

        pi.pinMode(self.a_phase, pi.OUTPUT)
        pi.pinMode(self.a_enbl, pi.OUTPUT)

    def start(self):
        pi.digitalWrite(self.a_phase, 1)
        pi.digitalWrite(self.a_enbl, 1)

    def stop(self):
        pi.digitalWrite(self.a_phase, 0)
        pi.digitalWrite(self.a_enbl, 0)


if __name__ == '__main__':

    if sys.argv[1] in {"stop"}:
        dcmotor = DC_Motor_DRV8835(a_phase=14, a_enbl=15)
        dcmotor.stop()
    elif sys.argv[1] in {"start"}:
        dcmotor = DC_Motor_DRV8835(a_phase=14, a_enbl=15)
        dcmotor.start()
    else:
        print("Need Argument:start or stop")