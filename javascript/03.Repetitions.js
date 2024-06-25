const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question(``, (answer) => {
    problem(answer)
    rl.close()
})

function problem(user_input){
    let longest = 0
    let prev = ''
    let streak = 0

    Array.from(user_input).forEach(x => {
        if(x == prev){
            streak++
        }else{
            longest = Math.max(longest, streak)
            streak = 1
        }
        prev = x
    })
    console.log(Math.max(longest, streak))
}