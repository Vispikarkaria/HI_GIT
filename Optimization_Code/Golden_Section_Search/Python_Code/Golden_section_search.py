#!/usr/bin/env python
# coding: utf-8

# In[66]:


class Optimization:
    def _init_(self):
        self.equation = equation
        self.iteration_number = iteration_number
        self.initial_point = initial_point
        self.final_point =final_point
        
        
    import numpy as np
    from sympy import symbols, Eq
    from sympy.functions import exp

        
    def golden_section_search(self, equation, iteration_number, initial_point, final_point,  error, iter_error, Min_or_Max):
        from sympy import symbols, Eq
        optimization_history = np.empty([1,1])
        function_history = np.empty([1,1])
        x1 = initial_point
        x2 =final_point
        dis = np.empty([1,1])
        iteration_number = iteration_number
        x = symbols('x')
        if iter_error == "iter":
            for i in range(0, iteration_number):
                golden_ratio = ((np.sqrt(5)-1)/2)
                d = golden_ratio*(x2- x1)
                x1_new = x1 +(x2-x1)*0.382;
                xs = x1_new;
                f1 = round(equation.subs(x, xs), 20)
                x2_new = x1 +(x2-x1)*0.618;
                xs = x2_new;
                f2 = round(equation.subs(x, xs), 20)
                if Min_or_Max == "Min":
                    if f1>f2:
                        x1 = x1_new;
                        x2 = x2;
                    elif f1<f2:
                        x1= x1;
                        x2 = x2_new;
                elif Min_or_Max == "Max":
                    if f1>f2:
                        x1 = x1;
                        x2 = x2_new;
                    else:
                        x1= x1_new;
                        x2 = x2;
                else:
                    print("Error in Function Calling of Minimum, and Maximum")

                function_history = [function_history, [f1, f2]]
                optimization_history = [optimization_history, [x1, x2]];
                dis = [dis, d]
        
        elif iter_error == "error":
            d = 10000
            while d>=error:
                golden_ratio = ((np.sqrt(5)-1)/2)
                d = golden_ratio*(x2- x1)
                x1_new = x1 +(x2-x1)*0.382;
                xs = x1_new;
                f1 = round(equation.subs(x, xs), 20)
                x2_new = x1 +(x2-x1)*0.618;
                xs = x2_new;
                f2 = round(equation.subs(x, xs), 20)
                if Min_or_Max == "Min":
                    if f1>f2:
                        x1 = x1_new;
                        x2 = x2;
                    elif f1<f2:
                        x1= x1;
                        x2 = x2_new;
                elif Min_or_Max == "Max":
                    if f1>f2:
                        x1 = x1;
                        x2 = x2_new;
                    else:
                        x1= x1_new;
                        x2 = x2;
                else:
                    print("Error in Function Calling of Minimum, and Maximum")

                function_history = [function_history, [f1, f2]]
                optimization_history = [optimization_history, [x1, x2]];
                dis = [dis, d]
        
        final_interval = "The final interval of " +Min_or_Max+ " is "+str([x1, x2]);
        final_result = "The final " +Min_or_Max+ " is "+str((x1+x2)/2);
        return optimization_history, final_interval, final_result


# In[67]:


##Example of how to run the code

Solution = Optimization()

from sympy import symbols, Eq
from sympy.functions import exp
import numpy as np
x = symbols('x')
f = 0.5 - (x*(exp(-(x**2))))
Solution.golden_section_search(f, 3, 0, 2, 0.01, "error","Min")

