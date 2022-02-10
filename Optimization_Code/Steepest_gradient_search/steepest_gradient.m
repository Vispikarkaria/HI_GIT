function [optimization_history, final_result, f1, dis] = steepest_gradient(equation, initial_point,  iteration_number, Min_or_Max)
xi = initial_point;
for i = 1:iteration_number
    syms delta
    syms ('x', [1,3])
    f = equation
    dfx = gradient(f);
    d = -[dfx];
    

    
    de = subs(d, x, xi);
    x0 = xi' + (delta*de);
    

    fdelta = subs(f, x, x0');
    fdelta_diff = diff(fdelta, delta);
    f_equation = fdelta_diff ==0;
    delta_val = solve(f_equation);
    
    xi = xi + (delta_val*de');

optimization_history = fdelta_diff;
final_result = xi;
f1 = 0;
f1 = delta_val;

dis = 0
final_result = round(xi, 10)
end
%%Answers 
