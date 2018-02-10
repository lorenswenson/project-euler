
a = function (perimeter){
    let sol= {solutions:"", number:0};
    for (n = 1; n<perimeter; n++){
        for (m=1; m<n; m++){
            c = Math.sqrt(n**2 + m**2);
            if (Number.isInteger(c) && n + m + c == perimeter) {
                sol.solutions += "{" + n + "," + m + "," + c + "}";
                sol.number += 1;
            }
        }
    }
    return sol;
};

function myOnload(){
    let bestSolution = NaN, maxSolutions = 0, bestPerimeter = 0;
    for (perimeter = 1; perimeter<1001; perimeter++){
        sol = a(perimeter);
        if (sol.number > maxSolutions) {
            bestSolution = sol;
            bestPerimeter = perimeter;
            maxSolutions = sol.number;
        }}
    document.getElementById("solution").innerHTML =
        "For " + bestPerimeter + " there are " + bestSolution.number +
        " solutions<br><br>They are: <br><br>" + bestSolution.solutions;
}
