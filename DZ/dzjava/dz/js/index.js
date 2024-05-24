var sum = 0;
for(var i = 1; i<1000;i++)
{
    if (i % 3 == 0)
    {
        sum = sum + i;

    }
    else if (i % 5 == 0) {
        sum += i;

    }
}

console.warn("Итог:" + sum)


var x = new Array(new Array(20, 34, 2), new Array(9, 12, 18), new Array(3, 4, 5));
min = x[0][0]
for(var i = 0; i<x.length;i++){
    for(var h = 0; h<x[i].length;h++)
    {

        if(min>x[i][h]){
            min = x[i][h]
        }
    }
}
console.log("Min num :" + min)

