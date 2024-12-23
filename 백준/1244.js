const input = require('fs')
    .readFileSync(process.platform === 'linux' ? 0 : './data.txt')
    .toString()
    .split('\n');

const N = input.shift();
let arr = input.shift().split(" ").map(Number);
const studentsCount = input.shift();

for(let i=0; i<studentsCount; i++) {
    const [sex, num] = input[i].split(" ").map(Number);

    if(sex == 1){
        manCalculate(arr, num)
    }else{
        girlCalculate(arr, num)
    }
}

let output = '';
arr.forEach((data, index) => {
    output += data + ' ';

    if ((index + 1) % 20 === 0) {
        output += '\n';
    }
})

console.log(output)

function manCalculate(arr, num) {
    for(let i=1; i<=arr.length; i++) {
        //배수인 경우
        if(i % num == 0) {
            arr[i-1] = arr[i-1] == 1 ? 0 : 1;
        }
    }
}

function girlCalculate(arr, num) {
    let isDone = false;
    let left = num-2;
    let right = num;
    arr[num-1] = arr[num-1] == 1 ? 0 : 1;

    while(!isDone){
        if(left < 0 || right >= arr.length) {
            isDone = true;
            break;
        }

        if(arr[left] != arr[right]) {
            isDone = true;
            break;
        }

        arr[left] = arr[left] == 1 ? 0 : 1;
        arr[right] = arr[right] == 1 ? 0 : 1;

        left--;
        right++;
    }
}