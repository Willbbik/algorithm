const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .trim()
    .split('\n')
    .map(Number);

const N = input[0];

//후보가 한명인 경우
if(N == 1){
    console.log(0);
    return;
}

//후보1번을 제외한 후보들 배열 생성
let arr = new Array(N-1);
for(let i=0; i<N-1; i++) {
    arr[i] = parseInt(input[i+2])
}

let count = 0;
let me = input[1];

call(arr);

console.log(count)


function call(list) {
    list.sort(function (a, b) {
        return b - a;
    });

    if(me > list[0]){
        return;
    }

    count++;
    me++;
    
    list[0] = list[0] - 1;    
    return call(list)
}