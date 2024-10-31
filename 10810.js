//한줄
// let input = require('fs')..readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt').toString().trim();

//여러줄
const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .trim()
    .split('\n');

const [N, M] = input[0].split(' ').map(Number);
const list = new Array(N).fill(0);

for (let a = 1; a <= M; a++) {
    let [start, end, k] = input[a].split(' ').map(Number);

    //바구니 덮어쓰기
    for (start; start <= end; start++) {
        list[start - 1] = k;
    }
}

console.log(list.join(' '));
