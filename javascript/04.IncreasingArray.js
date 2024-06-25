const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question('', limit => {
    rl.question('', userInput => {
        problem(userInput)
        rl.close()
    })
})

function problem(userInput) {
    let result = 0
    let nums = userInput.split(' ').map(Number).filter(isNumeric)
    if (nums.length > 1) {
        for (let index = 1; index < nums.length; index++) {
            const element = nums[index];
            const diff = element - nums[index - 1]
            if(diff<0){
                result += diff
                nums[index] = nums[index - 1]
            }

        }
    }
    console.log(Math.abs(result))
}

const isNumeric = x => (!isNaN(x) && parseFloat(x)) && isFinite(x)