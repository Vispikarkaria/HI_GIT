#!/usr/bin/env python
# coding: utf-8

# In[148]:


class Optimization:
    def _init_(self):
        self.equation = equation
        self.iteration_number = iteration_number
        self.initial_point = initial_point
        self.final_point =final_point
        
        
    import numpy as np
    from sympy import symbols, Eq
    from sympy.functions import exp

        
    def golden_section_search(self, equation, iteration_number, initial_point, final_point):
        from sympy import symbols, Eq
        optimization_history = np.empty([1,1])
        function_history = np.empty([1,1])
        x1 = initial_point
        x2 =final_point
        dis = np.empty([1,1])
        iteration_number = iteration_number
        x = symbols('x')
        for i in range(1, iteration_number):
            golden_ratio = ((np.sqrt(5)-1)/2)
            d = golden_ratio*(x2- x1)
            x1_new = x1 + d;
            xs = x1_new;
            f1 = round(equation.subs(x, xs), 4)
            x2_new = x2 - d;
            xs = x2_new;
            f2 = round(equation.subs(x, xs), 4)

            if f1>f2:
                x1 = x1;
                x2 = x2_new;
            elif f1<f2:
                x1= x1_new;
                x2 = x2;
            function_history = [function_history, [f1, f2]]
            optimization_history = [optimization_history, [x1, x2]];
            dis = [dis, d]
        return optimization_history

        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




