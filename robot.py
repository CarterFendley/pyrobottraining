#!/usr/bin/env python

import wpilib

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        self.motor1 = wpilib.Talon(1)
        self.motor2 = wpilib.Talon(2)
        self.motor3 = wpilib.Victor(3)
        self.motor4 = wpilib.Victor(4)
        
        self.dio1 = wpilib.DigitalInput(1)
        self.analog5 = wpilib.AnalogInput(5)
        
        self.stick = wpilib.Joystick(0)
        
        self.toggeled = True
        self.button = False
        
    def teleopPeriodic(self):
        self.motor1.set(1)
        
        self.motor2.set(self.stick.getX())
        
        if self.dio1.get():
            self.motor3.set(self.stick.getY())
        else:
            self.motor3.set(0)
        
        if wpilib.DriverStation.getInstance().getBatteryVoltage() < 9:
            self.motor1.set(0)
            self.motor2.set(0)
            self.motor3.set(0)
            
        if self.stick.getTrigger():
            self.toggeled = False
        elif not self.toggeled:
            self.toggeled = True
            self.button = not self.button
            
        if self.button:
            self.motor4.set(self.stick.getZ()) 
        
    def disabledPeriodic(self):
        self.motor1.set(0)
        self.motor2.set(0)
        self.motor3.set(0)
        self.motor4.set(0)

if __name__ == '__main__':
    wpilib.run(MyRobot)
