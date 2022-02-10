syms delta
syms ('x', [1,4])
eq = x1^2 + (2*x2^2) + (2*x3^2) + (2*x1*x2) + (2*x2*x3) +x4
[optimization_history, final_result, f1, dis] = steepest_gradient_search(eq, [1 1 1 1],  2, "Min", 4)