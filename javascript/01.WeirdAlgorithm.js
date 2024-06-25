const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question(``, inp => {
    problem(inp)
    rl.close()
})

function problem(userInput){
    let num = parseInt(userInput)
    let arr = [num]
    while(num !== 1){
        if(num % 2 == 0) num = Math.floor(num / 2)
        else num = (num * 3) + 1
        arr.push(num)
    }
    console.log(arr.join(' '))
}

