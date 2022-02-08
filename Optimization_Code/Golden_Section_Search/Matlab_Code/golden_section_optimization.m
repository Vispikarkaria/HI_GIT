%%This code can be used to find the minimum or maximum of a single variable
%%function by using the golden section search 

% Inputs
% equation: It is recommended to enter a single variable equation with variable "x". Additionally, please use syms x at the start of your implementation. Eg: x^2 + 2
% initial_point: Enter the first point of your interval
% final_point: Enter the final point of your interval
% iteration_number: enter the number of iterations required
% error: Enter the error rate required 
% iter_error: Select whether you want to solve this problem by using number of iterations or error rate 
% Min_or_Max: Select whether you want to find the minimum or the maximum of the point 

% Outputs
% optimization_history: This will give you the history of x1 and x2 per iteration
% function_history: This will give you the history of f(x1) and f(x2) per iteration
% dis: This will give you the history of the delta function 
% final_interval: This will give you the final value of the result interval 
% final_result: This will give you the final result 


function [optimization_history, function_history, dis, final_interval, final_result] = golden_section_optimization(equation, initial_point, final_point, iteration_number, error, iter_error, Min_or_Max)

% This Part of code initializes all the variables 
f = equation;
optimization_history = [];
function_history = [];
x1 = initial_point;
x2 = final_point;
dis = [];
final_result = [];

%%This code will run if the user selects number of iterations as an option
if iter_error == "iter"
    for i = 0:iteration_number
        golden_ratio = ((sqrt(5)-1)/2);
        d = golden_ratio*(x2- x1);
        x1_new = x1 +(x2-x1)*0.382;
        x = x1_new;
        f1 = round(subs((f), x), 4);
        x2_new = x1 +(x2-x1)*0.618;
        x = x2_new;
        f2 = round(subs((f), x), 4);
        if Min_or_Max == 'Min'
            if f1>f2
                x1 = x1_new;
                x2 = x2;
            elseif f1<f2
                x1= x1;
                x2 = x2_new;
            end
        elseif Min_or_Max == 'Max'
            if f1>f2
                x1 = x1;
                x2 = x2_new;
            else
                x1= x1_new;
                x2 = x2;
            end
    
        else 
            display("Error in Function Calling");
        end
    function_history = [function_history, [f1 f2]];
    optimization_history = [optimization_history, [x1 x2]];
    dis = [dis, d];
    
    end
final_interval = [x1, x2];
final_result = (x1+x2)/2;

%%This code will run if the user selects as the error to stop the code
elseif iter_error == "error"
golden_ratio = ((sqrt(5)-1)/2);
d = golden_ratio*(x2- x1);

    while d >= error
        golden_ratio = ((sqrt(5)-1)/2);
        d = golden_ratio*(x2- x1);
        x1_new = x1 +(x2-x1)*0.382;
        x = x1_new;
        f1 = round(subs((f), x), 4);
        x2_new = x1 +(x2-x1)*0.618;
        x = x2_new;
        f2 = round(subs((f), x), 4);
        if Min_or_Max == 'Min'
            if f1>f2
                x1 = x1_new;
                x2 = x2;
            elseif f1<f2
                x1= x1;
                x2 = x2_new;
            end
        elseif Min_or_Max == 'Max'
            if f1>f2
                x1 = x1;
                x2 = x2_new;
            else
                x1= x1_new;
                x2 = x2;
            end
    
        else 
            display("Error in Function Calling")
        end
    function_history = [function_history, [f1 f2]];
    optimization_history = [optimization_history, [x1 x2]];
    dis = [dis, d];
    
    end 
final_interval = [x1, x2];
final_result = (x1+x2)/2;

    
%% This shows the error
else 
   display("Error in selecting iter_error")

end


end


