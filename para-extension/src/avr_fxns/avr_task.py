"""AVR task functions"""

import math
import threading
from utilities import time_conversions

USE_OMEGA_ASSERTS = 0
USE_ASSERTS = 0
USE_DICT_PEAK_SPEED_RPM_RPM = 1

class AvrTask:

    """Class for handling AVR task operations"""

    def __init__(self,m,w,c,a,desc):
        self.m = m
        self.omega = w
        self.wcet = c
        self.alpha = a
        self.desc = desc
        self.mode_utils = [-1]*self.m

    def is_feasible(self):

        """Get whether accel values or util makes model infeasible on uniprocessor"""

        if self.alpha <= 0:

            return False

        highest_util = self.get_max_mode_utilization()

        if highest_util <= 1:

            return True

        return False

    def print_parameters(self):

        """Print Model Parameters"""

        print("AVR Task Params")

        print("M:",self.m)

        print("W:",self.omega)

        print("C:",self.wcet)

        print("A:",self.alpha)

    def calc_mode_utilizations(self):

        """Get max utilizations for all modes"""

        m = self.m

        assert m > 1

        self.mode_utils = [0]*(m+1)

        for i in range(1,m+1):

            self.mode_utils[i] = self.wcet[i]/self.t_bar_final_us(i)

    def get_max_mode_utilization(self):

        """Get max utilization of any mode"""

        self.calc_mode_utilizations()

        return max(self.mode_utils)

    def print_mode_utilizations(self):

        """Print all mode utilizations calculations"""

        if self.mode_utils[0] == -1:

            self.calc_mode_utilizations()

        for i in range(1,self.m+1):

            print(self.wcet[i],"us /",self.t_bar_final_us(i)," us = ",self.mode_utils[i],"%")

    def t_bar_final_us(self,i):

        """Get miat when accelerating maximally from \\omega_i for one rev"""

        assert i >= 1
        assert i <= self.m

        assert i % 1 == 0

        next_speed_max_accel = math.sqrt(self.omega[i]**2 + 2*self.alpha)

        next_speed_max_accel = min(self.omega[-1],next_speed_max_accel)

        miat_minutes = self.fxn_t_bar_min_rpm(self.omega[i],next_speed_max_accel)

        miat_us = time_conversions.fxn_min_to_us(miat_minutes)

        return miat_us

    def fxn_t_bar_min_rpm(self,omega_i,omega_j):

        """MIAT (in minutes) from \\omega_i to \\omega_j in minutes - honor peak limit"""

        omega_m = self.omega[-1]

        omega_i = min(omega_i,omega_m)
        omega_j = min(omega_j,omega_m)

        omega_p = self.fxn_peak_speed_rpm_rpm(omega_i, omega_j)

        if omega_p <= omega_m :

            miat_minutes = self.fxn_t_min_rpm(omega_i,omega_j)

        else:

            miat_minutes = self.fxn_t_p_min_rpm(omega_i, omega_j)

        return miat_minutes

    def fxn_peak_speed_rpm_rpm(self,omega_i,omega_j):

        """Get \\omega_p given \\omega_i, \\omega_j by rpm - returns in revolutions/min"""

        alpha = self.alpha

        p_rpm = math.sqrt((omega_i**2 + 2*alpha + omega_j**2)/2.0)

        return p_rpm

    def fxn_t_p_min_rpm(self,omega_i,omega_j):

        """MIAT in minutes when accelerating from
            \\omega_i to \\omega_j by rpm w/o exceeding \\omega_p"""

        p = self.fxn_peak_speed_rpm_rpm(omega_i, omega_j)

        assert p>0

        omega_m = self.omega[-1]
        alpha = self.alpha

        t_a = (omega_m-omega_i)/alpha
        t_n = (omega_i**2-2*omega_m**2+omega_j**2)/(2*alpha*omega_m) + (1/omega_m)
        t_d = (omega_m-omega_j)/alpha

        min_interarrival_time_minutes = t_a + t_n + t_d

        return min_interarrival_time_minutes

    def fxn_t_min_rpm(self,omega_i,omega_j):

        """Get MIAT from \\omega_i to \\omega_j in minutes -- without a maximum speed restriction"""

        alpha = self.alpha

        miat_minutes = (math.sqrt(2*omega_j**2 + 4*alpha + 2*omega_i**2) - omega_j - omega_i)/alpha

        return miat_minutes
