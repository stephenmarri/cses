const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question(``, inp_one => {
    rl.question(``, inp_two => {
        problem(inp_one, inp_two)
        rl.close()
    })
})

function problem(limit, num){
    limit = parseInt(limit)
    let nums = num.split(' ').map(Number).filter(isNumeric)

    const sum_of_ap = Math.floor((limit * (limit + 1))/2)
    const sum_nums = nums.reduce((a,b)=> a+b, 0)
    console.log(sum_of_ap - sum_nums)
}

function isNumeric(x){
    return (!isNaN(x) && parseFloat(x)) && isFinite(x)
}